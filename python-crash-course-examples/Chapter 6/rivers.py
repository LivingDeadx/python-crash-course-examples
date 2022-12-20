
# Create a dictionary that includes rivers and the countries that they run through.

rivers = {
	'nile': 'egypt',
	'amazon': 'brazil',
	'yangtze': 'china',
	'yenisei': 'mangolia'
}

# Using a loop, print a statment with the river and the country it belongs in

for river, country in rivers.items():
	print(f"The {river.title()} runs through {country.title()}")

# Using a loop, print out all of the rivers in the dictionary

print("\n")
for river in rivers.keys():
	print(f"{river.title()}")

# Using a loop, print out all of the countries in the dictionary

print("\n")
for country in rivers.values():
	print(f"{country.title()}")