from qdrant_client import QdrantClient
from qdrant_client.http.models import (
    Distance,
    PointStruct,
    VectorParams,
)

from app.config.settings import settings
from app.core.exceptions import QdrantException
from app.core.logger import setup_logger

logger = setup_logger()


class QdrantService:
    """
    Production Qdrant Service

    Responsibilities
    ----------------
    - Connect to Qdrant
    - Health Check
    - Create Collection
    - Upsert Vectors
    - Semantic Search
    - Count Stored Vectors
    - Delete Collection
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
        Check whether collection exists.
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
        Create collection if it doesn't exist.
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

    def upsert_documents(
        self,
        documents: list[dict],
    ):
        """
        Store vectors inside Qdrant.
        """

        try:

            points = []

            for doc in documents:

                points.append(
                    PointStruct(
                        id=doc["id"],
                        vector=doc["embedding"],
                        payload={
                            "document": doc["document"],
                            "page": doc["page"],
                            "text": doc["text"],
                        },
                    )
                )

            self.client.upsert(
                collection_name=self.collection,
                points=points,
            )

            logger.info(
                f"Successfully inserted {len(points)} vectors."
            )

        except Exception as e:

            logger.exception("Vector insertion failed.")

            raise QdrantException(str(e))

    def search(
        self,
        query_vector: list[float],
        limit: int = 5,
    ):
        """
        Semantic vector search.
        """

        try:

            response = self.client.query_points(
                collection_name=self.collection,
                query=query_vector,
                limit=limit,
            )

            results = response.points

            logger.info(
                f"Retrieved {len(results)} matching chunks."
            )

            return results

        except Exception as e:

            logger.exception("Semantic search failed.")

            raise QdrantException(str(e))

    def count_points(self) -> int:
        """
        Count stored vectors.
        """

        try:

            result = self.client.count(
                collection_name=self.collection,
                exact=True,
            )

            logger.info(
                f"Collection contains {result.count} vectors."
            )

            return result.count

        except Exception as e:

            logger.exception("Count operation failed.")

            raise QdrantException(str(e))

    def delete_collection(self):
        """
        Delete collection.
        """

        try:

            if not self.collection_exists():

                logger.info(
                    f"Collection '{self.collection}' does not exist."
                )

                return

            self.client.delete_collection(
                collection_name=self.collection,
            )

            logger.info(
                f"Collection '{self.collection}' deleted successfully."
            )

        except Exception as e:

            logger.exception("Failed to delete collection.")

            raise QdrantException(str(e))