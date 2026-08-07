from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError

from app.config.settings import settings
from app.core.exceptions import RAGException
from app.core.handlers import (
    rag_exception_handler,
    http_exception_handler,
    validation_exception_handler,
    generic_exception_handler,
)
from app.core.logger import setup_logger
from app.models.query import QueryRequest
from app.models.response import APIResponse

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

# Register Custom Exception Handler
app.add_exception_handler(
    RAGException,
    rag_exception_handler,
)

# Register HTTP Exception Handler
app.add_exception_handler(
    HTTPException,
    http_exception_handler,
)

# Register Validation Exception Handler
app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler,
)

# Register Generic Exception Handler
app.add_exception_handler(
    Exception,
    generic_exception_handler,
)


@app.get(
    "/",
    tags=["Root"],
    response_model=APIResponse,
)
async def home():
    logger.info("Home endpoint called")

    return APIResponse(
        success=True,
        message="Production RAG API Running 🚀",
        data={
            "version": "1.0.0",
        },
    )


@app.get(
    "/health",
    tags=["Health"],
    response_model=APIResponse,
)
async def health():
    logger.info("Health endpoint called")

    return APIResponse(
        success=True,
        message="Application Healthy",
        data={
            "status": "healthy",
        },
    )
