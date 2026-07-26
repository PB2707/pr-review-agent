from pathlib import Path


class PromptService:

    def load_reviewer_prompt(self):

        prompt_path = (
            Path(__file__)
            .parent.parent
            / "prompts"
            / "reviewer_prompt.txt"
        )

        return prompt_path.read_text()