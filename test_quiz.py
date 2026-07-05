from pathlib import Path

from processings.pdf_reader import PDFReader
from processings.text_cleaner import TextCleaner
from processings.chunker import Chunker

from ai.quiz_generator import QuizGenerator


reader = PDFReader()
cleaner = TextCleaner()
chunker = Chunker()
quiz = QuizGenerator()


pdf_path = Path("upload/software engineering.pdf")
if not pdf_path.exists():
    pdf_path = Path("uploads/software engineering.pdf")

text = reader.extract_text(str(pdf_path))

clean_text = cleaner.clean(text)

chunks = chunker.split(clean_text)

quiz_text = chunks[0]

questions = quiz.generate_quiz(quiz_text)

print(questions)