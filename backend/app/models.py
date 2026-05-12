from pydantic import BaseModel, Field
from typing import List

class ExcuseRequest(BaseModel):
    situation: str = Field(..., description="The situation requiring an excuse")
    tone: str = Field(..., description="The tone of the excuse (Professional, Casual, Dramatic, Funny, Emotional)")
    urgency: float = Field(..., description="The urgency level (0-100)")
    relationship: str = Field(..., description="Relationship to the recipient (Boss, Friend, Teacher, Partner, Parent)")

class ExcuseResponse(BaseModel):
    main_excuse: str
    emotional_reasoning: str
    whatsapp_message: str
    email_message: str
    follow_up_answers: List[str]
    risk_score: float
