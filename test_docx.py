from processings.docx_reader import DOCXReader

reader = DOCXReader()

text = reader.extract_text("upload/sample.docx")

print(text)