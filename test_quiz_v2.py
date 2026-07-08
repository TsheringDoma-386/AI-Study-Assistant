from processings.pdf_reader import PDFReader
from processings.text_cleaner import TextCleaner
from processings.chunker import Chunker

from ai.quiz_generator import QuizGenerator


reader = PDFReader()
cleaner = TextCleaner()
chunker = Chunker()

quiz = QuizGenerator()


text = reader.extract_text("upload/software engineering.pdf")

clean_text = cleaner.clean(text)

chunks = chunker.split(clean_text)

result = quiz.generate_quiz(
    text=chunks[0],
    difficulty="Easy",
    quiz_type="MCQ"
)

print(result)