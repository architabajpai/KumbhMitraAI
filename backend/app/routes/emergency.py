from fastapi import APIRouter

router = APIRouter()

EMERGENCY_WORDS = [
    "help",
    "accident",
    "lost child",
    "medical emergency",
    "danger",
    "fire"
]

@router.post("/detect")
def detect(payload: dict):

    text = payload["message"].lower()

    emergency = any(
        word in text
        for word in EMERGENCY_WORDS
    )

    return {
        "emergency": emergency
    }
