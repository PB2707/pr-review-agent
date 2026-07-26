from pydantic import BaseModel


class FileReview(BaseModel):
    filename: str
    review: str


class AIReviewResponse(BaseModel):
    title: str
    author: str
    reviews: list[FileReview]