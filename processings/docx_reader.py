from pathlib import Path

from docx import Document


class DOCXReader:
    """Read text from DOCX files."""

    def _resolve_path(self, file_path: str) -> Path:
        path = Path(file_path)
        root = Path(__file__).resolve().parents[1]

        candidates = []
        if path.is_absolute():
            candidates.append(path)
        else:
            candidates.append(path)
            candidates.append(root / path)

            if path.parts and path.parts[0] in {"upload", "uploads"}:
                candidates.append(root / Path("upload", *path.parts[1:]))
                candidates.append(root / Path("uploads", *path.parts[1:]))
            else:
                candidates.append(root / "upload" / path.name)
                candidates.append(root / "uploads" / path.name)

        for candidate in candidates:
            if candidate.exists():
                return candidate

        return candidates[0] if candidates else path

    def extract_text(self, file_path: str) -> str:
        resolved_path = self._resolve_path(file_path)
        document = Document(str(resolved_path))

        text = ""

        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"

        return text