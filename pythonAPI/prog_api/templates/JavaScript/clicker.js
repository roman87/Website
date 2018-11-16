const button = document.querySelector(".request")
const close = document.querySelector(".closePopup")
const openmenu = document.querySelector(".openMenu")
const closemenu = document.querySelector(".closeMenu")
button.addEventListener("click", function(){
document.querySelector(".popup").style.display = "flex"
})
close.addEventListener("click", function(){
document.querySelector(".popup").style.display = "none"
})
openmenu.addEventListener("click", function(){
document.querySelector(".menu").style.left = 0
})
closemenu.addEventListener("click", function(){
document.querySelector(".menu").style.left = "-50vw"
})
