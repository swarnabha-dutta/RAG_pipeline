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

from app.models.response import APIResponse
from app.models.query import QueryRequest
from app.models.ingestion import IngestionRequest

from app.services.ingestion_service import IngestionService
from app.services.rag_service import RAGService

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

# Register Exception Handlers

app.add_exception_handler(
    RAGException,
    rag_exception_handler,
)

app.add_exception_handler(
    HTTPException,
    http_exception_handler,
)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler,
)

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


@app.post(
    "/ingest",
    tags=["Ingestion"],
    response_model=APIResponse,
)
async def ingest_document(
    request: IngestionRequest,
):
    """
    Ingest a PDF document into the vector database.
    """

    logger.info(
        f"Received ingestion request : {request.pdf_path}"
    )

    service = IngestionService()

    result = service.ingest_document(
        request.pdf_path
    )

    return APIResponse(
        success=True,
        message="Document ingested successfully.",
        data=result,
    )


@app.post(
    "/query",
    tags=["RAG"],
    response_model=APIResponse,
)
async def ask_question(
    request: QueryRequest,
):
    """
    Ask a question using the RAG pipeline.
    """

    logger.info(
        f"Received question : {request.question}"
    )

    rag_service = RAGService()

    result = await rag_service.answer_question(
        request.question
    )

    return APIResponse(
        success=True,
        message="Answer generated successfully.",
        data=result,
    )