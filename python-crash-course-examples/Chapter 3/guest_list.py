# Create a guest list of people to invite to dinner
guests = ['Chris Pratt', 'Peyton Manning', 'Michael Chandler']
invited_guests = len(guests)
print(f'There are {invited_guests} people on the guest list.\n')
# Create the message that will be sent out to all the invited guests
message = ", you have been invited for a special evening dinner at the Diamand Manor."
# Send out the messages addressed to the guests
print(f'{guests[0]}{message}')
print(f'{guests[1]}{message}')
print(f'{guests[2]}{message}\n')

print('Peyton Manning will not be able to attend the dinner.')

# Remove Peyton Manning from the list and invite another guest in his place
guests[1] = 'Russell Wilson'

invited_guests = len(guests)
print(f'\nThere are {invited_guests} on the guest list.\n')

#Resend the messages
print(f'\n{guests[0]}{message}')
print(f'{guests[1]}{message}')
print(f'{guests[2]}{message}\n')

print('Sir we have found a bigger table, we can invte three more guests!\n')

# Add 3 more guests to the list and resend the messages out
guests.insert(0, 'Chris Evans')
guests.insert(2, 'Tom Cruise')
guests.append('Michael Myers')

invited_guests= len(guests)
print(f'There are {invited_guests} people on the guest list.\n')

print(f'{guests[0]}{message}')
print(f'{guests[1]}{message}')
print(f'{guests[2]}{message}')
print(f'{guests[3]}{message}')
print(f'{guests[4]}{message}')
print(f'{guests[5]}{message}')

print('\nSir our new table will not arrive in time!\n')

#Pop guests off the list until only to remain.
poppedguest = guests.pop()
print(f'Sorry {poppedguest}, we will not have enough room for you at dinner')
poppedguest = guests.pop()
print(f'Sorry {poppedguest}, we will not have enough room for you at dinner')
poppedguest = guests.pop()
print(f'Sorry {poppedguest}, we will not have enough room for you at dinner')
poppedguest = guests.pop()
print(f'Sorry {poppedguest}, we will not have enough room for you at dinner')

print('\nSir we can still invite that last two guests on the list!\n')

#Now let the last two people on the list know that they are still invited to dinner, removing them from the list.
poppedguest = guests.pop()
print(f'{poppedguest} you are still invited to dinner!')
poppedguest = guests.pop()
print(f'{poppedguest} you are still invited to dinner!')