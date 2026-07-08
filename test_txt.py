from processings.txt_reader import TXTReader

reader = TXTReader()

text = reader.extract_text("uploads/sample.txt")

print(text)