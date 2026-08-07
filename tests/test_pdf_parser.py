from app.ingestion.pdf_parser import PDFParser

parser = PDFParser(
    "data/pdfs/AI Python Engineering Assignment.pdf"
)

print("=" * 50)
print("Metadata")
print(parser.extract_metadata())

print("=" * 50)
print("Pages")
print(parser.extract_pages())

print("=" * 50)
print("Full Text")
print(parser.extract_text())