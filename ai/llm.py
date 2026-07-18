import os

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI


# Load environment variables
load_dotenv()


def get_llm():
    """
    Returns a Gemini LLM object.
    """

    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY not found in .env file."
        )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=api_key,
        temperature=0.3
    )

    return llm
