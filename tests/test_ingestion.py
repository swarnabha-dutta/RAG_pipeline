from app.services.ingestion_service import IngestionService

service = IngestionService()

result = service.ingest_document(
    "data/pdfs/AI Python Engineering Assignment.pdf"
)

print(result)