from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config.settings import settings
from app.core.logger import setup_logger

logger = setup_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("========== Starting Production RAG API ==========")
    logger.info(f"Collection Name : {settings.COLLECTION_NAME}")
    logger.info(f"Embedding Model : {settings.EMBEDDING_MODEL}")
    logger.info("RAG API Started Successfully")

    yield

    logger.info("========== Shutting Down RAG API ==========")


app = FastAPI(
    title="Production RAG API",
    version="1.0.0",
    description="Production Ready RAG System",
    lifespan=lifespan,
)


@app.get("/", tags=["Root"])
async def home():
    logger.info("Home endpoint called")

    return {
        "success": True,
        "message": "Production RAG API Running 🚀",
        "version": "1.0.0",
    }


@app.get("/health", tags=["Health"])
async def health():
    logger.info("Health endpoint called")

    return {
        "success": True,
        "status": "healthy",
    }