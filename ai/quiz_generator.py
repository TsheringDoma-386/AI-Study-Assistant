from ai.llm import get_llm


class QuizGenerator:

    def __init__(self):
        self.llm = get_llm()

    def generate_quiz(self, text):

        prompt = f"""
You are an educational AI assistant.

Read the following study material carefully.

Generate:

1. Five Multiple Choice Questions (MCQs)
   - Each question should have four options (A, B, C, D)
   - Mention the correct answer.

2. Three True/False Questions
   - Mention whether the answer is True or False.

3. Two Short Answer Questions
   - Provide a brief answer.

Study Material:

{text}
"""

        response = self.llm.invoke(prompt)

        return response.content