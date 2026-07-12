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