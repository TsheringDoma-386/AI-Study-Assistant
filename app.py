import tempfile
from pathlib import Path

import streamlit as st

from ai import quiz_generator
from ai.recommendation import RecommendationGenerator
from ai.study_plan_generator import StudyPlanGenerator
from processings.docx_reader import DOCXReader
from processings.pdf_reader import PDFReader
from processings.txt_reader import TXTReader
from database.models import get_latest_progress

st.title("AI Study Assistant")

st.write("Development environment is working!")

uploaded_file = st.file_uploader(
    "Upload Study Material",
    type=["pdf", "txt", "docx"],
)

if uploaded_file is not None:
    suffix = Path(uploaded_file.name).suffix.lower()

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
        temp_file.write(uploaded_file.getvalue())
        temp_path = temp_file.name

    try:
        if suffix == ".pdf":
            text = PDFReader().extract_text(temp_path)
        elif suffix == ".txt":
            text = TXTReader().extract_text(temp_path)
        elif suffix == ".docx":
            text = DOCXReader().extract_text(temp_path)
        else:
            text = ""

        st.text_area("Extracted Text", text, height=300)
    

        # create chunks for quiz generation (simple char-based chunks with overlap)
        def chunk_text(text, chunk_size=1000, overlap=200):
            if not text:
                return []
            chunks = []
            start = 0
            while start < len(text):
                end = min(start + chunk_size, len(text))
                chunks.append(text[start:end].strip())
                start = end - overlap if end - overlap > start else end
            return chunks

        chunks = chunk_text(text, chunk_size=1000, overlap=200)

    finally:
        Path(temp_path).unlink(missing_ok=True)

        difficulty = st.selectbox(
    "Select Difficulty",
    ["Easy", "Medium", "Hard"]
)

quiz_type = st.selectbox(
    "Select Quiz Type",
    ["MCQ", "True/False", "Fill in the Blanks"]
)
quiz =quiz_generator.generate_quiz(
    chunks[0],
    difficulty,
    quiz_type
)
import streamlit as st

if "flashcards" not in st.session_state:
    st.session_state.flashcards = []

if "current_card" not in st.session_state:
    st.session_state.current_card = 0

    card = st.session_state.flashcards[st.session_state.current_card]

st.subheader("Flashcard")

st.write("### Question")
st.write(card["question"])

if st.button("Show Answer"):
    st.write("### Answer")
    st.write(card["answer"])

    col1, col2 = st.columns(2)

with col1:
    if st.button("Previous") and st.session_state.current_card > 0:
        st.session_state.current_card -= 1

with col2:
    if (
        st.button("Next")
        and st.session_state.current_card < len(st.session_state.flashcards) - 1
    ):
        st.session_state.current_card += 1

        st.subheader("📊 Study Progress")

progress = get_latest_progress()

if progress:

    docs, quizzes, flashcards, last = progress

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Documents", docs)

    with col2:
        st.metric("Quizzes", quizzes)

    with col3:
        st.metric("Flashcards", flashcards)

    st.write(f"**Last Activity:** {last}")

else:
    st.info("No study progress available.")

    from datetime import datetime
from database.models import save_progress

save_progress(
    documents=1,
    quizzes=1,
    flashcards=10,
    date=str(datetime.now())
)
st.header("📅 AI Study Planner")

subject = st.text_input("Subject")

hours = st.number_input(
    "Study Hours",
    min_value=1,
    max_value=8,
    value=2
)

preferred_time = st.selectbox(
    "Preferred Time",
    ["Morning", "Afternoon", "Evening", "Night"]
)

days = st.multiselect(
    "Study Days",
    [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
)
class StudyPlanner:
    def generate_plan(self, subject, hours, days_csv, preferred_time):
        days = [d.strip() for d in days_csv.split(",") if d.strip()]
        plan_lines = []
        hours_per_day = max(1, min(hours, 8))
        for d in days:
            plan_lines.append(f"{d}: Study {subject} for {hours_per_day} hour(s) in the {preferred_time}.")
        return "\n".join(plan_lines) if plan_lines else "No days selected."

if st.button("Generate Study Plan"):

    planner = StudyPlanner()

    plan = planner.generate_plan(
        subject,
        hours,
        ", ".join(days),
        preferred_time
    )

    st.subheader("Your Weekly Study Plan")

    st.write(plan)
    st.header("⏰ Break Optimizer")

hours = st.number_input(
    "Study Hours",
    min_value=1,
    max_value=8,
    value=2
)
# ...existing code...
class BreakOptimizer:
    def __init__(self, config=None):
        self.config = config or {}

    def optimize(self, schedule):
        """
        Placeholder implementation — replace with your optimization logic.
        `schedule` can be any data structure you use (list/dict/etc).
        """
        # TODO: implement real optimization
        return schedule
# ...existing code...

if st.button("Generate Break Schedule"):

    optimizer = BreakOptimizer()

    schedule = optimizer.generate_schedule(hours)

    for item in schedule:
        st.write(f"{item['activity']} - {item['minutes']} minutes")
        st.header("📅 AI Study Plan Generator")

subject = st.text_input("Subject")

exam_date = st.date_input("Exam Date")

difficulty = st.selectbox(
    "Difficulty",
    ["Easy", "Medium", "Hard"]
)

hours = st.number_input(
    "Hours per Day",
    1,
    8,
    2
)

if st.button("Generate Study Plan"):

    planner = StudyPlanGenerator()

    plan = planner.generate_plan(
        subject,
        str(exam_date),
        hours,
        difficulty
    )

    st.write(plan)
    st.header("🤖 AI Study Coach")

subject = st.text_input("Subject")

quiz_count = st.number_input(
    "Quizzes Completed",
    0,
    100,
    10
)

flashcards = st.number_input(
    "Flashcards Reviewed",
    0,
    1000,
    50
)

hours = st.number_input(
    "Study Hours Per Week",
    1,
    50,
    8
)

if st.button("Get Recommendations"):

    coach = RecommendationGenerator()

    advice = coach.generate_recommendation(
        subject,
        quiz_count,
        flashcards,
        hours
    )

    st.write(advice)