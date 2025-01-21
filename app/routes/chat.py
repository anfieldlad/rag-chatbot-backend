from fastapi import APIRouter
from app.utils.openai_client import get_openai_response

router = APIRouter()

@router.post("/")
async def chat(user_message: str):
    """
    Handles user chat input and returns AI response.
    """
    ai_response = get_openai_response(user_message)
    return {"user_message": user_message, "ai_response": ai_response}