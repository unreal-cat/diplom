from quart import Quart, render_template, request, send_file
from tools.scaner import Scanner, Person, Vesiqe
from tools.pdf_creator import CreatorPDF
from tools.face_cropping import FaceCropping
from tools.site_login import Authorization
from tools.create_pdf_password import add_password_to_pdf
from tools.create_png import pdf_to_single_png_pymupdf
from random import randint
import secrets, os


app = Quart(__name__, static_folder="cv-website/static", template_folder="cv-website/template")

@app.route("/", methods=["GET"])
async def _web():
    return await render_template("login.html", button_text="ВОЙТИ")

@app.route("/reflink", methods=["GET"])
async def _reflink_main():
    return await render_template("login.html", button_text="ВОЙТИ")


@app.route("/reflink/<reflink>", methods=["GET"])
async def _reflink(reflink):
    authorization = Authorization()
    if authorization.check_reflink(reflink=reflink):
        authorization.del_reflink(reflink=reflink)
        return await render_template("index.html")

    return await render_template("login.html", button_text="<span style='font-color: red'>ОШИБКА ВХОДА | ПОВТОРИТЬ</span>")


@app.route("/authorization", methods=["POST"])
async def _authorization():
    authorization_info = await request.json
    authorization = Authorization()
    account_status = authorization.check_account(
        user_login=authorization_info.get("login"),
        user_password=authorization_info.get("password"))
    
    if account_status: 
        return {"status": True, "reflink": F"reflink/{authorization.new_reflink()}"}

    else: return {"status": False, "reflink": F"reflink/error"}

@app.route('/personal-detales', methods=['POST', 'GET'])
async def personal_detalis():
    file = await request.files
    file = file.get('file')

    if file:
        # обработка файла
        file_name = file.filename
        file_path = f"tools/upload/{file_name}"
        await file.save(file_path)

        scaner: list = Scanner(file_path=file_path).document_result
        face_photo = FaceCropping(image_path=file_path)
        information = Person(information=scaner)
        
        result: dict = {
            "name": information.name,
            "date": information.date,
            "height": information.height,
            "surname": information.surname,
            "address": information.address,
            "fathers-name": information.fathers_name,
            "eyes-color": information.eyes_color,
            "hair-color": information.hair_color,
            "document-photo": face_photo.crop_face,
            "dqk-code": information.dqk_code}

        print("\n", result)
        return result
    

    else:
        print("REQUESTS ADDED - FALSE")
        return {"status": False} #'Ошибка загрузки файла'
    

@app.route('/travel-detales', methods=['POST', 'GET'])
async def travel_detalis():
    file = await request.files
    file = file.get('file')
    print("REQUESTS ADDED")
    if file:
        # обработка файла
        print("REQUESTS ADDED — TRUE")
        filename = file.filename
        await file.save(F"tools/upload/{filename}")

        scaner: list = Scanner(file_path=f"tools/upload/{filename}", is_passport=True).document_result
        information = Person(information=scaner, is_passport=True)
        result: dict = {
            "number": information.passport_id,
            "country": information.passport_country,
            "document-type": information.document_type,
            "issued": information.passport_date_issue,
            "valid": information.passport_expiration_date}

        return result
    

    else:
        print("REQUESTS ADDED - FALSE")
        return {"status": False} #'Ошибка загрузки файла'

@app.route('/seamans-detales', methods=['POST', 'GET'])
async def seamans_details():
    seamans_book_file = await request.files
    seamans_book_json = await request.form
    file = seamans_book_file.get('file')
    radio_old = seamans_book_json.get("radio_old")
    radio_now = seamans_book_json.get("radio_now")
    print(seamans_book_json)
    if file:
        # обработка файла
        print("REQUESTS ADDED — TRUE — SEAMANS")
        
        filename = F"{file.filename}-{randint(1111,9999)}"
        await file.save(F"tools/upload/{filename}")

        scaner: list = Scanner(file_path=f"tools/upload/{filename}", is_passport=False).document_result
        if radio_now == "on": information = Vesiqe(information=scaner, switch=True)
        if radio_old == "on": information = Vesiqe(information=scaner, switch=False)

        print()
        print(F"{information.country=}")
        print()

        result: dict = {
            "document-1": {
                "name": "SEAMANS BOOK",
                "country": information.country,
                "date-start": information.date[0],
                "date-end": information.date[1]},

            "document-2": {
                "name": "SEAARERS IDENTITY",
                "number": information.number,
                "country": information.country,
                "date-start": information.date[0],
                "date-end": information.date[1]}}
        
        return result

@app.route("/<file_code>", methods=["GET", "POST"])
async def _download(file_code):
    print(file_code)
    if os.path.exists("tools/load/" + file_code + ".pdf"):
        return await send_file("tools/load/" + file_code + ".pdf", mimetype="application/pdf")
    
    if os.path.exists("tools/load/" + file_code + ".png"):
        return await send_file("tools/load/" + file_code + ".png", mimetype="application/png")

    return 404


@app.route("/download", methods=["GET", "POST"])
async def _load():
    document_info = await request.json
    file_code = secrets.token_hex(6)

    CreatorPDF(file_code=file_code).creating(
        personal_surname = document_info.get("personal-surname"),
        personal_name = document_info.get("personal-name"),
        personal_fathers = document_info.get("personal-fathers"),
        personal_date = document_info.get("personal-date"),
        personal_address = document_info.get("personal-address"),
        personal_height = document_info.get("personal-height"),
        personal_eyes = document_info.get("personal-eyes"),
        personal_hair = document_info.get("personal-hair"),
        personal_weight = document_info.get("personal-weight"),

        contact_mobile = document_info.get("contact-mobile"),
        contact_email = document_info.get("contact-email"),
        
        next_mobile = document_info.get("next-mobile"),
        next_address = document_info.get("next-address"),
        next_reality = document_info.get("next-reality"),
        next_name = document_info.get("next-name"),

        # travel_document_type = document_info.get("travel-document-type"),
        travel_country = document_info.get("travel-country"),
        travel_valid = document_info.get("travel-valid"),
        travel_issued = document_info.get("travel-issued"),
        travel_number = document_info.get("travel-number"),
        
        # seamans_document_type_1 = document_info.get("seamans-document-type-1"),
        seamans_dqk_code_1 = document_info.get("seamans-dqk-code-1"),
        seamans_country_1 = document_info.get("seamans-country-1"),
        seamans_issued_1 = document_info.get("seamans-issued-1"),
        seamans_valid_1 = document_info.get("seamans-valid-1"),
        
        # seamans_document_type_2 = document_info.get("seamans-document-type-2"),
        seamans_number_2 = document_info.get("seamans-number-2"),
        seamans_country_2 = document_info.get("seamans-country-2"),
        seamans_issued_2 = document_info.get("seamans-issued-2"),
        seamans_valid_2 = document_info.get("seamans-valid-2"),

        education_school = document_info.get("education-school"),
        education_issue = document_info.get("education-issue"),
        education_class = document_info.get("education-class"),
        education_from = document_info.get("education-from"),
        education_to = document_info.get("education-to"),

        # document_info.get("language-language-1"),
        # document_info.get("language-speaking-1"),
        # document_info.get("language-reading-1"),
        # document_info.get("language-writing-1"),
        # document_info.get("language-language-2"),
        # document_info.get("language-speaking-2"),
        # document_info.get("language-reading-2"),
        # document_info.get("language-writing-2"),
        
        # medical_document = document_info.get("medical-document"),
        medical_grade = document_info.get("medical-grade"),
        medical_place_issue = document_info.get("medical-place-issue"),
        medical_date_issue = document_info.get("medical-date-issue"),
        medical_expiry = document_info.get("medical-expiry"),
        
        certificate_grade = document_info.get("certificate-grade"),
        certificate_country = document_info.get("certificate-country"),
        certificate_certificate = document_info.get("certificate-certificate"),
        certificate_date = document_info.get("certificate-date-issued"),
        certificate_expires = document_info.get("certificate-expires"),
        certificate_details = document_info.get("certificate-details"))    

    # СТАВИТ ПАРОЛЬ НА PDF 
    if "-" in document_info.get("document-password", "0"): 
        add_password_to_pdf(password=document_info.get("document-password"), 
                            input_pdf_path=F"tools/load/{file_code}.pdf",
                            file_code=file_code)

    # ДЕЛАЕТ PNG ИЗ PDF
    if document_info.get("document-png", "off") == "on":
        pdf_to_single_png_pymupdf(file_code=file_code, input_pdf_path=F"tools/load/{file_code}.pdf")


    print("\n", document_info)
    print("\n", document_info.get("document-png", "off"))
    
    return {"status": True, "filecode": file_code}


# УСТАНОВКА ДОМЕНА
app.run("localhost", 9001, debug=True)