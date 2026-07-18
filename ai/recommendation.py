from ai.llm import get_llm


class RecommendationGenerator:

    def __init__(self):
        self.llm = get_llm()

    def generate_recommendation(
        self,
        subject,
        quizzes_completed,
        flashcards_reviewed,
        study_hours
    ):

        prompt = f"""
You are an AI Study Coach.

Student Information

Subject:
{subject}

Quizzes Completed:
{quizzes_completed}

Flashcards Reviewed:
{flashcards_reviewed}

Study Hours Per Week:
{study_hours}

Generate:

1. Strengths
2. Weaknesses
3. Study Recommendations
4. Weekly Goals
5. Motivational Tip

Keep the response clear and encouraging.
"""

        response = self.llm.invoke(prompt)

        return response.content