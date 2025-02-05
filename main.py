# main.py
import logging
from extract import fetch_reddit_posts
from schema import post_schema


def display_post(post, index):
    """
    Displays a single post using the expected schema.
    """
    print(f"Post {index}:")
    print(f"Title: {post.get('title', 'No title')}")
    print(f"Author: {post.get('author', 'Unknown')}")
    print(f"URL: {post.get('url', 'No URL')}")
    print(f"Comments: {post.get('num_comments', 0)}")
    print(f"Score: {post.get('score', 0)}")
    print(f"Upvote Ratio: {post.get('upvote_ratio', 0.0)}")
    print(f"Domain: {post.get('domain', 'Unknown')}")
    print(
        f"Content Preview: {post.get('selftext', 'No content available')[:100]}..."
    )  # Short preview of content
    print(f"Created (UTC): {post.get('created_utc', 'Unknown time')}")
    print(f"Number of Crossposts: {post.get('num_crossposts', 0)}")
    print(f"Keywords: {', '.join(post.get('keywords', []))}")
    print(f"Preview Image: {post.get('preview', 'No preview available')}")
    print(f"Permalink: {post.get('permalink', 'No permalink available')}")
    print()  # Blank line for readability


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    subreddit_name = input("Enter subreddit name: ")
    num_posts = int(input("Enter number of posts to fetch: "))

    # Fetch the posts
    posts = fetch_reddit_posts(subreddit_name, num_posts)

    # Log the number of posts fetched
    logging.info(f"Fetched and stored {len(posts)} posts from {subreddit_name}")

    # Display the first 20 posts or fewer if less than 20 are fetched
    print("\nDisplaying the first 20 posts:\n")
    for i, post in enumerate(posts[:20], start=1):
        display_post(post, i)
