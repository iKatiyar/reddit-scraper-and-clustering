# query_cluster.py (updated)

from sklearn.metrics.pairwise import cosine_similarity
from database import get_db
from clustering import (
    fetch_posts_for_clustering,
    prepare_tagged_documents,
    train_doc2vec_model,
    perform_clustering,
    visualize_clusters,
)
import numpy as np


# Function to filter posts by keyword within the current clustering session
def find_posts_by_cluster(user_query):
    db = get_db()
    # Search for posts containing the keyword in their list of extracted keywords
    posts = db.find(
        {"keywords": {"$in": [user_query]}}, {"title": 1, "content": 1, "cluster": 1}
    )

    clusters = {}
    for post in posts:
        cluster_id = post.get("cluster", "Unknown")
        if cluster_id not in clusters:
            clusters[cluster_id] = []
        clusters[cluster_id].append(post)

    return clusters


# Function to find the closest matching cluster based on user input (query)
def find_closest_cluster(user_input, model, doc_vectors, cluster_labels):
    input_vector = model.infer_vector(user_input.split())
    similarities = cosine_similarity([input_vector], doc_vectors)[0]
    closest_idx = np.argmax(similarities)
    closest_cluster = cluster_labels[closest_idx]
    return closest_cluster


if __name__ == "__main__":
    user_input = input("Enter keywords or a message to search: ")

    # Fetch the posts and train the clustering model
    posts = fetch_posts_for_clustering()
    tagged_documents = prepare_tagged_documents(posts)
    model = train_doc2vec_model(tagged_documents)
    doc_vectors = np.array([model.dv[i] for i in range(len(posts))])
    cluster_labels = perform_clustering(doc_vectors)

    # Check for exact keyword matches within the posts
    cluster_posts = find_posts_by_cluster(user_input)
    if cluster_posts:
        print(f"\nClusters containing posts with keyword '{user_input}':\n")
        for cluster, posts in cluster_posts.items():
            print(f"Cluster {cluster}:")
            for post in posts:
                print(f"- {post['title']} (Preview: {post['content'][:100]}...)")
            print("\n")
    else:
        # If no exact match, proceed to find the closest cluster using similarity
        closest_cluster = find_closest_cluster(
            user_input, model, doc_vectors, cluster_labels
        )
        cluster_posts = [
            posts[i] for i in range(len(posts)) if cluster_labels[i] == closest_cluster
        ]

        # Display posts in the closest cluster
        print(f"\nPosts from Cluster {closest_cluster}:")
        for post in cluster_posts:
            print(f"- {post['title']} (Keywords: {', '.join(post['keywords'])})")

    # Visualize the closest cluster
    visualize_clusters(
        doc_vectors, cluster_labels, posts, num_clusters=5, use_tsne=True
    )
