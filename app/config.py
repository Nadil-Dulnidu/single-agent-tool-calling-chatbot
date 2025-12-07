import os

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()
class Settings(BaseModel):
    """Loads settings from environment variables."""

    OPENAI_API_KEY: str = ""
    OPENAI_MODEL_NAME: str = "gpt-4o-mini"
    LANGCHAIN_API_KEY: str = ""
    SERPAPI_API_KEY: str = ""


settings = Settings(
    OPENAI_API_KEY=os.getenv("OPENAI_API_KEY") or "",
    OPENAI_MODEL_NAME=os.getenv("OPENAI_MODEL_NAME", "gpt-4o-mini"),
    LANGCHAIN_API_KEY=os.getenv("LANGCHAIN_API_KEY") or "",
    SERPAPI_API_KEY=os.getenv("SERPAPI_API_KEY") or "",
)

# Fail fast if essential keys are missing
if not settings.OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable not set.")

if not settings.SERPAPI_API_KEY:
    raise ValueError("SERPAPI_API_KEY environment variable not set.")

if not settings.LANGCHAIN_API_KEY:
    raise ValueError("LANGCHAIN_API_KEY environment variable not set.")