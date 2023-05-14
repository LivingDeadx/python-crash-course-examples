
# Create a dicitionary of 3 People, then store in a list

person1 = {'first name': 'Rocky', 'last name': 'Balboa', 'age': 30, 'city': "Philadelphia" }
person2 = {'first name': 'Jamal', 'last name': 'Murray', 'age': 26, 'city': "Denver" }
person3 = {'first name': 'Mario', 'last name': 'Jumpman', 'age': 42, 'city': "The Mushroom Kingdom" }

people = [person1, person2, person3]

# Print out each Ker-Value pair for every person

for person in people:
	for key, value in person.items():
		print(f"{key.title()}: {value}")
	print("\n")