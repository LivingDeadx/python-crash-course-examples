# Create a list of your favorite pizzas
pizzas = ['Cheese', 'Hawaiian', 'Pepperoni']

# Create a for loop that displays all pizzas in the list
for pizza in pizzas:
	print(pizza)

print('\n')

# Create a for loop that displays a sentence with the pizza in the list
for pizza in pizzas:
	print(f"{pizza} is my one of my top 3 favorite pizzas!")
print('\n')
# Create a for loop and then at the end of the loop add a sentence that displays only once
for pizza in pizzas:
	print(f"{pizza} is my one of my top 3 favorite pizzas!")
print('I really love pizza!')

print('\n')

#Using the split method, make a copy of the pizzas list.
friends_pizzas = pizzas[:]

# Now add a new pizza to the orginal list and one to the new copied list
pizzas.append('Sausage')
friends_pizzas.append('Stuffed Crust')

# Now using a for loop, display your favorite pizzas and your friends favorite pizzas
print('My favorite pizzas are:')
for pizza in pizzas:
	print(f'\t{pizza}')

print('\n')

print('My friends favorite pizzas are:')
for pizza in friends_pizzas:
	print(f'\t{pizza}')
