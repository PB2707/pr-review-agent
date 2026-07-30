from pydantic import BaseModel


class AgentReview(BaseModel):
    agent: str
    review: str


class FileReview(BaseModel):
    filename: str
    summary: str
    reviews: list[AgentReview]


class AIReviewResponse(BaseModel):
    title: str
    author: str
    review_count: int
    duration_seconds: float
    reviews: list[FileReview]