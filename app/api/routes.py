from fastapi import APIRouter, HTTPException

from app.models.request_models import ReviewRequest
from app.models.review_models import AIReviewResponse
from app.services.github_service import GitHubService

router = APIRouter()

from app.services.review_service import ReviewService

review_service = ReviewService()


@router.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "PR Review Agent"
    }


@router.post("/review", response_model=AIReviewResponse)
def review_pull_request(request: ReviewRequest):
    try:
        return review_service.review_pull_request(
    str(request.pr_url)
)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))