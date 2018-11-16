let money = window.prompt("Enter the amount of money")
let apples = window.prompt("Enter the number of apples")
let breads = window.prompt("Enter the number of breads")
let pr_apples = window.prompt("Enter the price of one apple") * apples
let pr_breads = window.prompt("Enter the price of one bread") * breads
let z = money >= pr_apples + pr_breads
document.write(z)
