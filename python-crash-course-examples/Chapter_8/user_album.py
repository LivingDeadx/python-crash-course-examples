""" Using the function from album.py, let the user
	create albums using the funciton """

def make_album(artist_name, album_name, num_of_songs = None):
	album = {'Artist': artist_name.title(), 'Album': album_name.title()}

	if num_of_songs:
		album['Songs'] = num_of_songs

	return album

while True:

	print("What album is your favorite? (Press 'q' to stop anytime)")

	artist_name = input('Artist Name?: ')

	if artist_name == 'q':
		break

	album_name = input('Album Name?: ')

	if album_name == 'q':
		break

	num_of_songs = input('Number of Songs? (This is optional): ')

	if num_of_songs == 'q':
		break

	if num_of_songs == '':
		num_of_songs = None
	else:
		num_of_songs = int(num_of_songs)

	print(make_album(artist_name, album_name, num_of_songs))

	countinue = input('Would you like to add another? (Y/N?): ')

	if countinue.lower() == 'n':
		break 