from processings.chunker import Chunker

text = "Artificial Intelligence" * 500

chunker = Chunker()

chunks = chunker.split(text)

print("Chunks:", len(chunks))

print(chunks[0])