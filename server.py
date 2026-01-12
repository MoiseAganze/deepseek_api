from fastapi import FastAPI
from ai import AI
from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str

app = FastAPI(title="Mon premier serveur FastAPI")

@app.get("/")
def home():
    return {"message": "Bienvenue dans Deepseek ai 🚀"}

@app.post("/message")
def chat(chat_request: ChatRequest):
    ai=AI()
    user_text=chat_request.message
    ai_response=ai.chat(user_text)
    return {"status": "ok","user_message":user_text,"ai_response":ai_response}

