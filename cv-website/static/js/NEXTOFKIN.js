
var addButton = document.getElementById('add__next__of__kin__inputs__button');
var footerBlock = document.querySelector('.next__of__kin__block > .footer');
var next__of__kin__block = document.querySelector('.next__of__kin__block');
var footer__background = document.querySelector('.next__of__kin__block > .footer__background');
var block__count = true

// Добавляем обработчик события на клик по кнопке
addButton.addEventListener('click', function() {
    
    if (block__count) {
        // Создаем новый элемент div
        var newDiv = document.createElement('div');
        newDiv.className = 'next__of__kin__main__inputs__block';
        newDiv.id = 'next__of__kin__lit__inputs__block__delete';
        next__of__kin__block.style.height = next__of__kin__block.clientHeight + 49 + "px";
        footer__background.style.height = footer__background.clientHeight + 49 + "px";
        newDiv.innerHTML = '<div class="next__of__kin__lit__inputs__block"><input type="text" name="" placeholder="NEXT OF KIN:" class="input__text"><div class="input__line"></div></div><div class="next__of__kin__lit__inputs__block"><input type="text" name="" placeholder="PHONE:" class="input__text"><div class="input__line"></div></div><div class="next__of__kin__lit__inputs__block"><input type="text" name="" placeholder="RELATIONSHIP:" class="input__text"><div class="input__line"></div></div><div class="next__of__kin__lit__inputs__block"><input type="text" name="" style="width: 200px;" placeholder="ADDRESS:" class="input__text"><div class="input__line"></div></div>';
    
        // Добавляем новый элемент к footerBlock
        footerBlock.appendChild(newDiv);
        addButton.innerHTML = "–";
        block__count = false;

    } else {
        var next__of__kin__block__delete = document.getElementById("next__of__kin__lit__inputs__block__delete");
        next__of__kin__block__delete.parentNode.removeChild(next__of__kin__block__delete);
        next__of__kin__block.style.height = next__of__kin__block.clientHeight - 49 + "px";
        footer__background.style.height = footer__background.clientHeight - 49 + "px";
        addButton.innerHTML = "+";
        block__count = true;};});
