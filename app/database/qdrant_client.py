from qdrant_client import QdrantClient
from qdrant_client.http.models import (
    Distance,
    VectorParams,
    PointStruct,
)

from app.config.settings import settings
from app.core.exceptions import QdrantException
from app.core.logger import setup_logger

logger = setup_logger()


class QdrantService:
    """
    Production Qdrant Service
    """

    def __init__(self):
        try:
            self.client = QdrantClient(
                url=settings.QDRANT_URL,
                api_key=settings.QDRANT_API_KEY or None,
            )

            self.collection = settings.COLLECTION_NAME

            logger.info("Connected to Qdrant successfully.")

        except Exception as e:
            logger.exception("Failed to connect to Qdrant.")

            raise QdrantException(str(e))

    def collection_exists(self) -> bool:
        """
        Check whether the collection already exists.
        """
        try:
            collections = self.client.get_collections()

            return any(
                collection.name == self.collection
                for collection in collections.collections
            )

        except Exception as e:
            logger.exception("Failed to check collection.")

            raise QdrantException(str(e))

    def create_collection(self):
        """
        Create collection if it doesn't already exist.
        """
        try:
            if self.collection_exists():
                logger.info(
                    f"Collection '{self.collection}' already exists."
                )
                return

            self.client.create_collection(
                collection_name=self.collection,
                vectors_config=VectorParams(
                    size=384,
                    distance=Distance.COSINE,
                ),
            )

            logger.info(
                f"Collection '{self.collection}' created successfully."
            )

        except Exception as e:
            logger.exception("Failed to create collection.")

            raise QdrantException(str(e))

    def health_check(self) -> bool:
        """
        Check whether Qdrant server is reachable.
        """
        try:
            self.client.get_collections()

            logger.info("Qdrant health check passed.")

            return True

        except Exception as e:
            logger.exception("Qdrant health check failed.")

            raise QdrantException(str(e))