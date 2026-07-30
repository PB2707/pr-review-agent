from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    APP_NAME = "PR Review Agent"
    APP_VERSION = "1.0.0"

    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5-coder:7b")


settings = Settings()