''' Create a poll that asks users about what
	there dream vacation is. Display the poll results
	after every user has gone. '''

namePrompt = 'Hello! May I start with your name? '
vacationPrompt = 'If you could go anywhere, where would that be? '

responses = {}

while True:
	name = input(namePrompt)
	location = input(vacationPrompt)
	responses[name] = location
	moreUsers = input("Are you the last in line?"
					  " Yes or No? ")
	print("\n")
	if moreUsers.lower() == 'yes':
		break

print("\n ----POLL RESULTS----")
for name, respose in responses.items():
	print(f"\n {name.title()} would love to visit {respose.title()}!")