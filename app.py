import tempfile
from pathlib import Path

import streamlit as st

from ai import quiz_generator
from processings.docx_reader import DOCXReader
from processings.pdf_reader import PDFReader
from processings.txt_reader import TXTReader

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