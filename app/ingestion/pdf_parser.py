from pathlib import Path

import fitz  # PyMuPDF

from app.core.exceptions import DocumentNotFoundException
from app.core.logger import setup_logger
from app.utils.text_cleaner import TextCleaner

logger = setup_logger()


class PDFParser:
    """
    Production Grade PDF Parser

    Responsibilities
    ----------------
    - Validate PDF
    - Extract page-wise text
    - Extract complete text
    - Extract metadata
    """

    def __init__(self, pdf_path: str):
        self.pdf_path = Path(pdf_path)

    def validate_pdf(self) -> None:
        """
        Validate the PDF before processing.
        """

        logger.info(f"Validating PDF : {self.pdf_path}")

        if not self.pdf_path.exists():
            raise DocumentNotFoundException(
                f"PDF not found : {self.pdf_path}"
            )

        if self.pdf_path.suffix.lower() != ".pdf":
            raise DocumentNotFoundException(
                "Only PDF files are supported."
            )

        logger.info("PDF validation successful.")

    def extract_pages(self) -> list[dict]:
        """
        Extract text page by page.

        Returns:
            [
                {
                    "page": 1,
                    "text": "...",
                },
                ...
            ]
        """

        self.validate_pdf()

        logger.info(f"Opening PDF : {self.pdf_path.name}")

        pages = []

        try:

            with fitz.open(self.pdf_path) as pdf:

                for page_number, page in enumerate(pdf, start=1):

                    # Extract raw text
                    text = page.get_text("text")

                    # Clean extracted text
                    text = TextCleaner.clean(text)

                    if not text:
                        continue

                    pages.append(
                        {
                            "page": page_number,
                            "text": text,
                        }
                    )

            logger.info(
                f"Extracted {len(pages)} pages from {self.pdf_path.name}"
            )

            return pages

        except Exception:
            logger.exception("Failed to extract PDF.")
            raise

    def extract_text(self) -> str:
        """
        Extract full document text.
        """

        pages = self.extract_pages()

        return "\n\n".join(
            page["text"]
            for page in pages
        )

    def extract_metadata(self) -> dict:
        """
        Extract PDF metadata.
        """

        self.validate_pdf()

        try:

            with fitz.open(self.pdf_path) as pdf:

                metadata = pdf.metadata

                return {
                    "filename": self.pdf_path.name,
                    "pages": len(pdf),
                    "title": metadata.get("title"),
                    "author": metadata.get("author"),
                    "subject": metadata.get("subject"),
                    "creator": metadata.get("creator"),
                    "producer": metadata.get("producer"),
                }

        except Exception:
            logger.exception("Metadata extraction failed.")
            raise