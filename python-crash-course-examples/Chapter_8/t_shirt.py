""" Define a function that accepts a size and message
	to create a shirt with the size and message to be printed
	on to the t-shirt. """

def create_shirt(size = 'l', message = 'I love python'):
	print(f'Okay. Making a {size.upper()} size shirt'
		  f' with the message "{message}" printed on the front.')

create_shirt()
create_shirt(size = 'm')
create_shirt(message = 'GO NUGGETS')
create_shirt('xl', 'MSU Denver')
create_shirt(size = 'm', message = 'CU Denver')
create_shirt(message = 'CCD', size = 's')