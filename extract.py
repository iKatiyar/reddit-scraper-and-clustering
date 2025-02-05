# extract.py
import praw
from model import (
    clean_html,
    extract_text_from_image,
    mask_username,
    retry_on_failure,
    extract_keywords_tfidf,
)
from database import insert_many_posts
from datetime import datetime
import logging
from settings import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT

# PRAW Setup
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT,
)


# Fetch Reddit posts with all required fields
@retry_on_failure
def fetch_reddit_posts(subreddit_name, num_posts):
    subreddit = reddit.subreddit(subreddit_name)
    posts_data = []
    combined_texts = []  # For keyword extraction later

    for post in subreddit.new(limit=num_posts):
        try:
            print(post)
            # Clean title and selftext
            title_clean = clean_html(post.title)
            selftext_clean = clean_html(post.selftext)

            # Mask username
            username_masked = mask_username(post.author.name)

            # Extract image text if image exists
            image_text = ""
            if post.url.endswith(("jpg", "jpeg", "png")):
                image_text = extract_text_from_image(post.url)

            # Combine all content for keyword extraction
            combined_text = f"{title_clean} {selftext_clean} {image_text}"
            combined_texts.append(combined_text)

            # Collect additional fields
            post_data = {
                "title": title_clean,
                "author": username_masked,
                "num_comments": post.num_comments,
                "url": post.url,
                "selftext": selftext_clean,
                "created_utc": datetime.utcfromtimestamp(post.created_utc).isoformat(),
                "upvote_ratio": post.upvote_ratio,
                "score": post.score,
                "num_crossposts": post.num_crossposts,
                "preview": (
                    post.preview["images"][0]["source"]["url"]
                    if "preview" in post.__dict__
                    else ""
                ),
                "permalink": post.permalink,
                "domain": post.domain,
                "content": combined_text,
                "keywords": [],
            }

            posts_data.append(post_data)
        except Exception as e:
            logging.error(f"Failed to process post: {e}")

    # Keyword extraction using TF-IDF
    keywords_list = extract_keywords_tfidf(combined_texts)
    for idx, keywords in enumerate(keywords_list):
        posts_data[idx]["keywords"] = keywords

    # Store in MongoDB
    insert_many_posts(posts_data)

    return posts_data
