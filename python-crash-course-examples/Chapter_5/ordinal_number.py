# Store the numbers 1 to 9 in a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Loop through the numbers list and turn them into ordinal numbers
for num in numbers:
	if num == 1:
		print(f'{num}st')
	elif num == 2:
		print(f'{num}nd')
	elif num == 3:
		print(f'{num}rd')
	elif num >= 4 and num <= 9:
		print(f'{num}th')