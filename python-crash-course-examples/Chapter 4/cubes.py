# Create a list of cubes from 1 - 10 using for loops and display each value of the list.
cubes = []

for value in range(1, 11):
	cubes.append(value**3)

for cube in cubes:
	print(cube)