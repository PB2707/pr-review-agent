from pathlib import Path


class PromptService:

    def load_prompt(self, filename: str) -> str:

        prompt_path = (
            Path(__file__).parent.parent
            / "prompts"
            / filename
        )

        return prompt_path.read_text()