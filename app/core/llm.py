
from langchain_openai import ChatOpenAI
from app.config import settings

OPENAI_API_KEY = settings.OPENAI_API_KEY
OPENAI_MODEL_NAME = settings.OPENAI_MODEL_NAME

llm = ChatOpenAI(
    model=OPENAI_MODEL_NAME,
    temperature=0.0,
    streaming=True,
    api_key=OPENAI_API_KEY
)