# Create a list of usernames including the name admin
#usernames = ['GodRay23', 'DunkinCoffee3', 'LivingDead', 'admin', 'FlawlessClaw34']
usernames = []
# Create a loop that greets every user, admind gets asked a special message.
# Make sure to check if the list is empty.
if usernames:
    for user in usernames:
	    if user == 'admin':
		    print("Hello admin, would you like to see a status report?")
	    else:
		    print(f"Hello {user}, it is nice to see you again!")
else:
	print("We need to find some users!")		   