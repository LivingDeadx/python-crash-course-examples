
# Copy the dictionary from the favorite_languages example

favorite_languages = {
	'jen':'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	'jason': 'java',
	'jordan': 'c'
	}

# Now make a list of people who should take the poll, including some who have already taken the poll

polling = ['jen', 'edward', 'mike', 'nathan', 'joe', 'jason', 'mary']

# Now loop through the list. If they have taken the poll, thank them. If they have not taken the poll, invite them to take the poll.

for name in polling:
	if name in favorite_languages.keys():
		print(f"{name.title()}, thank you for taking the poll!\n")
	else:
		print(f"{name.title()}, would you like to take our poll?\n")