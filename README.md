# 🔍 Reddit Scraper & Topic Clustering

> End-to-end NLP pipeline — scrape Reddit posts via the Reddit API, extract TF-IDF keywords, embed with Doc2Vec, cluster with K-Means, and visualize with PCA and t-SNE. All posts stored in MongoDB.

---

## ✨ What It Does

Point it at any subreddit → it automatically:
1. **Scrapes** posts (title, body, comments, score, upvote ratio, preview images)
2. **Cleans** content — strips HTML, masks usernames for privacy, runs OCR on image posts
3. **Extracts keywords** using TF-IDF across all fetched posts
4. **Embeds** documents using **Doc2Vec** (100-dimensional vectors)
5. **Clusters** with **K-Means** + evaluates quality via silhouette score
6. **Visualizes** clusters in 2D using **PCA** and **t-SNE**
7. **Stores** everything (posts + cluster labels) in **MongoDB**

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Gensim](https://img.shields.io/badge/Gensim-Doc2Vec-4B8BBE?style=flat-square&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square&logoColor=white)

---

## 🔄 Pipeline

```
Subreddit Input
      │
      ▼
┌─────────────────┐
│  PRAW Scraper   │  Fetches posts: title, body, score,
│  (extract.py)   │  comments, upvote ratio, preview, permalink
│                 │  + OCR on image posts (Tesseract)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  NLP Processor  │  HTML cleaning, username masking,
│  (model.py)     │  TF-IDF keyword extraction per post
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    MongoDB      │  Stores all post data + keywords
│  (database.py)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Doc2Vec        │  Trains on post content →
│  Embeddings     │  100-dim document vectors
│  (clustering.py)│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  K-Means        │  Clusters posts into N topics
│  + Silhouette   │  Evaluates quality with silhouette score
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  PCA / t-SNE    │  Reduces to 2D for visualization
│  Visualization  │  Saves clusters_pca.png / clusters_tsne.png
└─────────────────┘
```

---

## 🏗️ Architecture

```
reddit-scraper-and-clustering/
├── main.py          # Entry point — interactive CLI
├── automation.py    # One-command full pipeline runner
├── extract.py       # Reddit scraping via PRAW
├── model.py         # NLP: HTML cleaning, OCR, TF-IDF, username masking
├── clustering.py    # Doc2Vec training, K-Means, PCA/t-SNE visualization
├── database.py      # MongoDB connection + insert/query helpers
├── query_cluster.py # Query posts by cluster label
├── schema.py        # Post schema definition
├── settings.py      # API credentials (loaded from env)
├── requirements.txt
└── clusters_pca.png / clusters_tsne.png  # Output visualizations
```

---

## 🚀 Running Locally

### Prerequisites
- Python 3.10+
- MongoDB running locally or a MongoDB Atlas URI
- Reddit API credentials ([create app here](https://www.reddit.com/prefs/apps))
- Tesseract OCR (optional, for image post text extraction)

### Install & configure

```bash
git clone https://github.com/iKatiyar/reddit-scraper-and-clustering.git
cd reddit-scraper-and-clustering

pip install -r requirements.txt
```

Edit `settings.py` with your credentials:

```python
REDDIT_CLIENT_ID     = "your_client_id"
REDDIT_CLIENT_SECRET = "your_client_secret"
REDDIT_USER_AGENT    = "your_app_name"
MONGO_URI            = "mongodb://localhost:27017"
MONGO_DB_NAME        = "reddit_clustering"
MONGO_COLLECTION_NAME = "posts"
```

### Run the full pipeline

```bash
python automation.py
```

Or step by step:

```bash
python main.py        # Scrape posts interactively
python clustering.py  # Embed, cluster, and visualize
```

---

## 📊 Clustering Methods

| Method | Role |
|--------|------|
| **TF-IDF** | Keyword extraction per post |
| **Doc2Vec** | 100-dim semantic document embeddings |
| **K-Means** | Partition posts into N topic clusters |
| **Silhouette Score** | Evaluate cluster quality (−1 to +1) |
| **PCA** | Linear 2D reduction for fast visualization |
| **t-SNE** | Nonlinear 2D reduction for detailed topology |

---

## 📡 Output

- `clusters_pca.png` — PCA 2D cluster plot with color-coded topics
- `clusters_tsne.png` — t-SNE 2D cluster plot
- MongoDB collection updated with `cluster` label on every post
- CLI output of top keywords per cluster
