from fastapi import APIRouter

from app.models.chat import ChatRequest
from app.services.gemini_service import ask_gemini

from app.database.mongodb import chat_collection

router = APIRouter()

@router.post("/chat")
def chat(req: ChatRequest):

    answer = ask_gemini(req.message, req.language)

    chat_collection.insert_one({
        "user": req.message,
        "assistant": answer
    })

    return {
        "answer": answer
    }
