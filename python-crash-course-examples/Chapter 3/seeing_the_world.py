#Create a list of 5 places that you want to visit and print it
places = ['Australia', 'Sweeden', 'London', 'Tokyo', 'Egypt']
print(places)

#Now sort the list without modifying the orginal list
print(sorted(places))

#Print the orginal list to make sure it hasn't been modified
print(places)

#Now sort the list in reverse order with out modifying the orignal list
print(sorted(places, reverse=True))

#Again, show that the orginal list has not been modified
print(places)

#Now lets revere the original order of the list, then reverse back to normal
places.reverse()
print(places)
places.reverse()
print(places)

#Now lets sort the list in alphabetic order, then put it in reverse alphabetic order
places.sort()
print(places)
places.sort(reverse=True)
print(places)