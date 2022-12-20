
# Create a Dictionry storing the poll results of everyones favorite language

favorite_languages = {
	'jen':'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	'jason': 'java',
	'jordan': 'c'
	}

# Create a list of your friends who took the poll

friends = ['jen', 'edward', 'jason']

# Print statments telling us what everyone's favorite language is

for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}.")

# Using a loop, display all of the participants in the poll

print("\nPeople who participated in the poll:")
for name in favorite_languages.keys():
	print(name.title())

# Using a loop and an if statment, display a message to your friends.

print("\n")
for name in favorite_languages:
	print(f"Hello {name.title()}!")

	if name in friends:
		language = favorite_languages[name].title()
		print(f"\t{name.title()}, I see you love {language}!\n")
	else:
		print('\tThank you for taking the poll!\n')

# Check if Erin took the poll. If not, please ask her too.

if 'erin' not in favorite_languages.keys():
	print('Erin please take our poll.')

# Thank everyone for taking the poll in name order.

print("\n")
for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll!")

# Using a loop, print out all of the languages mentioned in the poll.

print("\nThe following programming languages were mentioned:")
for value in favorite_languages.values():
	print(value.title())

# We can use set() to make sure that we don't return dublicate values

print("\n")
for value in set(favorite_languages.values()):
	print(value.title())