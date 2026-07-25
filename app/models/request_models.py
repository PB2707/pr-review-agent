from pydantic import BaseModel, HttpUrl


class ReviewRequest(BaseModel):
    pr_url: HttpUrl