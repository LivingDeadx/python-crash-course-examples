# Create a list of 3 animals that all have something in common
feline_animals = ['panther', 'tiger', 'leopard']

# Create a for loop that displays the each of the 3 items in the list
for feline in feline_animals:
	print(feline.title())

print('\n')

# Create a for loop that displays a sentence about each of the items in the list
for feline in feline_animals:
	print(f'{feline.title()} is just a really big cat!')

print('\n')

# Create a for loop that displays a sentence and display a single sentence at the end of the loop
for feline in feline_animals:
	print(f'{feline.title()} live in the wild.')
print('All of these animals are felines!\n')

# Adding more felines to the list
feline_animals.append('lion')
feline_animals.append('lynx')
feline_animals.append('cheetah')

# Using a slice, display the first 3 items of the list
print(f'The first 3 items of the list are:')
for feline in feline_animals[:3]:
	print(f'\t{feline.title()}')

print('\n')

# Using a slice, print out three items that are in the middle of the list
print(f'The animals in the middle are:')
for feline in feline_animals[1:5]:
	print(f'\t{feline.title()}')

print('\n')

# Using a slice, print the last three items of the list
print(f'The animals at the end of the list are:')
for feline in feline_animals[-3:]:
	print(f'\t{feline.title()}')