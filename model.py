# model.py
import re
from bs4 import BeautifulSoup
import pytesseract
import requests
from PIL import Image
import logging
import time
import random
from sklearn.feature_extraction.text import TfidfVectorizer


# Helper function to clean HTML
def clean_html(text):
    soup = BeautifulSoup(text, "html.parser")
    clean_text = soup.get_text()
    clean_text = re.sub(r"[^A-Za-z0-9\s]+", "", clean_text)  # Remove special characters
    return clean_text.strip()


# Mask usernames to maintain privacy
def mask_username(username):
    return f"user_{hash(username) % 10000}"


# Extract text from images using pytesseract
def extract_text_from_image(url):
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        logging.warning(f"Failed to extract text from image: {url}. Error: {e}")
        return ""


# Retry decorator to handle failures
def retry_on_failure(func):
    def wrapper(*args, **kwargs):
        retries = 3
        while retries > 0:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                retries -= 1
                logging.warning(f"Error: {e}, retrying... ({3 - retries} attempts)")
                time.sleep(5 + random.randint(1, 5))  # Random backoff
        raise Exception("Max retries exceeded")

    return wrapper


# Advanced keyword extraction using TF-IDF
def extract_keywords_tfidf(texts):
    vectorizer = TfidfVectorizer(
        stop_words="english", max_features=50
    )  # Increase max features to capture more words
    X = vectorizer.fit_transform(texts)
    feature_names = vectorizer.get_feature_names_out()
    tfidf_scores = X.toarray()

    keywords_list = []
    for doc_scores in tfidf_scores:
        top_keywords_idx = doc_scores.argsort()[-5:][
            ::-1
        ]  # Extract top 5 keywords per post
        keywords = [feature_names[idx] for idx in top_keywords_idx]
        keywords_list.append(keywords)
    return keywords_list
