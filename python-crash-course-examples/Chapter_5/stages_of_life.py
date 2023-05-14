# Create an if-elif-else block that determines a person's stage of life
age = -1
name = 'Finn'
if age < 0:
	print("Please enter a valid age.")
elif age >= 0 and age < 2:
	print(f'{name} is a baby.')
elif age >= 2 and age < 4:
	print(f'{name} is a toddler.')
elif age >=4 and age < 13:
	print(f'{name} is a kid.')
elif age >= 13 and age < 20:
	print(f'{name} is a teenager.')
elif age >= 20 and age < 65:
	print(f'{name} is an adult.')
else:
	print(f'{name} is an elder.')