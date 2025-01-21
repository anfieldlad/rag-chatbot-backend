from pydantic import BaseModel

class ChatRequest(BaseModel):
    user_message: str

class ChatResponse(BaseModel):
    user_message: str
    ai_response: str

class KnowledgeDocument(BaseModel):
    title: str
    content: str