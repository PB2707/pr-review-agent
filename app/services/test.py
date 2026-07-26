from app.services.llm_service import LLMService

llm = LLMService()

response = llm.chat(
    "Say hello in one sentence."
)

print(response)

from app.services.prompt_service import PromptService

prompt = PromptService()

print(prompt.load_reviewer_prompt())