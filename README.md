# reddit-scraper-clustering
# Reddit Scraper with Clustering

This project implements a Reddit scraper that extracts posts from specified subreddits, processes the data using Natural Language Processing (NLP) techniques, and applies clustering algorithms to group similar posts together. The project also features automation for periodic scraping and keyword-based search functionality.

## Key Features
- **Reddit API Integration**: Scrapes posts from subreddits using the Reddit API (PRAW).
- **MongoDB Storage**: Stores scraped posts and their metadata in a MongoDB database for persistent storage.
- **Text Vectorization**: Uses **Doc2Vec** to convert Reddit posts into vector representations for clustering.
- **Clustering Algorithm**: Applies **KMeans** clustering to group similar posts based on their content.
- **Keyword Extraction**: Uses **TF-IDF** for keyword extraction to facilitate querying posts by relevant topics.
- **Data Visualization**: Visualizes the clustered posts using dimensionality reduction techniques such as **t-SNE** and **PCA**.
- **Automation**: Automatically fetches new posts at specified intervals and updates the database with newly clustered posts.

## Technologies Used
- **Python**: The primary programming language for all scripts.
- **MongoDB**: NoSQL database used for storing Reddit posts.
- **PRAW (Python Reddit API Wrapper)**: Library used for fetching Reddit posts.
- **Gensim**: Library used for training the **Doc2Vec** model.
- **scikit-learn**: Used for **KMeans** clustering and **TF-IDF** keyword extraction.
- **matplotlib**: Visualization library for plotting the clusters.

## Project Structure
reddit-scraper-clustering/
│
├── README.md
├── requirements.txt
├── automation.py       # Script for automating periodic updates
├── clustering.py       # Script for clustering Reddit posts
├── database.py         # MongoDB connection handler
├── extract.py          # Reddit post extraction and keyword extraction
├── query_cluster.py    # Search and visualize clusters based on keywords
├── model.py            # Helper functions for text processing and model training
├── settings.py         # Stores API keys and other configuration settings
└── .gitignore          # Ignore sensitive files like .env

## Setup Instructions

### 1. Clone the Repository:
```bash
git clone https://github.com/your-username/reddit-scraper-clustering.git
cd reddit-scraper-clustering

virtualenv env
source env/bin/activate  # For Windows: env\Scripts\activate

pip install -r requirements.txt

REDDIT_CLIENT_ID=your-client-id
REDDIT_CLIENT_SECRET=your-client-secret
REDDIT_USER_AGENT=your-user-agent
MONGO_URI=mongodb://localhost:27017/
MONGO_DB_NAME=reddit_db
MONGO_COLLECTION_NAME=posts

#Run the Scraper and Clustering:
	•	To fetch posts periodically and update clusters:
python automation.py

	•	To query clusters by keyword and visualize them:
python query_cluster.py
