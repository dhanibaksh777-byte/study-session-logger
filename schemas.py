from pydantic import BaseModel
from typing import Optional

class ChatRequest(BaseModel):
    message : str


class StudyLogs(BaseModel):
    subject : Optional[str]
    duration_minutes : Optional[int]
    topics : Optional[list[str]] = None




