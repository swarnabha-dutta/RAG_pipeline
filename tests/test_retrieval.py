from app.services.retrieval_service import RetrievalService

service = RetrievalService()

results = service.retrieve(
    "What is the objective of this assignment?"
)

for chunk in results:
    print(chunk)