from pydantic import BaseModel


class Citation(BaseModel):
    document: str
    page: int
    text: str


class RAGResponse(BaseModel):
    answer: str
    citations: list[Citation]