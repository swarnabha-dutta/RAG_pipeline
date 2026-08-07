from app.database.qdrant_client import QdrantService

qdrant = QdrantService()

print("=" * 50)

print("Health Check:")
print(qdrant.health_check())

print("=" * 50)

print("Creating Collection...")
qdrant.create_collection()

print("=" * 50)

print("Collection Exists:")
print(qdrant.collection_exists())

print("=" * 50)