# automation.py

import time
import threading
from extract import fetch_reddit_posts
from clustering import cluster_posts


def periodic_update(subreddit, interval_minutes):
    while True:
        print("Fetching new posts...")
        try:
            fetch_reddit_posts(subreddit_name=subreddit, num_posts=10)
            print("Posts fetched successfully. Now clustering...")
            cluster_posts()
            print("Clustering complete. Database updated.")
        except Exception as e:
            print(f"Error during update: {e}")
        time.sleep(interval_minutes * 60)  # Convert minutes to seconds


def run_periodically(subreddit, interval_minutes):
    thread = threading.Thread(
        target=periodic_update, args=(subreddit, interval_minutes)
    )
    thread.daemon = True
    thread.start()
    return thread


if __name__ == "__main__":
    interval_minutes = int(input("Enter the interval in minutes for updates: "))
    subreddit = input("Enter subreddit name: ")
    run_periodically(subreddit, interval_minutes)
    input("Press Enter to stop the script at any time...\n")
