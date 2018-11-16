//const button = document.getElementsByTagName("button")[0]
//let url = "http://127.0.0.1:5000/1"

window.location = "http://127.0.0.1:5000/1"
let url = "http://127.0.0.1:5000/1"
let xhr = new XMLHttpRequest()
xhr.open("GET", url, true)
xhr.send()
let data
setTimeout(function(){data = JSON.parse(xhr.responseText)
console.log(data)
document.write("<h3>Hi</h3> <p>Roman</p>")
let elem1 = document.getElementsByTagName("h3")[0]
let elem2 = document.getElementsByTagName("p")[0]
elem1.innerHTML = data.title
elem2.innerHTML = data.text
}, 100)

//let xhr = new XMLHttpRequest()
//xhr.open("GET", url, true)
//xhr.send()
//let data = JSON.parse(xhr.responseText)
//console.log(data)


