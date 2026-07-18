from turtle import st

from database.db import get_connection


def save_progress(documents, quizzes, flashcards, date):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO study_progress(
        documents_uploaded,
        quizzes_generated,
        flashcards_generated,
        last_activity
    )
    VALUES (?, ?, ?, ?)
    """, (documents, quizzes, flashcards, date))

    conn.commit()
    conn.close()


def get_latest_progress():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT documents_uploaded,
           quizzes_generated,
           flashcards_generated,
           last_activity
    FROM study_progress
    ORDER BY id DESC
    LIMIT 1
    """)

    row = cursor.fetchone()

    conn.close()

    return row
from database.db import get_connection

def save_study_schedule(subject, difficulty, hours):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO study_schedule(
        subject,
        difficulty,
        study_hours
    )
    VALUES (?, ?, ?)
    """, (subject, difficulty, hours))

    conn.commit()
    conn.close()


def get_study_schedule():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT subject, difficulty, study_hours
    FROM study_schedule
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows
st.header("📚 Subject-wise Time Allocation")

subject = st.text_input("Subject Name")

difficulty = st.selectbox(
    "Difficulty",
    ["Easy", "Medium", "Hard"]
)
from database.db import get_connection

def save_study_plan(subject, exam_date, difficulty, hours, plan):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO study_plans(
        subject,
        exam_date,
        difficulty,
        hours_per_day,
        study_plan
    )
    VALUES (?, ?, ?, ?, ?)
    """, (subject, exam_date, difficulty, hours, plan))

    conn.commit()
    conn.close()


def get_all_study_plans():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT subject,
           exam_date,
           difficulty,
           hours_per_day,
           study_plan
    FROM study_plans
    """)

    plans = cursor.fetchall()

    conn.close()

    return plans
from database.db import get_connection

def save_recommendation(subject, recommendation):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO recommendations(
        subject,
        recommendation
    )
    VALUES (?, ?)
    """, (subject, recommendation))

    conn.commit()
    conn.close()


def get_recommendations():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT subject, recommendation
    FROM recommendations
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows