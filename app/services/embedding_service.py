from sentence_transformers import SentenceTransformer

from app.config.settings import settings
from app.core.exceptions import EmbeddingException
from app.core.logger import setup_logger

logger = setup_logger()


class EmbeddingService:
    """
    Production Embedding Service
    """

    def __init__(self):
        try:
            logger.info(
                f"Loading embedding model: {settings.EMBEDDING_MODEL}"
            )

            self.model = SentenceTransformer(
                settings.EMBEDDING_MODEL
            )

            logger.info("Embedding model loaded successfully.")

        except Exception as e:
            logger.exception("Failed to load embedding model.")
            raise EmbeddingException(str(e))

    def generate_embedding(self, text: str) -> list[float]:
        """
        Generate embedding for a single text.
        """

        try:
            embedding = self.model.encode(
                text,
                normalize_embeddings=True,
            )

            return embedding.tolist()

        except Exception as e:
            logger.exception("Embedding generation failed.")
            raise EmbeddingException(str(e))

    def generate_embeddings(
        self,
        texts: list[str],
    ) -> list[list[float]]:
        """
        Generate embeddings for multiple texts.
        """

        try:
            embeddings = self.model.encode(
                texts,
                normalize_embeddings=True,
            )

            return embeddings.tolist()

        except Exception as e:
            logger.exception("Batch embedding generation failed.")
            raise EmbeddingException(str(e))