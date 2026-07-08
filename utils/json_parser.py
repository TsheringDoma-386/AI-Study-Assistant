import json


def parse_flashcards(response_text):
    """
    Convert Gemini JSON response into a Python list.
    """

    cleaned = response_text.replace("```json", "").replace("```", "").strip()

    return json.loads(cleaned)