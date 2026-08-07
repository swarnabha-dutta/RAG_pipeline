from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseModel):
    OPENROUTER_API_KEY: str
    QDRANT_URL: str
    QDRANT_API_KEY: str
    COLLECTION_NAME: str
    EMBEDDING_MODEL: str
    OPENROUTER_BASE_URL: str
    OPENROUTER_MODEL: str

settings = Settings(
    OPENROUTER_API_KEY=os.getenv("OPENROUTER_API_KEY"),
    QDRANT_URL=os.getenv("QDRANT_URL"),
    QDRANT_API_KEY=os.getenv("QDRANT_API_KEY"),
    COLLECTION_NAME=os.getenv("COLLECTION_NAME"),
    EMBEDDING_MODEL=os.getenv("EMBEDDING_MODEL"),
    OPENROUTER_BASE_URL=os.getenv("OPENROUTER_BASE_URL"),
    OPENROUTER_MODEL=os.getenv("OPENROUTER_MODEL"),
)