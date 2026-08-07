from fastapi import Request, HTTPException
from fastapi.exceptions import RequestValidationError
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


async def http_exception_handler(
    request: Request,
    exc: HTTPException,
):
    logger.error(
        f"HTTP Exception : {exc.detail}"
    )

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.detail,
            "data": None,
        },
    )


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
):
    logger.error(
        f"Validation Error : {exc.errors()}"
    )

    errors = []

    for error in exc.errors():
        errors.append(
            {
                "field": ".".join(map(str, error["loc"])),
                "message": error["msg"],
            }
        )

    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "message": "Validation Error",
            "data": errors,
        },
    )


async def generic_exception_handler(
    request: Request,
    exc: Exception,
):
    logger.exception(
        f"Unhandled Exception : {str(exc)}"
    )

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Internal Server Error",
            "data": None,
        },
    )