from pymongo import MongoClient
from app.utils.openai_client import generate_embedding
from decouple import config

client = MongoClient(config("MONGO_URI"))
db = client["rag_chatbot"]
collection = db["knowledge"]

def insert_document(title, content):
    embedding = generate_embedding(content)
    document = {
        "title": title,
        "content": content,
        "embedding": embedding
    }
    result = collection.insert_one(document)
    return str(result.inserted_id)

def fetch_documents(query, top_k=5):
    query_embedding = generate_embedding(query)
    pipeline = [
        {
            "$search": {
                "index": "default",
                "knnBeta": {
                    "vector": query_embedding,
                    "path": "embedding",
                    "k": top_k
                }
            }
        }
    ]
    return list(collection.aggregate(pipeline))