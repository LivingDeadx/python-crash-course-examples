""" Make a list called sandwich_orders. Loop through this 
	list and print out a statement informing that each sandwich
	is being made while storing the finished sandwiches in a list
	called finished_sandwiches. Print out a statment at the end 
	stating each sandwhich that was made. Make sure that there is
	no pastrami sandwiches in the order list."""

sandwich_orders = ['b.l.t', 'pastrami', 'ham and cheese', 'pastrami',
				   'peanut butter & jelly', 'pastrami', 'tuna']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	currentOrder = sandwich_orders.pop()
	print(f"\nCreating {currentOrder.title()}...")
	finished_sandwiches.append(currentOrder)

print(f"\nThe following sandwiches were made:")
count = 0
for sandwich in finished_sandwiches:
	count = count + 1
	print(f"{count}. {sandwich.title()}")