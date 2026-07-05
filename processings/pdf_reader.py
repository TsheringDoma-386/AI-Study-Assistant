import os
from pathlib import Path

import PyPDF2
from PyPDF2.errors import PdfReadError


class PDFReader:

    def __init__(self):
        pass

    def extract_text(self, pdf_path):

        """
        Extract text from a PDF file.

        Parameters
        ----------
        pdf_path : str

        Returns
        -------
        str
        """

        candidate = Path(pdf_path)
        if not candidate.is_absolute():
            for base in [Path.cwd(), Path(__file__).resolve().parent.parent]:
                possible = base / candidate
                if possible.exists():
                    candidate = possible
                    break

        if not candidate.exists():
            raise FileNotFoundError(f"{pdf_path} not found.")

        if candidate.stat().st_size == 0:
            raise ValueError(f"{candidate} is empty.")

        text = ""

        try:
            with candidate.open("rb") as file:
                reader = PyPDF2.PdfReader(file)

                for page in reader.pages:
                    extracted = page.extract_text()

                    if extracted:
                        text += extracted + "\n"
        except (PdfReadError, ValueError) as exc:
            raise ValueError(f"{pdf_path} is not a valid PDF or is corrupted: {exc}") from exc

        if not text.strip():
            raise ValueError(f"{pdf_path} does not contain readable text.")

        return text