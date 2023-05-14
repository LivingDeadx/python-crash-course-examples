# Ask the user for a number to be tested
# if it is a multiple of 10

num = input("Can you name a number " 
			"that is a multiple of 10? ")
if num == '':
	num = int(0)
else:
	num = int(num)

# Test to see if the user input is a
# multiple of 10, if not display that the
# number is not a multiple of 10, if it input
# is display the number is a multiple of 10.

if num % 10 == 0:
	print(f"\n{num} is a multiple of 10!")
else:
	print(f"\n{num} is a not multiple of 10!")