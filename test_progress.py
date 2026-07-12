from datetime import datetime

from database.db import create_tables
from database.models import save_progress, get_latest_progress

create_tables()

save_progress(
    documents=5,
    quizzes=12,
    flashcards=60,
    date=str(datetime.now())
)

progress = get_latest_progress()

print(progress)