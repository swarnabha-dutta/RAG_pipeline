from app.ingestion.pdf_parser import PDFParser
from app.ingestion.text_chunker import TextChunker

parser = PDFParser(
    "data/pdfs/AI Python Engineering Assignment.pdf"
)

pages = parser.extract_pages()

chunker = TextChunker(
    chunk_size=500,
    chunk_overlap=100,
)

chunks = chunker.chunk_pages(
    pages,
    "AI Python Engineering Assignment.pdf",
)

print("=" * 50)
print(f"Total Chunks : {len(chunks)}")
print("=" * 50)

for chunk in chunks[:3]:
    print(chunk)
    print("-" * 80)