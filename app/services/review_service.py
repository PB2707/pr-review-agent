from app.services.github_service import GitHubService
from app.services.llm_service import LLMService
from app.services.prompt_service import PromptService
from pathlib import Path
import time
SUPPORTED_EXTENSIONS = {
    ".py",
    ".java",
    ".js",
    ".ts",
    ".go",
    ".cpp",
    ".c",
    ".cs",
    ".sql",
    ".yaml",
    ".yml",
    ".json",
    ".xml",
    ".md",
}

class ReviewService:

    def __init__(self):
        self.github = GitHubService()
        self.llm = LLMService()
        self.prompts = PromptService()

    def review_pull_request(self, pr_url: str):

        start_time = time.time()

        pr = self.github.get_pr_details(pr_url)

        reviews = []

        base_prompt = self.prompts.load_reviewer_prompt()

        for file in pr.files:

            extension = Path(file.filename).suffix

            if extension and extension not in SUPPORTED_EXTENSIONS:
                print(f"Skipping {file.filename}")
                continue

            if not file.patch:
                print(f"Skipping {file.filename} (no patch)")
                continue

            prompt = f"""
    {base_prompt}

    Repository Pull Request Review

    Filename:
    {file.filename}

    Status:
    {file.status}

    Additions:
    {file.additions}

    Deletions:
    {file.deletions}

    Diff:

    {file.patch}
    """

            print(f"Reviewing {file.filename}...")

            try:
                ai_review = self.llm.chat(prompt)
            except Exception as e:
                ai_review = f"Error generating review: {str(e)}"

            print("✓ Review complete")

            reviews.append({
                "filename": file.filename,
                "review": ai_review
            })

        end_time = time.time()

        print(f"Review completed in {end_time - start_time:.2f} seconds")

        return {
    "title": pr.title,
    "author": pr.author,
    "review_count": len(reviews),
    "duration_seconds": round(end_time - start_time, 2),
    "reviews": reviews,
}