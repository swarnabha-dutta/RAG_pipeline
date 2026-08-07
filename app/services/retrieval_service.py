from app.core.logger import setup_logger
from app.services.embedding_service import EmbeddingService
from app.database.qdrant_client import QdrantService

logger = setup_logger()


class RetrievalService:
    """
    Production Retrieval Service

    Responsibilities
    ----------------
    - Generate embedding for user question
    - Perform semantic search in Qdrant
    - Return relevant chunks
    """

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.qdrant_service = QdrantService()

    def retrieve(
        self,
        question: str,
        limit: int = 5,
    ) -> list[dict]:
        """
        Retrieve relevant document chunks.

        Parameters
        ----------
        question : str
            User question

        limit : int
            Number of chunks to retrieve

        Returns
        -------
        list[dict]
        """

        logger.info(
            f"Retrieving context for question: {question}"
        )

        # Generate query embedding
        query_embedding = (
            self.embedding_service.generate_embedding(
                question
            )
        )

        # Perform semantic search
        results = self.qdrant_service.search(
            query_vector=query_embedding,
            limit=limit,
        )

        retrieved_chunks = []

        for result in results:

            retrieved_chunks.append(
                {
                    "score": result.score,
                    "document": result.payload.get("document"),
                    "page": result.payload.get("page"),
                    "text": result.payload.get("text"),
                }
            )

        logger.info(
            f"Retrieved {len(retrieved_chunks)} relevant chunks."
        )

        return retrieved_chunks