from pydantic import BaseModel, Field


class IngestionRequest(BaseModel):
    pdf_path: str = Field(
        ...,
        min_length=1,
        description="Path to the PDF document",
        examples=[
            "data/pdfs/AI Python Engineering Assignment.pdf"
        ],
    )