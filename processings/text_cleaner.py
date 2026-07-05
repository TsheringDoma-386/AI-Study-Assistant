import re


class TextCleaner:

    def clean(self, text):

        text = re.sub(r"\s+", " ", text)

        text = text.replace("\t", " ")

        text = text.strip()

        return text