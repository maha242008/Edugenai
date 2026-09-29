from typing import List

from pydantic import BaseModel, Field


class QuestionRequest(BaseModel):
    question: str = Field(..., min_length=1)


class TextRequest(BaseModel):
    text: str = Field(..., min_length=1)


class QuizRequest(BaseModel):
    topic: str = Field(..., min_length=1)


class LearningPathRequest(BaseModel):
    topic: str = Field(..., min_length=1)
    level: str = "beginner"


class AIResponse(BaseModel):
    answer: str


class QuizQuestion(BaseModel):
    question: str
    options: List[str]
    answer: str
    explanation: str = ""


class QuizResponse(BaseModel):
    questions: List[QuizQuestion]