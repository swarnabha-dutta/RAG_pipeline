from pydantic import BaseModel


class IngestionResponse(BaseModel):
    document: str
    pages: int
    chunks: int
    vectors: int