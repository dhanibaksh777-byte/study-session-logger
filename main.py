from fastapi import FastAPI
from groq_client import get_conversation
from System_prompt import SYSTEM_PROMPT
from schemas import ChatRequest,StudyLogs
import json
from fastapi import HTTPException

app = FastAPI()

@app.post("/chat")
def chat(request: ChatRequest):
    Conversation = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": request.message}
    ]

    try:
        bot_reply = get_conversation(Conversation)
        parsed_data = json.loads(bot_reply)
        return StudyLogs(**parsed_data)
    except Exception as e:
        print(f"ERROR: {e}")
        raise HTTPException(status_code=500, detail="Something went wrong")