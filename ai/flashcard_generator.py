from ai.llm import get_llm


class FlashcardGenerator:

    def __init__(self):
        self.llm = get_llm()

    def generate_flashcards(self, text):
        prompt = f"""
You are an educational AI assistant.

Read the study material and generate exactly 10 flashcards.

Return ONLY valid JSON.

Format:

[
  {{
    "question": "What is Software Engineering?",
    "answer": "Software Engineering is the application of engineering principles to the design, development, and maintenance of software."
  }},
  {{
    "question": "...",
    "answer": "..."
  }}
]

Study Material:

{text}
"""

        response = self.llm.invoke(prompt)

        return response.content