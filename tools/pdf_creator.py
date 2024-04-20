# -*- coding: utf-8 -*-
# РАЗРАБОТКА ОТ T.ME/FELIX4
# СОЗДАНИЕ НОВОГО PDF ФАЙЛА

from tools.face_cropping import FaceCropping
from io import BytesIO
from os import remove
import fitz



class CreatorPDF:
    def __init__(self, file_code: str) -> None:
        """Создание PDF файла tools/load/"""
        self._file_code: str = file_code
        
    def creating(self,         
        personal_surname: str,
        personal_name: str,
        personal_fathers: str,
        personal_date: str,
        personal_address: str,
        personal_height: str,
        personal_eyes: str,
        personal_hair: str,
        personal_weight: str,
        
        contact_mobile: str,
        contact_email: str,
        
        next_mobile: str,
        next_address: str,
        next_reality: str,
        next_name: str,
        
        # travel_document_type: str,
        travel_country: str,
        travel_valid: str,
        travel_issued: str,
        travel_number: str,
        
        # seamans_document_type_1: str,
        seamans_dqk_code_1: str,
        seamans_country_1: str,
        seamans_issued_1: str,
        seamans_valid_1: str,
        
        # seamans_document_type_2: str,
        seamans_number_2: str,
        seamans_country_2: str,
        seamans_issued_2: str,
        seamans_valid_2: str,

        education_school: str,
        education_issue: str,
        education_class: str,
        education_from: str,
        education_to: str,
        
        # language_language_1: str,
        # language_speaking_1: str,
        # language_reading_1: str,
        # language_writing_1: str,
        # language_language_2: str,
        # language_speaking_2: str,
        # language_reading_2: str,
        # language_writing_2: str,

        # medical_document: str,
        medical_grade: str,
        medical_place_issue: str,
        medical_date_issue: str,
        medical_expiry: str,

        certificate_grade: str,
        certificate_country: str,
        certificate_certificate: str,
        certificate_date: str,
        certificate_expires: str,
        certificate_details: str):
        
        # scaner: list = Scanner(file_path=self._file_path).document_result
        # information = Person(information=scaner)
        # result: dict = {
        #     "name": information.name,
        #     "date": information.date,
        #     "height": information.height,
        #     "surname": information.surname,
        #     "address": information.address,
        #     "fathers-name": information.fathers_name,
        #     "eyes-color": information.eyes_color,
        #     "hair-color": information.hair_color}
        
        open_document = fitz.open("mainPage.pdf")
        page = open_document[0]

        try:
            # Получаем первую страницу PDF-документа (может потребоваться изменить номер страницы)
            # Вставляем изображение на страницу PDF с указанными координатами и масштабом
            with open("face.png", "rb") as image_file:
                image_bytes = image_file.read()
                page.insert_image(fitz.Rect(100, 140, 890, 320), stream=BytesIO(image_bytes), keep_proportion=True)
        except: ...

        # PERSONAL
        page.insert_text(fitz.Point(240, 179), personal_surname, fontname="Times-Roman", fontsize=13)
        page.insert_text(fitz.Point(240, 198), personal_name, fontname="Times-Roman", fontsize=13)
        page.insert_text(fitz.Point(240, 220), personal_fathers, fontname="Times-Roman", fontsize=13)
        page.insert_text(fitz.Point(240, 242), personal_date, fontname="Times-Roman", fontsize=13)
        page.insert_text(fitz.Point(240, 276), personal_address, fontname="Times-Roman", fontsize=13)
        page.insert_text(fitz.Point(52, 374), personal_height, fontname="Times-Roman", fontsize=13)
        page.insert_text(fitz.Point(215, 374), personal_eyes, fontname="Times-Roman", fontsize=13)
        page.insert_text(fitz.Point(145, 374), personal_weight, fontname="Times-Roman", fontsize=13)
        
        # CONTACT
        page.insert_text(fitz.Point(130, 448), contact_mobile, fontname="Times-Roman", fontsize=13)
        page.insert_text(fitz.Point(390, 448), contact_email, fontname="Times-Roman", fontsize=13)

        # NEXT OF KIN
        page.insert_text(fitz.Point(110, 527), next_name, fontname="Times-Roman", fontsize=13)
        page.insert_text(fitz.Point(240, 527), next_mobile, fontname="Times-Roman", fontsize=13)
        page.insert_text(fitz.Point(370, 527), next_reality, fontname="Times-Roman", fontsize=13)
        page.insert_text(fitz.Point(447, 527), next_address, fontname="Times-Roman", fontsize=13)
        
        # TRAVEL PASSPORT DETAILS
        page.insert_text(fitz.Point(240, 600), travel_number, fontname="Times-Roman", fontsize=13)
        page.insert_text(fitz.Point(340, 600), travel_country, fontname="Times-Roman", fontsize=13)
        page.insert_text(fitz.Point(450, 600), travel_issued, fontname="Times-Roman", fontsize=13)
        page.insert_text(fitz.Point(517, 600), travel_valid, fontname="Times-Roman", fontsize=13)

        # SEAMANS BOOK DETAILS
        page = open_document[1]
        page.insert_text(fitz.Point(238, 129), seamans_dqk_code_1, fontname="Times-Roman", fontsize=13)
        page.insert_text(fitz.Point(322, 129), seamans_country_1, fontname="Times-Roman", fontsize=12)
        page.insert_text(fitz.Point(452, 129), seamans_issued_1, fontname="Times-Roman", fontsize=12)
        page.insert_text(fitz.Point(522, 129), seamans_valid_1, fontname="Times-Roman", fontsize=12)

        page.insert_text(fitz.Point(238, 145), seamans_number_2, fontname="Times-Roman", fontsize=13)
        page.insert_text(fitz.Point(322, 145), seamans_country_2, fontname="Times-Roman", fontsize=12)
        page.insert_text(fitz.Point(452, 145), seamans_issued_2, fontname="Times-Roman", fontsize=12)
        page.insert_text(fitz.Point(522, 145), seamans_valid_2, fontname="Times-Roman", fontsize=12)

        page.insert_text(fitz.Point(53, 222), education_school, fontname="Times-Roman", fontsize=14)
        page.insert_text(fitz.Point(231, 222), education_issue, fontname="Times-Roman", fontsize=14)
        page.insert_text(fitz.Point(331, 222), education_class, fontname="Times-Roman", fontsize=13)
        page.insert_text(fitz.Point(461, 230), education_from, fontname="Times-Roman", fontsize=14)
        page.insert_text(fitz.Point(531, 230), education_to, fontname="Times-Roman", fontsize=14)

        page.insert_text(fitz.Point(177, 460), medical_grade, fontname="Times-Roman", fontsize=14)
        page.insert_text(fitz.Point(301, 460), medical_place_issue, fontname="Times-Roman", fontsize=14)
        page.insert_text(fitz.Point(401, 466), medical_date_issue, fontname="Times-Roman", fontsize=14)
        page.insert_text(fitz.Point(490, 466), medical_expiry, fontname="Times-Roman", fontsize=14)
    
        page.insert_text(fitz.Point(50, 618), certificate_grade, fontname="Times-Roman", fontsize=14)
        page.insert_text(fitz.Point(158, 618), certificate_country, fontname="Times-Roman", fontsize=12)
        page.insert_text(fitz.Point(277, 618), certificate_certificate, fontname="Times-Roman", fontsize=12)
        page.insert_text(fitz.Point(363, 627), certificate_date, fontname="Times-Roman", fontsize=15)
        page.insert_text(fitz.Point(438, 627), certificate_expires, fontname="Times-Roman", fontsize=11)
        page.insert_text(fitz.Point(517, 627), certificate_details, fontname="Times-Roman", fontsize=17)
      

        open_document.save("tools/load/" + self._file_code + ".pdf")

        # Удаление фото фейса
        # remove(path="face.png")

# CreatorPDF("").creating()