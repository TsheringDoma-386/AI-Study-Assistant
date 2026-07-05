import os
import tempfile
import unittest

from processings.pdf_reader import PDFReader


class TestPDFReader(unittest.TestCase):
    def test_invalid_non_pdf_raises_value_error(self):
        with tempfile.NamedTemporaryFile("w", suffix=".pdf", delete=False) as handle:
            handle.write("this is not a real pdf")
            temp_path = handle.name

        try:
            with self.assertRaises(ValueError):
                PDFReader().extract_text(temp_path)
        finally:
            os.remove(temp_path)


if __name__ == "__main__":
    unittest.main()
