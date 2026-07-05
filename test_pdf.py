from pathlib import Path

from processings.pdf_reader import PDFReader

reader = PDFReader()

pdf_path = Path("upload/software engineering.pdf")
if not pdf_path.exists():
    pdf_path = Path("uploads/software engineering.pdf")

text = reader.extract_text(str(pdf_path))

print(text[:3000])
