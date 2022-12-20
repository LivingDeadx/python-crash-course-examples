
# Declaring Alien Dictionaries w/ their color and points

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'blue', 'points': 10}

print(alien_0)
print(alien_1)

# Declaring an empty Alien Dictionary and adding Key-Values after

alien_2 = {}

alien_2['color'] = 'red'
alien_2['points'] = 15

print(alien_2)

# Printing each Aliens Key-Value pair

print(alien_0['color'])
print(alien_0['points'])
print(alien_1['color'])
print(alien_1['points'])
print(alien_2['color'])
print(alien_2['points'])

# Modify Aliens Key-Value Pairs

print(f"Alien 0 is {alien_0['color']}")
print(f"Alien 1 is {alien_1['color']}")
print(f"Alien 2 is {alien_2['color']}")

alien_0['color'] = 'red'
alien_1['color'] = 'green'
alien_2['color'] = 'blue'

print(f"Alien 0 is now {alien_0['color']}")
print(f"Alien 1 is now {alien_1['color']}")
print(f"Alien 2 is now {alien_2['color']}")

# Storing a Key-Value pair and displaying by print

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

# Adding an x and y position to the Alien Dictionary

alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_1['x_position'] = 2
alien_1['y_position'] = 25
alien_2['x_position'] = 4
alien_2['y_position'] = 25

print(alien_0)
print(alien_1)
print(alien_2)

# Adding Speed to Aliens

alien_0['speed'] = 'medium'
alien_1['speed'] = 'slow'
alien_2['speed'] = 'fast'

print(alien_0)
print(alien_1)
print(alien_2)

# Moving Alien 0 based on their speed

print(f"Starting X Position of Alien 0 is {alien_0['x_position']}")

if   alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"Alien 0's X Position is now {alien_0['x_position']}") 

# Removing a Key-Value Pair from an Alien

print(alien_1)

del alien_1['points'] # This removes the Key-Valie Pair permanently

print(alien_1)