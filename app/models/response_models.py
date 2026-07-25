from pydantic import BaseModel
from typing import List, Optional


class ChangedFile(BaseModel):
    filename: str
    status: str
    additions: int
    deletions: int
    changes: int
    patch: Optional[str] = None


class ReviewResponse(BaseModel):
    title: str
    author: str
    base_branch: str
    head_branch: str
    files: List[ChangedFile]