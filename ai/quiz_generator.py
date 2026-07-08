from ai.llm import get_llm


class QuizGenerator:

    def __init__(self):
        self.llm = get_llm()


    def generate_quiz(self, text, difficulty, quiz_type):

        prompt = f"""
You are an AI Educational Assistant.

Study the following text carefully.

Generate a {difficulty} level quiz.
Quiz Type:
{quiz_type}

Rules:

If quiz type is MCQ:
- Generate 5 multiple choice questions
- Four options (A, B, C, D)
- Mention the correct answer

If quiz type is True/False:
- Generate 5 statements
- Mention True or False

If quiz type is Fill in the Blanks:
- Generate 5 fill in the blanks
- Mention the correct answer

Study Material:

{text}
"""
        response = self.llm.invoke(prompt)

        return response.content