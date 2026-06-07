from pymongo import MongoClient
from app.config import MONGODB_URI

client = MongoClient(MONGODB_URI)

db = client["mahakumbh"]

chat_collection = db["chat_history"]
