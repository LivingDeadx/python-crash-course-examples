""" Write a while loop that will tell the user
	the price of a movie ticket depending on the
	age they have inputed """
message = "Please enter an age: "

while True:
	age = input(message)
	if age.lower() == 'quit':
		break
	age = int(age)
	if age < 3 and age >= 0:
		print(f"\nThe movie ticket is Free!")
	elif age > 3 and age < 12:
		print(f"\nThe movie ticket is $10.")
	elif age > 12:
		print(f"\nThe movie ticket is $12.")
