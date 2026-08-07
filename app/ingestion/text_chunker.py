from app.core.logger import setup_logger

logger = setup_logger()


class TextChunker:
    """
    Production Grade Text Chunker

    Responsibilities
    ----------------
    - Split long text into chunks
    - Preserve overlap
    - Keep page metadata
    """

    def __init__(
        self,
        chunk_size: int = 500,
        chunk_overlap: int = 100,
    ):

        if chunk_overlap >= chunk_size:
            raise ValueError(
                "chunk_overlap must be smaller than chunk_size"
            )

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk_pages(
        self,
        pages: list[dict],
        document_name: str,
    ) -> list[dict]:
        """
        Convert page-wise text into chunks.

        Returns
        -------
        [
            {
                "id": 0,
                "document": "...",
                "page": 1,
                "text": "...",
            }
        ]
        """

        logger.info("Starting text chunking.")

        chunks = []
        chunk_id = 0

        for page in pages:

            text = page["text"]
            page_number = page["page"]

            start = 0

            while start < len(text):

                end = start + self.chunk_size

                chunk = text[start:end].strip()

                if chunk:

                    chunks.append(
                        {
                            "id": chunk_id,
                            "document": document_name,
                            "page": page_number,
                            "text": chunk,
                        }
                    )

                    chunk_id += 1

                start += (
                    self.chunk_size
                    - self.chunk_overlap
                )

        logger.info(
            f"Generated {len(chunks)} chunks."
        )

        return chunks