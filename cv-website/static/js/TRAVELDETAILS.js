
$('.input-file.travel input[type=file]').on('change', function(){
    // let file = this.files[0];
    var upload_button = document.getElementById('upload_button travel');

    // Изменяем стиль элемента, чтобы показать кнопку
    upload_button.style.display = 'block';});


document.getElementById('upload_button travel').addEventListener('click', function () {
    var fileInput = document.getElementById('file__input travel');
    var file = fileInput.files[0]; // Получаем выбранный 
    var button = document.getElementById('upload_button travel');
    
    var inputFileBlock = document.querySelector('.input-file.travel span');
    inputFileBlock.innerHTML = '<img src="../static/materials/personalDatails/checked.svg" class="file__checked" style="width: 30px;">';
    
    // Отключаем кнопку отправки фото
    var disabled_file_input = document.getElementById("file__input travel");
    var spanElement = document.querySelector('.input-file.travel span');
    disabled_file_input.disabled = true;
    spanElement.style.backgroundColor = 'rgba(0, 0, 0, 0.59)';
    spanElement.style.cursor = 'not-allowed';
    
    // Заменяем содержимое элемента новым HTML-кодом или текстом
    button.innerHTML = '<img src="../static/materials/personalDatails/loading.svg" class="upload-svg loading">';

    if (file) {
        var formData = new FormData();
        formData.append('file', file); // Добавляем файл в FormData

        fetch('/travel-detales', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            // Обработка ответа в формате JSON
            var country = document.getElementsByName('travel-country')[0];
            var valid = document.getElementsByName('travel-valid')[0];
            var issued = document.getElementsByName('travel-issued')[0];
            var document_type = document.getElementsByName('travel-document-type')[0];
            var number = document.getElementsByName('travel-number')[0];
            
            var hide_block = document.getElementById("upload_button travel");
            
            // Изменяем стиль элемента, чтобы скрыть кнопку
            hide_block.classList.add("hidden");
            
            
            // Заполняем поле ввода значением из JSON-объекта
            document_type.value = data["document-type"];
            country.value = data["country"];
            number.value = data["number"];
            issued.value = data["issued"]
            valid.value = data["valid"]
            console.log(data);
        })

        .catch(error => {
            console.error('Произошла ошибка:', error);
        });
    } else {
        console.error('Файл не выбран');
    }
});