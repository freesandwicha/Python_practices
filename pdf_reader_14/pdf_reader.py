# -*- coding = utf-8 -*-
# Motto : Practice makes perfect.
# Time : 26/8/2023 12:20 pm

import re
from collections import Counter
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_file: str) -> list[str]:
    with open(pdf_file, 'rb') as pdf:
        #For a PDF, which isn't a plaintext format like .txt or .csv,
        # using binary mode ensures the content is correctly read without issues that might arise from encoding or decoding binary data as text.
        reader = PdfReader(pdf, strict=False)
        #PdfReader can read PDF

        print('Pages', len(reader.pages))
        print('-' * 10) #Divider

        #In the PdfReader object, pages is an attribute that represents all the pages of the PDF as a list-like object.
        pdf_text: list[str] = [page.extract_text() for page in reader.pages]
        #The page.extract_text() method attempts to extract all the textual content from that particular page.
        # It returns the extracted text as a string.
        #reader.pages gives us access to all the individual pages in the PDF.
        return pdf_text

def counter_words(text_list: list[str]) -> Counter:
    all_words: list[str] = []
    for text in text_list:
        splite_text: list[str] = re.split(r'\s+| [,;?!.-]\s*', text.lower())
        #split function from the re module splits a string by the occurrences of a pattern.
        #print(splite_text)

        all_words += [word for word in splite_text if word]
    return Counter(all_words)
  # This object will have each word as a key and its frequency as the value.


def main():
    extract_text: list[str] = extract_text_from_pdf('sample.pdf')
    counter: Counter = counter_words(text_list=extract_text)

    for word, mentions in counter.most_common(7):
        print(f'{word:7}: {mentions} times')


if __name__ == '__main__':
    main()



