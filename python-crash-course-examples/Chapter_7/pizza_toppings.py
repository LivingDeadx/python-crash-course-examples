""" Create a While loop that asks the user
	to input a series of toppings that they
	would like on their pizza. Quit the loop
	once they input 'quit' """
print("What toppings would you like on your pizza?")

active = True
toppings = []
count = 0
while active:
	topping = input()
	if topping.lower() == "quit":
		print(f"\nOkay I added the following toppings to your pizza:")
		for ingredient in toppings:
			count = count + 1
			print(f"{count}. {ingredient}")
		active = False
	else:
		toppings.append(topping.title())
		print(f"Okay I will add {topping.title()} to your pizza.")