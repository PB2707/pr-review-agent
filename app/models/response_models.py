from pydantic import BaseModel
from typing import List, Optional

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



from pydantic import BaseModel
from typing import Optional


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