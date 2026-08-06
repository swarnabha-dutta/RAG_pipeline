from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import RAGException
from app.core.logger import setup_logger

logger = setup_logger()


async def rag_exception_handler(
    request: Request,
    exc: RAGException,
):
    logger.error(
        f"RAG Exception : {exc.message}"
    )

    return JSONResponse(
        status_code=400,
        content={
            "success": False,
            "message": exc.message,
            "data": None,
        },
    )