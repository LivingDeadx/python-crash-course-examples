""" Create an infinite loop to showcase
	what one looks like """

start = input("Press enter to start the infinite loop: ")
try:
	while True:
		print("CTRL-C to stop")
except KeyboardInterrupt:
	print("Phew, thank you for stopping me...")