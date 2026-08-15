from typing import Optional
from pydantic import BaseModel


class AgentReview(BaseModel):
    agent: str
    review: str


class RiskAssessment(BaseModel):
    score: int
    level: str


class FileReview(BaseModel):
    filename: str
    summary: str
    risk: RiskAssessment
    reviews: list[AgentReview]


class AIReviewResponse(BaseModel):
    title: str
    author: str
    review_count: int
    duration_seconds: float
    reviews: list[FileReview]
    report_path: Optional[str] = None