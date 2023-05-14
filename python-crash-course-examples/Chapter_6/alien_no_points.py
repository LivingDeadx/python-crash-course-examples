
# Declare a Alien Dictionary w/o a Key-Value pair for points

alien_0 = {'color': 'green', 'speed': 'slow'}
#alien_0['points'] = 5

# Use the get() method to call for a value that may not exist

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)