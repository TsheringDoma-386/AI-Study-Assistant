import sqlite3

DATABASE_NAME = "study_materials.db"


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS study_materials(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        upload_date TEXT,
        quiz TEXT,
        flashcards TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS study_progress(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        documents_uploaded INTEGER,
        quizzes_generated INTEGER,
        flashcards_generated INTEGER,
        last_activity TEXT
    )
    """)

    conn.commit()
    conn.close()