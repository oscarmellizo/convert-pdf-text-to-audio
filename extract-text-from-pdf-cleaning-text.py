from PyPDF2 import PdfReader

with open("TutorialPython3.pdf", "rb") as book:
    book_reader = PdfReader(book)
    page_list = book_reader.pages
    introduction_page = page_list[8]
    page_text = introduction_page.extract_text()
    print(page_text)
    page_text_cleaning = ''.join(page_text.splitlines())
    print(page_text_cleaning)
    