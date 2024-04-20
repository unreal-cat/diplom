# -*- coding: utf-8 -*-
# РАЗРАБОТКА ОТ T.ME/FELIX4

from PyPDF2 import PdfReader, PdfWriter

def add_password_to_pdf(password: str, file_code: str, input_pdf_path: str, output_pdf_path: str="tools/load"):
    """Создание пароля для PDF файла.
    :params: input_pdf_path: str - ПУТЬ К PDF ФАЙЛУ НА КОТОРУЮ НУЖНО ПОСТАВИТЬ ПАРОЛЬ
    :params: output_pdf_path: str - ПУТЬ КУДА БУДЕТ СОХРАНЯТСЯ PDF ФАЙЛ
    :params: file_code: str - КОД ФАЙЛА ДЛЯ СОХРАНЕНИЯ ЕГО В АРХИВЕ 
    :params: password: str - ПАРОЛЬ ДЛЯ PDF 
    :return: STR - ПУТЬ К СОХРАНЕННОМУ ФАЙЛУ"""

    # Открываем PDF-файл с помощью PyMuPDF
    output_pdf_name = F"{output_pdf_path}/{file_code}.pdf"
    with open(input_pdf_path, 'rb') as input_file:
        pdf_reader = PdfReader(input_file)
        pdf_writer = PdfWriter()

        # Добавляем страницы из оригинального PDF-файла в новый PDF-файл
        for page_number in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_number])

        # Устанавливаем пароль на новый PDF-файл
        pdf_writer.encrypt(password)

        with open(output_pdf_name, 'wb') as output_file:
            pdf_writer.write(output_file)

    return output_pdf_name

if __name__ == "__main__":
    add_password_to_pdf(password="12345")
