
# Create a Dictionary to store data from a poll asking people what their favorite numbers are

favorite_numbers = {
	'john': [34, 21, 23, 18],
	'rayman': [9, 12, 98, 27],
	'leah': [21, 34, 76, 45],
	'lexi': [87, 31, 54, 42],
	'shyla': [2, 1, 5, 4]
}

# Print out statments that tell what each persons favorite number is
for person, numbers in favorite_numbers.items():
	print(f"\n{person.title()}'s favorite numbers are:")
	for number in numbers:
		print(f"\t{number}")