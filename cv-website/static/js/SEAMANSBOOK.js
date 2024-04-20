// Получаем кнопку по идентификатору "fid-2"
var radio_button_1 = document.getElementById("fid-1");
var radio_button_2 = document.getElementById("fid-2");

// Добавляем обработчик события "click"
// Устанавливаем новое значение атрибута "value"
radio_button_1.addEventListener("click", function() {
    radio_button_2.value = "off";
    radio_button_1.value = "on";});
  
radio_button_2.addEventListener("click", function() {
  radio_button_1.value = "off";
  radio_button_2.value = "on";});




$('.input-file.seamans input[type=file]').on('change', function(){
    // let file = this.files[0];
    var upload_button = document.getElementById('upload_button seamans');

    // Изменяем стиль элемента, чтобы показать кнопку
    upload_button.style.display = 'block';});


document.getElementById('upload_button seamans').addEventListener('click', function () {
    var fileInput = document.getElementById('file__input seamans');
    var file = fileInput.files[0]; // Получаем выбранный 
    var button = document.getElementById('upload_button seamans');
    
    var inputFileBlock = document.querySelector('.input-file.seamans span');
    inputFileBlock.innerHTML = '<img src="../static/materials/personalDatails/checked.svg" class="file__checked" style="width: 30px;">';
    
    // Отключаем кнопку отправки фото
    var disabled_file_input = document.getElementById("file__input seamans");
    var spanElement = document.querySelector('.input-file.seamans span');
    disabled_file_input.disabled = true;
    spanElement.style.backgroundColor = 'rgba(0, 0, 0, 0.59)';
    spanElement.style.cursor = 'not-allowed';
    
    // Заменяем содержимое элемента новым HTML-кодом или текстом
    button.innerHTML = '<img src="../static/materials/personalDatails/loading.svg" class="upload-svg loading">';

    if (file) {
        var formData = new FormData();
        formData.append('file', file); // Добавляем файл в FormData
        formData.append('radio_old', radio_button_1.value);
        formData.append('radio_now', radio_button_2.value);

        fetch('/seamans-detales', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            // Обработка ответа в формате JSON
            var document_type_1 = document.getElementsByName('seamans-document-type-1')[0];
            var country_1 = document.getElementsByName('seamans-country-1')[0];
            var issued_1 = document.getElementsByName('seamans-issued-1')[0];
            var valid_1 = document.getElementsByName('seamans-valid-1')[0];
            // - - - - - 
            var document_type_2 = document.getElementsByName('seamans-document-type-2')[0];
            var country_2 = document.getElementsByName('seamans-country-2')[0];
            var number_2 = document.getElementsByName('seamans-number-2')[0];
            var issued_2 = document.getElementsByName('seamans-issued-2')[0];
            var valid_2 = document.getElementsByName('seamans-valid-2')[0];
            
            // Изменяем стиль элемента, чтобы скрыть кнопку
            var hide_block = document.getElementById("upload_button seamans");
            hide_block.classList.add("hidden");
            
            
            // Заполняем поле ввода значением из JSON-объекта
            document_type_1.value = data["document-1"]["name"];
            country_1.value = data["document-1"]["country"];
            issued_1.value = data["document-1"]["date-start"];
            valid_1.value = data["document-1"]["date-end"];

            document_type_2.value = data["document-2"]["name"];
            country_2.value = data["document-2"]["country"];
            number_2.value = data["document-2"]["number"];
            issued_2.value = data["document-2"]["date-start"];
            valid_2.value = data["document-2"]["date-end"];
            console.log(data);
        })

        .catch(error => {
            console.error('Произошла ошибка:', error);
        });
    } else {
        console.error('Файл не выбран');
    }
});