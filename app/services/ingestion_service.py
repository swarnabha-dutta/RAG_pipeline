from pathlib import Path

from app.core.logger import setup_logger
from app.services.embedding_service import EmbeddingService
from app.database.qdrant_client import QdrantService
from app.ingestion.pdf_parser import PDFParser
from app.ingestion.text_chunker import TextChunker

logger = setup_logger()


class IngestionService:
    """
    Production Ingestion Service

    Responsibilities
    ----------------
    - Parse PDF
    - Chunk Text
    - Generate Embeddings
    - Store Vectors in Qdrant
    """

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.qdrant_service = QdrantService()
        self.text_chunker = TextChunker()

    def ingest_document(self, pdf_path: str) -> dict:
        """
        Complete document ingestion pipeline.

        Parameters
        ----------
        pdf_path : str

        Returns
        -------
        dict
        """

        logger.info(f"Starting ingestion : {pdf_path}")

        parser = PDFParser(pdf_path)

        # Extract metadata
        metadata = parser.extract_metadata()

        # Extract page-wise text
        pages = parser.extract_pages()

        logger.info(f"Extracted {len(pages)} pages.")

        # Chunk document
        chunks = self.text_chunker.chunk_pages(
            pages=pages,
            document_name=metadata["filename"],
        )

        logger.info(f"Generated {len(chunks)} chunks.")

        if not chunks:
            logger.warning("No chunks generated.")

            return {
                "document": metadata["filename"],
                "pages": metadata["pages"],
                "chunks": 0,
                "vectors": 0,
            }

        # Batch embedding generation
        texts = [
            chunk["text"]
            for chunk in chunks
        ]

        embeddings = self.embedding_service.generate_embeddings(
            texts
        )

        # Attach embeddings
        for chunk, embedding in zip(
            chunks,
            embeddings,
        ):
            chunk["embedding"] = embedding

        logger.info("Embeddings generated successfully.")

        # Create collection if required
        self.qdrant_service.create_collection()

        # Store vectors
        self.qdrant_service.upsert_documents(
            chunks
        )

        vector_count = self.qdrant_service.count_points()

        logger.info(
            f"Ingestion completed successfully for {metadata['filename']}"
        )

        return {
            "document": metadata["filename"],
            "pages": metadata["pages"],
            "chunks": len(chunks),
            "vectors": vector_count,
        }