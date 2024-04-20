function password_gen() {
    // Генерация рандомного числа для последних трех цифр (от 100 до 999)
    var password_button = document.getElementById("document-password");    
    var password_one = Math.floor(100 + Math.random() * 900).toString();
    var password_two = Math.floor(100 + Math.random() * 900).toString();
    password_button.textContent = password_one + "-" + password_two;
    
    if (document.querySelector(".password").style.backgroundColor === "rgb(255, 255, 255)") {
        document.querySelector(".password").style.backgroundColor = "rgb(166 192 255 / 69%)";}
}

function document_png() {
    var png_button = document.getElementById("document_png");  
    if (png_button.style.backgroundColor === "rgb(255, 255, 255)") {
        png_button.style.backgroundColor = "rgb(166 192 255 / 69%)";
        png_button.setAttribute("data-value", "on");
    } else {
        png_button.style.backgroundColor = "#fff";
        png_button.setAttribute("data-value", "off");
    }
}
console.log(document.getElementById("document_png").dataset.value)
var saveBlock = document.querySelector(".save");
saveBlock.addEventListener("click", function() {
    // ИНФОРМАЦИЯ КОТОРУЮ НУЖНО ОТПРАВИТЬ НА СЕРВЕР
    if (saveBlock.style.backgroundColor === "rgb(255, 255, 255)") {
        saveBlock.style.backgroundColor = "rgb(166 192 255 / 69%)";}
    
    const data = {
        // PERSONAL BLOCK
        "personal-surname": document.getElementsByName('surname')[0].value,
        "personal-name": document.getElementsByName('name')[0].value,
        "personal-fathers": document.getElementsByName('fathers-name')[0].value,
        "personal-date": document.getElementsByName('date')[0].value,
        "personal-address": document.getElementsByName('address')[0].value,
        "personal-height": document.getElementsByName('height')[0].value,
        "personal-eyes": document.getElementsByName('eyes-color')[0].value,
        "personal-hair": document.getElementsByName('hair-color')[0].value,
        "personal-weight": document.getElementsByName('weight')[0].value,
        
        // CONTACT BLOCK
        "contact-mobile": document.getElementsByName('mobile')[0].value,
        "contact-email": document.getElementsByName('email')[0].value,
        
        // NEXT OF KIN BLOCK
        "next-mobile": document.getElementsByName('next-mobile')[0].value,
        "next-address": document.getElementsByName('next-address')[0].value,
        "next-reality": document.getElementsByName('next-reality')[0].value,
        "next-name": document.getElementsByName('next-name')[0].value,
        
        // TRAVEL BLOCK
        "travel-country": document.getElementsByName('travel-country')[0].value,
        "travel-valid": document.getElementsByName('travel-valid')[0].value,
        "travel-issued": document.getElementsByName('travel-issued')[0].value,
        "travel-document-type": document.getElementsByName('travel-document-type')[0].value,
        "travel-number": document.getElementsByName('travel-number')[0].value,
        
        // SEAMANS BLOCK
        "seamans-document-type-1": document.getElementsByName('seamans-document-type-1')[0].value,
        "seamans-dqk-code-1": document.getElementsByName('seamans-dqk-code-1')[0].value,
        "seamans-country-1": document.getElementsByName('seamans-country-1')[0].value,
        "seamans-issued-1": document.getElementsByName('seamans-issued-1')[0].value,
        "seamans-valid-1": document.getElementsByName('seamans-valid-1')[0].value,
        
        "seamans-document-type-2": document.getElementsByName('seamans-document-type-2')[0].value,
        "seamans-number-2": document.getElementsByName('seamans-number-2')[0].value,
        "seamans-country-2": document.getElementsByName('seamans-country-2')[0].value,
        "seamans-issued-2": document.getElementsByName('seamans-issued-2')[0].value,
        "seamans-valid-2": document.getElementsByName('seamans-valid-2')[0].value,

        // EDUCATION BLOCK
        "education-school": document.getElementsByName('education-school')[0].value,
        "education-issue": document.getElementsByName('education-issue')[0].value,
        "education-class": document.getElementsByName('education-class')[0].value,
        "education-from": document.getElementsByName('education-from')[0].value,
        "education-to": document.getElementsByName('education-to')[0].value,

        // KNOWLEDGE LANGUAGE
        "language-language-1": document.getElementsByName('language-language-1')[0].value,
        "language-speaking-1": document.getElementsByName('language-speaking-1')[0].value,
        "language-reading-1": document.getElementsByName('language-reading-1')[0].value,
        "language-writing-1": document.getElementsByName('language-writing-1')[0].value,
        
        "language-language-2": document.getElementsByName('language-language-2')[0].value,
        "language-speaking-2": document.getElementsByName('language-speaking-2')[0].value,
        "language-reading-2": document.getElementsByName('language-reading-2')[0].value,
        "language-writing-2": document.getElementsByName('language-writing-2')[0].value,
        
        // MEDICAL INFORMATION
        "medical-document": document.getElementsByName('medical-document')[0].value,
        "medical-grade": document.getElementsByName('medical-grade')[0].value,
        "medical-place-issue": document.getElementsByName('medical-place-issue')[0].value,
        "medical-date-issue": document.getElementsByName('medical-date-issue')[0].value,
        "medical-expiry": document.getElementsByName('medical-expiry')[0].value,

        // CERTIFICATE OF COMPETENCY
        "certificate-grade": document.getElementsByName('certificate-grade')[0].value,
        "certificate-country": document.getElementsByName('certificate-country')[0].value,
        "certificate-certificate": document.getElementsByName('certificate-certificate')[0].value,
        "certificate-date-issued": document.getElementsByName('certificate-date-issued')[0].value,
        "certificate-expires": document.getElementsByName('certificate-expires')[0].value,
        "certificate-details": document.getElementsByName('certificate-details')[0].value,
        
        // ENDBLOCK
        "document-password": document.getElementById("document-password").textContent.trim(),
        "document-png": document.getElementById("document_png").dataset.value,
    };

    // Метод запроса (может быть и 'GET', в зависимости от вашего случая)
    // Преобразование данных в JSON и отправка их как тело запроса
    fetch('/download', {
        method: 'POST', 
        body: JSON.stringify(data), 
        headers: {
            'Content-Type': 'application/json' 
        }
    })
    .then(response => {
        if (!response.ok) {
            // Если ответ не успешен, бросаем ошибку
            throw new Error('Ошибка сети');
        }
        // Если запрос успешен и ответ получен, начнем печать
        return response.json();

    })
    .then(data => {
        // Обращаемся к свойству "filecode" в объекте "data"
        var url = "/" + data["filecode"];
        
        // Открываем ссылку во втором окне (новой вкладке)
        window.open(url, '_blank');
    })
    .catch(error => {
        console.error(error);
    });
});
