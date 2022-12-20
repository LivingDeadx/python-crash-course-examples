# Create a two lists of 5 current users and new users
current_users = ['GodRay23', 'DunkinCoffee3', 'LivingDead', 'HaltingFire65', 'FlawlessClaw34']
new_users = ["FireflyWarrior", "GodRay23", "GolemParty2", "LivingDead", "HaltingFire65", 'BlocksofWater']

# Using if statements and for loops, ensure that usernames are unique
lower_current = []

for user in current_users:
	lower_current.append(user.lower())

print(lower_current)

for user in new_users:
	if user.lower() in lower_current:
		print(f'The username, {user}, is not available. Please try another username.\n')
	else:
		print(f'The username, {user}, is available.\n')