from ai.llm import get_llm


class StudyPlanner:
    def __init__(self):
        self.llm = get_llm()

    def generate_plan(self, subject, hours, days, preferred_time):

        prompt = f"""
You are an AI Study Planner.

Create a study schedule.

Subject: {subject}

Study Hours Per Session: {hours}

Study Days: {days}

Preferred Time: {preferred_time}

Generate a clear weekly study timetable with:
- Day
- Time
- Study Task
- Suggested Breaks
"""

        response = self.llm.invoke(prompt)

        return response.content