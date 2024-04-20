# -*- coding: utf-8 -*-
# РАЗРАБОТКА ОТ T.ME/FELIX4

import fitz  # PyMuPDF
from PIL import Image
from os import remove

# СОЗДАНИЕ PNG ИЗ PDF 
def pdf_to_single_png_pymupdf(file_code: str, input_pdf_path: str="mainPage.pdf" , output_png_path: str="tools/load", resolution: int=200):
    """Создание PNG из PDF
    :params: input_pdf_path - Путь где находить сам PDF 
    :params: output_png_path - Путь где будет сохраняться сам PNG 
    :return: STR - Название файла на выходе"""

    all_images = []
    max_width, total_height = 0, 0
    pdf_document = fitz.open(input_pdf_path)

    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]
        image = page.get_pixmap(matrix=fitz.Matrix(resolution / 72, resolution / 72))
        all_images.append(Image.frombytes("RGB", [image.width, image.height], image.samples))
        max_width = max(max_width, image.width)
        total_height += image.height

    # Создаем пустой холст с максимальными размерами
    pdf_document.close()
    combined_image = Image.new("RGB", (max_width, total_height))

    # Наложение каждого изображения на холст
    offset = 0
    for image in all_images:
        combined_image.paste(image, (0, offset))
        offset += image.height

    # Сохраняем объединенное изображение
    output_file_name: str = f"{output_png_path}/{file_code}.png"
    combined_image.save(output_file_name)
    remove(F"{output_png_path}/{file_code}.pdf")
    
    return output_file_name

# Пример использования
if __name__ == "__main__":
    print(pdf_to_single_png_pymupdf())

