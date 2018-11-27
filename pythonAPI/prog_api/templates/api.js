let url = "http://127.0.0.1:5000/"
let xhr = new XMLHttpRequest()
xhr.open("GET", url, false)
xhr.send()
setTimeout(() => {
}, 100)
let data = JSON.parse(xhr.responseText)
const elem = document.getElementById("main1")
function display(element){
title = element.title
elem.insertAdjacentHTML("beforeend", "<button>" + title + "</button><input class='edit' type='button' value='Edit'><input class='delete' type='button' value='Delete'><br /><br />")
}
data.forEach(display)


let arr = Array.from(document.getElementsByTagName("button"))
let arr1 = Array.from(document.getElementsByClassName("edit"))
let arr2 = Array.from(document.getElementsByClassName("delete"))
let data_article

function click_article(i){
arr[i].onclick = function(){
url_article = data[i - 1].url_article
xhr.open("GET", url_article, false)
xhr.send()
setTimeout(() => {
}, 100)
data_article = JSON.parse(xhr.responseText)
document.getElementById("title_article").innerHTML = data_article.title
document.getElementById("text_article").innerHTML = data_article.text
}
}

let title_update
let text_update
function edit_article(j){
arr1[j].onclick = function(){
id = data[j].id
title_update = document.getElementById("title_update").value
text_update = document.getElementById("text_update").value
fetch(url, {
method: "PUT",
headers: {
"Content-Type": "application/json; charset=utf-8"
},
body: JSON.stringify({"title_update": title_update, "text_update": text_update, "id": id})
})
.then(response => response.json())
}
}

function delete_article(k){
arr2[k].onclick = function(){
id = data[k].id
fetch(url, {
method: "DELETE",
headers: {
"Content-Type": "application/json; charset=utf-8"
},
body: JSON.stringify({"id": id})
})
.then(response => response.json())
}
}

for (i = 1; i < arr.length - 1; i++){
click_article(i)
}
for (j = 0; j < arr1.length; j++){
edit_article(j)
}
for (k = 0; k < arr2.length; k++){
delete_article(k)
}


let title_p
let text_p
document.getElementById("pa").onclick = function (){
title_p = document.getElementById("title_send").value
text_p = document.getElementById("text_send").value
fetch(url, {
method: "POST",
headers: {
"Content-Type": "application/json; charset=utf-8"
},
body: JSON.stringify({"title": title_p, "text": text_p})
})
.then(response => response.json())
}
