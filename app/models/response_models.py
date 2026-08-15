from pydantic import BaseModel
from typing import Optional

from pydantic import BaseModel


class AgentReview(BaseModel):
    agent: str
    review: str


class FileReview(BaseModel):
    filename: str
    summary: str
    reviews: list[AgentReview]


class ReviewResponse(BaseModel):
    title: str
    author: str
    review_count: int
    duration_seconds: float
    reviews: list[FileReview]






class ChangedFile(BaseModel):
    filename: str
    status: str
    additions: int
    deletions: int
    changes: int
    patch: Optional[str] = None


class PullRequestDetails(BaseModel):
    title: str
    author: str
    base_branch: str
    head_branch: str
    files: list[ChangedFile]



class AIReviewResponse(BaseModel):
    title: str
    author: str
    review_count: int
    duration_seconds: float
    reviews: list[FileReview]
    report_path: Optional[str] = None