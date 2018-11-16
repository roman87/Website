document.getElementsByTagName("body")[0].setAttribute("style", "background-color:" + prompt("Какой будет фон у страницы?"));
document.querySelectorAll(".page")[0].setAttribute("style", "color:" + prompt("Какой будет цвет текста на странице?"));
document.querySelectorAll(".name")[0].innerHTML = prompt("Как зовут человека, который вас вдохновляет");
document.getElementsByTagName("img")[0].src = prompt("Введите адрес картинки");
let text = document.querySelectorAll(".shortBio")[0];
text.innerHTML = prompt("Введите текст страницы");
text.class += " animated";
