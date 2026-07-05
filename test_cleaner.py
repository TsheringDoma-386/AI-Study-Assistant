from processings.text_cleaner import TextCleaner

sample = """

Artificial      Intelligence


is


awesome.

"""

cleaner = TextCleaner()

print(cleaner.clean(sample))