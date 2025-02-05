## 🔥 Reddit Scraper & Clustering: Uncover Hidden Topics with AI

Automated Reddit Scraping, Intelligent Clustering, and Data-Driven Insights
Ever wondered what people are talking about on Reddit? This project lets you scrape Reddit posts, analyze trends, and cluster discussions into meaningful topics—all with powerful machine learning and NLP techniques.

From data extraction to clustering and visualizing patterns, this project helps you automate insights from Reddit communities! 🚀

## 📌 Table of Contents

- 🎯 Features
- 🛠️ Technologies Used
- 📂 Project Structure
- ⚙️ Installation
- 🚀 How to Use
- 🧠 Clustering Techniques
- 📊 Results & Visualizations
- 📜 License

## 🎯 Features
- **Automated Reddit Scraping** – Collects posts from subreddits using the **Reddit API**
- **Text Cleaning & Preprocessing** – Removes stopwords, lemmatizes text, and prepares for clustering
- **AI-Powered Clustering** – Uses **K-Means, DBSCAN, PCA, and t-SNE** to uncover hidden patterns
- **Interactive Visualizations** – Generates plots to explore Reddit discussions intuitively
- **End-to-End Automation** – Run the entire pipeline with a single script

## 🛠️ Technologies Used
- **🐍 Python** – Core programming language
- **📊 Pandas & NumPy** – Data manipulation and numerical computing
- **🛢️ MongoDB** – NoSQL database for storing Reddit posts efficiently
- **🌐 PRAW (Python Reddit API Wrapper)**: Library used for fetching Reddit posts.
- **🧠 Gensim** – Topic modeling and word embeddings (Word2Vec, LDA)
- **🤖 Scikit-Learn** – Machine learning algorithms (K-Means, DBSCAN)
- **📈 Matplotlib** – Data visualization

## 📂 Project Structure

	📂 reddit-scraper-clustering
	├── automation.py        # Runs the entire pipeline in one go  
	├── clustering.py        # Applies K-Means, DBSCAN, PCA, and t-SNE  
	├── database.py          # Stores and retrieves Reddit posts  
	├── download.py          # Fetches Reddit data using API  
	├── extract.py           # Cleans and preprocesses text  
	├── main.py              # Entry point for running the project  
	├── clusters_pca.png     # PCA visualization of clustered data  
	├── clusters_tsne.png    # t-SNE visualization of clusters  
	├── README.md            # Project documentation  
	└── requirements.txt     # Python dependencies  


## ⚙️ Installation

### 🔧 Step 1: Clone the Repository
	git clone https://github.com/yourusername/reddit-scraper-clustering.git
	cd reddit-scraper-clustering
 
###  📦 Step 2: Install Dependencies
	pip install -r requirements.txt

### 🔑 Step 3: Get Reddit API Credentials
	1. Go to Reddit's Developer Portal.
	2. Create a script-based app.
	3. Note down your client ID, client secret, and user agent.
	4. Add these to your project’s authentication settings.

## 🚀 How to Use

### 📥 1. Scrape Reddit Data
Modify download.py to specify subreddits and keywords, then run:

	python download.py
This will collect posts and store them in a database.

### 🔍 2. Extract & Clean Data
Prepare text data for clustering:

	python extract.py
This removes stopwords, punctuation, and unwanted noise for better analysis.

### 🤖 3. Perform AI-Powered Clustering
Run:

	python clustering.py
K-Means Clustering: Groups similar posts together
DBSCAN: Identifies dense topic clusters
PCA & t-SNE: Creates stunning visualizations of Reddit topics

### 🔄 4. Automate Everything
Run the full pipeline in one go:

	python automation.py

## 🧠 Clustering Techniques  

| **Method** | **Purpose** |
|------------|------------|
| **K-Means Clustering** | Groups similar Reddit posts into topics |
| **DBSCAN** | Finds dense, noise-resistant clusters |
| **PCA (Principal Component Analysis)** | Reduces dimensionality for visualization |
| **t-SNE (t-distributed Stochastic Neighbor Embedding)** | Creates high-quality 2D visualizations |

## 📊 Results & Visualizations
Once clustering is complete, you’ll get:

📌 PCA-Based Clustering (clusters_pca.png) – Shows high-level structure of topics.  
📌 t-SNE-Based Clustering (clusters_tsne.png) – Provides a detailed, nonlinear visualization.

These interactive insights help uncover what Reddit communities are discussing!

## 📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

