import tempfile
from pathlib import Path

import streamlit as st

from ai import quiz_generator
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