# Name a dictionary called favorite_places and 
# Record a persons 3 favorite places to go

favorite_places = {
	'john': ['denver', 'nashville', 'new york'],
	'gary': ['dallas', 'las vegas', 'phoenix'],
	'kim': ['nashville', 'houstan', 'new orleans'],
	'jason': ['flagstaff', 'hollywood', 'detroit'],
	'jamie': ['chicago', 'miami', 'new england']
}

# Loop through the dictionary and
# and print the data

for name, places in favorite_places.items():
	print(f"\n{name.title()}'s favorite places are:")
	for place in places:
		print(f"\t{place.title()}")
