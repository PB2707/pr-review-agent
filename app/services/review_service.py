from app.services.github_service import GitHubService
from app.services.llm_service import LLMService
from app.services.prompt_service import PromptService
import time


AGENTS = [
    ("Security", "security_prompt.txt"),
    ("Performance", "performance_prompt.txt"),
    ("Readability", "readability_prompt.txt"),
]


class ReviewService:

    def __init__(self):
        self.github = GitHubService()
        self.llm = LLMService()
        self.prompts = PromptService()

    def review_pull_request(self, pr_url: str):

        start_time = time.time()

        pr = self.github.get_pr_details(pr_url)

        reviews = []

        for file in pr.files:

            if not file.patch:
                print(f"Skipping {file.filename} (no patch)")
                continue

            agent_reviews = []

            # Run each specialist agent
            for agent_name, prompt_file in AGENTS:

                base_prompt = self.prompts.load_prompt(prompt_file)

                prompt = f"""
{base_prompt}

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

                print(f"Running {agent_name} Agent on {file.filename}...")

                review = self.llm.chat(prompt)

                agent_reviews.append(
                    {
                        "agent": agent_name,
                        "review": review,
                    }
                )

            # Combine all agent reviews
            combined_reviews = ""

            for review in agent_reviews:
                combined_reviews += (
                    f"{review['agent']} Review:\n"
                    f"{review['review']}\n\n"
                )

            # Run Summary Agent
            summary_prompt = self.prompts.load_prompt("summary_prompt.txt")

            summary_input = f"""
{summary_prompt}

Below are the reviews from multiple AI reviewers.

{combined_reviews}
"""

            print(f"Running Summary Agent on {file.filename}...")

            summary = self.llm.chat(summary_input)

            # Store the complete review for this file
            reviews.append(
                {
                    "filename": file.filename,
                    "summary": summary,
                    "reviews": agent_reviews,
                }
            )

        end_time = time.time()

        result = {
    "title": pr.title,
    "author": pr.author,
    "review_count": len(reviews),
    "duration_seconds": round(end_time - start_time, 2),
    "reviews": reviews,
}

        print("\n========== FINAL RESPONSE ==========")
        print(result)
        print("===================================\n")

        return result