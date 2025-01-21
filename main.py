from fastapi import FastAPI
from app.routes import chat, knowledge

# Initialize FastAPI app
app = FastAPI(title="RAG Chatbot API", version="1.0")

# Include routes
app.include_router(chat.router, prefix="/api/chat", tags=["Chat"])
app.include_router(knowledge.router, prefix="/api/knowledge", tags=["Knowledge"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the RAG Chatbot API"}

@app.get("/model")
def get_model_info():
    return {"model": "gpt-4o", "description": "Using the latest OpenAI GPT-4o model for responses."}
