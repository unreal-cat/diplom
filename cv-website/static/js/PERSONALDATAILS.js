


$('.input-file.personal input[type=file]').on('change', function(){
    // let file = this.files[0];
    var upload_button = document.getElementById('upload_button personal');

    // Изменяем стиль элемента, чтобы показать кнопку
    upload_button.style.display = 'block';});


document.getElementById('upload_button personal').addEventListener('click', function () {
    var fileInput = document.getElementById('file__input personal');
    var file = fileInput.files[0]; // Получаем выбранный 
    var button = document.getElementById('upload_button personal');
    
    var inputFileBlock = document.querySelector('.input-file.personal span');
    inputFileBlock.innerHTML = '<img src="../static/materials/personalDatails/checked.svg" class="file__checked" style="width: 30px;">';
    
    // Отключаем кнопку отправки фото
    var disabled_file_input = document.getElementById("file__input personal");
    var spanElement = document.querySelector('.input-file.personal span');
    var imageElement = document.querySelector('.passport__photo__upload');
    imageElement.innerHTML = '<img src="../static/materials/personalDatails/loading.svg" style="width: 80px; opacity: 0.5;" class="upload-svg loading">';
    
    disabled_file_input.disabled = true;
    spanElement.style.backgroundColor = 'rgba(0, 0, 0, 0.59)';
    spanElement.style.cursor = 'not-allowed';
    
    // Заменяем содержимое элемента новым HTML-кодом или текстом
    button.innerHTML = '<img src="../static/materials/personalDatails/loading.svg" class="upload-svg loading">';

    if (file) {
        var formData = new FormData();
        formData.append('file', file); // Добавляем файл в FormData

        fetch('/personal-detales', {
            method: 'POST',
            body: formData})

        .then(response => response.json())
        .then(data => {
            // Обработка ответа в формате JSON
            var dqk_code = document.getElementsByName('seamans-dqk-code-1')[0];
            var fathers_name = document.getElementsByName('fathers-name')[0];
            var eyes_color = document.getElementsByName('eyes-color')[0];
            var hair_color = document.getElementsByName('hair-color')[0];
            var surname = document.getElementsByName('surname')[0];
            var address = document.getElementsByName('address')[0];
            var height = document.getElementsByName('height')[0];
            var date = document.getElementsByName('date')[0];
            var name = document.getElementsByName('name')[0]
            
            var hide_block = document.getElementById("upload_button personal");
            
            // Изменяем стиль элемента, чтобы скрыть кнопку
            hide_block.classList.add("hidden");
            
            
            // Заполняем поле ввода значением из JSON-объекта
            fathers_name.value = data["fathers-name"];
            eyes_color.value = data["eyes-color"]
            hair_color.value = data["hair-color"]
            dqk_code.value = data["dqk-code"];
            address.value = data["address"];
            surname.value = data["surname"];
            height.value = data["height"];
            name.value = data["name"];
            date.value = data["date"];


            // Создаем элемент img
            var imageEl = document.createElement('img');
            imageEl.src = "data:image/png;base64," + data["document-photo"];

            // Очистите содержимое элемента .passport__photo__upload
            imageElement.innerHTML = '';

            // Добавьте элемент img (imageEl) внутрь элемента .passport__photo__upload
            imageElement.appendChild(imageEl);

            // imageElement.innerHTML = '<img src="" class="document-photo"/>';
            
            // var doc_image = document.querySelector('.document-photo')
            // doc_image.scr = 
            
            
            console.log(data);
        })

        .catch(error => {
            console.error('Произошла ошибка:', error);
        });
    } else {
        console.error('Файл не выбран');
    }
});