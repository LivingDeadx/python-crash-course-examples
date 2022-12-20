
# Create a Dictionary to store data from a poll asking people what their favorite numbers are

favorite_numbers = {
	'john': 34,
	'rayman': 9,
	'leah': 21,
	'lexi': 87,
	'shyla': 2
}

# Print out statments that tell what each persons favorite number is
for person in favorite_numbers:
	print(f"{person.title()}'s favorite number is {favorite_numbers[person]}.")