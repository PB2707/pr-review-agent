from fastapi import APIRouter, HTTPException

from app.models.request_models import ReviewRequest
from app.models.response_models import ReviewResponse
from app.services.github_service import GitHubService

router = APIRouter()

github_service = GitHubService()


@router.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "PR Review Agent"
    }


@router.post("/review", response_model=ReviewResponse)
def review_pull_request(request: ReviewRequest):
    try:
        return github_service.get_pr_details(str(request.pr_url))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))