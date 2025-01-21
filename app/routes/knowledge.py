from fastapi import APIRouter
from app.services.retrieval import insert_document, fetch_documents

router = APIRouter()

@router.post("/")
async def add_knowledge(title: str, content: str):
    """
    Add a knowledge document with its title and content.
    """
    document_id = insert_document(title, content)
    return {"message": "Document added successfully", "id": document_id}

@router.get("/")
async def get_knowledge(query: str):
    """
    Retrieve documents related to the query.
    """
    results = fetch_documents(query)
    return {"results": results}