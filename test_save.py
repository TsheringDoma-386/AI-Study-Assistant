from datetime import datetime

from database.models import save_material

save_material(
    filename="software engineering.pdf",
    upload_date=str(datetime.now()),
    quiz="Sample Quiz",
    flashcards="Sample Flashcards"
)

print("Saved Successfully!")