import re

from github import Github

from app.core.config import settings
from github.PullRequest import PullRequest
from app.models.response_models import ChangedFile, PullRequestDetails


class GitHubService:
    def __init__(self):
        self.client = Github(settings.GITHUB_TOKEN)

    def parse_pr_url(self, pr_url: str):
        """
        Extract owner, repository and PR number from a GitHub PR URL.

        Example:
        https://github.com/octocat/Hello-World/pull/1347

        Returns:
        ("octocat", "Hello-World", 1347)
        """

        pattern = r"github\.com/([^/]+)/([^/]+)/pull/(\d+)"

        match = re.search(pattern, pr_url)

        if not match:
            raise ValueError("Invalid GitHub Pull Request URL.")

        owner, repo, pr_number = match.groups()

        return owner, repo, int(pr_number)
    
  



    
    def get_pull_request(self, pr_url: str) -> PullRequest:
        """
        Fetch a GitHub Pull Request object.
        """

        owner, repo, pr_number = self.parse_pr_url(pr_url)

        repository = self.client.get_repo(f"{owner}/{repo}")

        pull_request = repository.get_pull(pr_number)

        return pull_request
    
    def get_pr_details(self, pr_url: str) -> PullRequestDetails:
        """
        Fetch PR details and convert them to our response model.
        """

        pr = self.get_pull_request(pr_url)

        changed_files = []

        for file in pr.get_files():
            changed_files.append(
                ChangedFile(
                    filename=file.filename,
                    status=file.status,
                    additions=file.additions,
                    deletions=file.deletions,
                    changes=file.changes,
                    patch=file.patch,
                )
            )

        return PullRequestDetails(
            title=pr.title,
            author=pr.user.login,
            base_branch=pr.base.ref,
            head_branch=pr.head.ref,
            files=changed_files,
        )