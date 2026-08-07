from app.services.ingestion_service import IngestionService

service = IngestionService()

result = service.ingest_document(
    "data/pdfs/02_Maneka_Gandhi_vs_Union_of_India_p0683-p0794.pdf"
)

print(result)