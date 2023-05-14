""" Define a function named make_album() that builds
	a dicitionary for an album. Use this function to make
	3 different album entries. """

def make_album(artist_name, album_name, num_of_songs = None):
	album = {'Artist': artist_name.title(), 'Album': album_name.title()}

	if num_of_songs:
		album['Songs'] = num_of_songs

	return album

album1 = make_album('nirvana', 'nevermind')
album2 = make_album('papa roach', 'infest', 13)
album3 = make_album('2Pac', 'all eyes on me')

print(album1)
print(album2)
print(album3)
