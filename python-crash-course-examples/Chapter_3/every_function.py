# Use every function that has been taught in Chapter 3

games = ['Minecraft', 'Dead by Daylight', 'Rocket League', 'Pac-Man', 'Castlevania', 'Unitl Dawn']
print(games)

#.title() prints out an idex of the list with the first letter captializied
print(games[0].title())
print(games[1].title())
print(games[2].title())
print(games[3].title())
print(games[4].title())
print(games[5].title())cdcdcd

#.append adds a new item into the list
games.append('Animal Crossing')
games.append('Forza Motorsport')
print(games)

#.insert() places an item in the list at a certain index
games.insert(2, 'Fortnite')
games.insert(5, 'Final Fantasy')
print(games)

#del will remove any item at the specified index
del games[4]
del games[2]
print(games)

#.pop() pops the last item or specified index off the list and stores it into a variable
popped_game = games.pop()
print(popped_game)
popped_game = games.pop(2)
print(popped_game)
print(games)

#.remove() removes a specific item off the list
games.remove('Minecraft')
print(games)

#sorted() prints the list out in alphabetic order, you can also sort it in reverse alphabetic order with sorted(reverse=True)
print(sorted(games))
print(sorted(games, reverse=True))

#.reverse will completely reverse the list order permanently
games.reverse()
print(games)
games.reverse()
print(games)

#.sort sorts the list in alphabetic order permanently, you can also do .sort(revers=True) to sort the list into reverse alphabetic order
games.sort()
print(games)
games.sort(reverse=True)
print(games)

#len() will give you the length of the list in its current state
games_length = len(games)
print(games_length)
print(len(games))