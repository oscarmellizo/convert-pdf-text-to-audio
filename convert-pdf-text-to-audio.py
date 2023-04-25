from PyPDF2 import PdfReader
import pyttsx3

def get_text_fron_pdf(file_name, page_number_from, page_number_to):
    with open(file_name, "rb") as pdf:
        book_reader = PdfReader(pdf)
        page_list = book_reader.pages
        text = ""
        for index in range(page_number_from,page_number_to):
            introduction_page = page_list[index]
            text = text + introduction_page.extract_text() + " "
    return text

def remove_line_break(value):
    return ' '.join(value.splitlines())

def generate_mp3_from_text(text, file_name):
    engine = pyttsx3.init("sapi5")
    engine.save_to_file(text, file_name + ".mp3")
    engine.runAndWait()

pdf_text = get_text_fron_pdf("TutorialPython3.pdf", 8, 11)
print("[" + pdf_text + "]")
pdf_text_without_line_break = remove_line_break(pdf_text)
generate_mp3_from_text(pdf_text_without_line_break, "introduction")