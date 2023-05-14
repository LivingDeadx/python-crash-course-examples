# Create some pets and store them in a list

pet1 = {'type': 'dog', 'owner': 'jason'}
pet2 = {'type': 'cat', 'owner': 'jill'}
pet3 = {'type': 'horse', 'owner': 'mary'}
pet4 = {'type': 'cow', 'owner': 'dan'}
pet5 = {'type': 'lizard', 'owner': 'randle'}

pets = [pet1, pet2, pet3, pet4, pet5]

# Loop through the list of pets 
# and display all information about the pets

for pet in pets:
	petType = f"{pet['type'].title()}"
	petOwner = f"{pet['owner'].title()}"
	print(f"The {petType} is owned by {petOwner}.")