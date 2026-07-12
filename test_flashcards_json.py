from processings.pdf_reader import PDFReader
from processings.text_cleaner import TextCleaner
from processings.chunker import Chunker

from ai.flashcard_generator import FlashcardGenerator
from utils.json_parser import parse_flashcards

reader = PDFReader()
cleaner = TextCleaner()
chunker = Chunker()
generator = FlashcardGenerator()

text = reader.extract_text("upload/software engineering.pdf")
clean_text = cleaner.clean(text)
chunks = chunker.split(clean_text)

response = generator.generate_flashcards(chunks[0])

flashcards = parse_flashcards(response)

for card in flashcards:
    print(card["question"])
    print(card["answer"])
    print("-" * 40)