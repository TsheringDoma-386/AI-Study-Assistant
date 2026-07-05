from pathlib import Path

from processings.pdf_reader import PDFReader
from processings.text_cleaner import TextCleaner
from processings.chunker import Chunker

from ai.flashcard_generator import FlashcardGenerator


reader = PDFReader()
cleaner = TextCleaner()
chunker = Chunker()
flashcard_generator = FlashcardGenerator()

pdf_path = Path("upload/software engineering.pdf")
if not pdf_path.exists():
    pdf_path = Path("uploads/software engineering.pdf")

text = reader.extract_text(str(pdf_path))
clean_text = cleaner.clean(text)
chunks = chunker.split(clean_text)

flashcards = flashcard_generator.generate_flashcards(chunks[0])

print(flashcards)