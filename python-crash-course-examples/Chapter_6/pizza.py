pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],	
}

print(f"You ordered a {pizza['crust']}-crust pizza"
		"with the following toppings:")

listNum = 0;
for topping in pizza['toppings']:
	listNum = listNum + 1
	print(f"\t{listNum}. {topping.title()}")
