let names = [
	[
		['куры', 'гуси', 'павлины'],
		['сокол', 'орел', 'соловей']
	],
	[
		['собака', 'кошка'],
		['обезьяна', 'рысь']
	]
]
for(group of names){
for(animals of group){
for(animal of animals){
console.log(animal)
}
}
}
