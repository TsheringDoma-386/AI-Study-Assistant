from ai.llm import get_llm


class FlashcardGenerator:

    def __init__(self):
        self.llm = get_llm()

    def generate_flashcards(self, text):

        prompt = f"""
You are an educational AI assistant.

Read the following study material.

Generate 10 flashcards.

Rules:

1. Each flashcard should have:

Front:
<Question>

Back:
<Answer>

2. Keep answers concise.
3. Use only information from the text.

Study Material:

{text}
"""

        response = self.llm.invoke(prompt)

        return response.content