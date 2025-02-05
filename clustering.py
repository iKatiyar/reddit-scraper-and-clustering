# clustering.py (updated)

import numpy as np
import matplotlib

matplotlib.use("Agg")  # Use the non-GUI Agg backend
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from database import get_db


# Fetch posts from the database for clustering
def fetch_posts_for_clustering():
    collection = get_db()
    posts = list(
        collection.find({}, {"content": 1, "title": 1, "keywords": 1})
    )  # Fetch content, title, and keywords
    return posts


# Prepare the documents for Doc2Vec
def prepare_tagged_documents(posts):
    return [
        TaggedDocument(post["content"].split(), [i]) for i, post in enumerate(posts)
    ]


# Train the Doc2Vec model
def train_doc2vec_model(tagged_documents):
    model = Doc2Vec(vector_size=100, window=5, min_count=2, workers=4)

    # Build vocabulary before training
    model.build_vocab(tagged_documents)
    print("Vocabulary built successfully.")

    # Now, train the model
    model.train(tagged_documents, total_examples=model.corpus_count, epochs=40)
    print("Doc2Vec model trained successfully.")

    return model


# Perform clustering using KMeans
def perform_clustering(doc_vectors, num_clusters=5):
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    clusters = kmeans.fit_predict(normalize(doc_vectors))
    return clusters


# Cluster posts and store cluster labels in the database
def cluster_posts(num_clusters=5, display=True):
    posts = fetch_posts_for_clustering()
    if not posts:
        print("No posts found to cluster.")
        return

    tagged_documents = prepare_tagged_documents(posts)

    # Train the Doc2Vec model
    model = train_doc2vec_model(tagged_documents)

    # Get the document vectors for clustering
    doc_vectors = np.array([model.dv[i] for i in range(len(posts))])

    # Perform clustering
    cluster_labels = perform_clustering(doc_vectors, num_clusters)

    # Calculate silhouette score to evaluate clustering quality
    silhouette_avg = silhouette_score(doc_vectors, cluster_labels)
    print(f"Silhouette Score: {silhouette_avg}")

    # Update each post with its cluster label in the database
    for i, post in enumerate(posts):
        get_db().update_one(
            {"_id": post["_id"]}, {"$set": {"cluster": int(cluster_labels[i])}}
        )

    # Optionally visualize clusters
    if display:
        visualize_clusters(doc_vectors, cluster_labels, posts, num_clusters)

    return cluster_labels


# Visualize clusters using t-SNE or PCA
def visualize_clusters(
    doc_vectors, cluster_labels, posts, num_clusters, use_tsne=False
):
    # Reduce dimensions using PCA or t-SNE
    if use_tsne:
        from sklearn.manifold import TSNE

        tsne = TSNE(n_components=2, random_state=42, perplexity=30, n_iter=1000)
        reduced_vectors = tsne.fit_transform(doc_vectors)
    else:
        pca = PCA(n_components=2)
        reduced_vectors = pca.fit_transform(doc_vectors)

    # Plot clusters
    plt.figure(figsize=(10, 7))
    colors = plt.cm.get_cmap("tab10", num_clusters)

    for cluster in range(num_clusters):
        indices = np.where(cluster_labels == cluster)
        cluster_points = reduced_vectors[indices]
        plt.scatter(
            cluster_points[:, 0],
            cluster_points[:, 1],
            label=f"Cluster {cluster}",
            c=[colors(cluster)],
        )

    plt.title("Clusters of Reddit Posts")
    plt.xlabel("Component 1")
    plt.ylabel("Component 2")
    plt.legend()

    # Save the plot
    plt.savefig("clusters_tsne.png" if use_tsne else "clusters_pca.png")
    print(
        f"Cluster visualization saved as {'clusters_tsne.png' if use_tsne else 'clusters_pca.png'}"
    )

    # Display top keywords per cluster
    print("\nTop Keywords per Cluster:")
    for cluster in range(num_clusters):
        cluster_posts = [
            posts[i] for i in range(len(posts)) if cluster_labels[i] == cluster
        ]
        print(f"\nCluster {cluster}:")
        for post in cluster_posts:
            title = post.get("title", "No title available")
            keywords = ", ".join(post.get("keywords", []))
            print(f"- {title} (Keywords: {keywords})")
