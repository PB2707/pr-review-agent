from app.services.github_service import GitHubService
from app.services.llm_service import LLMService
from app.services.prompt_service import PromptService
import time
from concurrent.futures import ThreadPoolExecutor
from app.services.report_service import ReportService

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
        self.report_service = ReportService()

    def run_agent(
    self,
    agent_name: str,
    prompt_file: str,
    file,
):
        """
        Executes a single review agent.
        """

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

        return {
            "agent": agent_name,
            "review": review,
        }

    def review_pull_request(self, pr_url: str):

        start_time = time.time()
        print(AGENTS)

        pr = self.github.get_pr_details(pr_url)

        reviews = []

        for file in pr.files:

            if not file.patch:
                print(f"Skipping {file.filename} (no patch)")
                continue

            

            # Run each specialist agent
            with ThreadPoolExecutor(max_workers=len(AGENTS)) as executor:

                futures = []

                for agent_name, prompt_file in AGENTS:

                    future = executor.submit(
                        self.run_agent,
                        agent_name,
                        prompt_file,
                        file,
                    )

                    futures.append(future)
                agent_reviews = []

                for future in futures:
                    agent_reviews.append(future.result())



    

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
            risk = self.calculate_risk(agent_reviews)
            # Store the complete review for this file
            reviews.append(
                {
                    "filename": file.filename,
                    "summary": summary,
                    "reviews": agent_reviews,
                    "risk": risk,
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

        report_path = self.report_service.generate_markdown(result)

        print(f"Markdown report saved to: {report_path}")


        return result
    
    def calculate_risk(self, agent_reviews):
        """
        Calculates an overall risk score from agent reviews.
        """

        text = " ".join(
            review["review"].lower()
            for review in agent_reviews
        )

        score = 1

        if "critical" in text:
            score = 5
        elif "high" in text:
            score = 4
        elif "medium" in text:
            score = 3
        elif "low" in text:
            score = 2

        levels = {
            1: "Low",
            2: "Low",
            3: "Medium",
            4: "High",
            5: "Critical",
        }

        return {
            "score": score,
            "level": levels[score],
        }