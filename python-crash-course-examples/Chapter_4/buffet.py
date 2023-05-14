# Create a tuple of buffet foods
buffet_items = ('popcorn chicken', 'potato salad', 'ice cream', 'sushi', 'steak')

# Now using a for loop, print out each of the items
for item in buffet_items:
	print(item.title())

# Try modifying the tuple and see if Python will let you
# buffet_items[0] = 'salmon'

# In order to modify the tuple, it most be over-written. After modifying the tuple, use a for loop to display the items
buffet_items = ('popcorn chicken', 'salmon', 'ice cream', 'pork', 'steak')
for item in buffet_items:
	print(item.title())