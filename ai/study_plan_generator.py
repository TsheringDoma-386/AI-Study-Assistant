from ai.llm import get_llm


class StudyPlanGenerator:

    def __init__(self):
        self.llm = get_llm()

    def generate_plan(self, subject, exam_date, hours_per_day, difficulty):

        prompt = f"""
You are an AI Study Planner.

Generate a complete study plan.

Subject:
{subject}

Exam Date:
{exam_date}

Available Study Hours Per Day:
{hours_per_day}

Difficulty Level:
{difficulty}

Create:

1. Weekly Study Plan
2. Monthly Study Plan

For each day include:

- Topics
- Study Hours
- Revision Time
- Practice Questions
- Break Suggestions

Make the output neat using headings and bullet points.
"""

        response = self.llm.invoke(prompt)

        return response.content