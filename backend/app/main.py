from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.chat import router as chat_router
from app.routes.emergency import router as emergency_router
from app.routes.info import router as info_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(chat_router)
app.include_router(emergency_router)
app.include_router(info_router)

@app.get("/")
def home():

    return {
        "status":"running"
    }
