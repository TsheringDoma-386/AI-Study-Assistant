from database.db import get_connection


def save_material(filename, upload_date, quiz, flashcards):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO study_materials
        (filename, upload_date, quiz, flashcards)
        VALUES (?, ?, ?, ?)
    """, (filename, upload_date, quiz, flashcards))

    conn.commit()

    conn.close()


def get_all_materials():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM study_materials")

    rows = cursor.fetchall()

    conn.close()

    return rows