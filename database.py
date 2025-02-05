# database.py
import pymongo
from settings import MONGO_URI, MONGO_DB_NAME, MONGO_COLLECTION_NAME


def get_db():
    client = pymongo.MongoClient(MONGO_URI)
    db = client[MONGO_DB_NAME]
    return db[MONGO_COLLECTION_NAME]


def insert_many_posts(posts_data):
    collection = get_db()
    if posts_data:
        collection.insert_many(posts_data)
