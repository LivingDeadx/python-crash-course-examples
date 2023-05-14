users = {
	'HoodedGhost': {
		'first': 'billy',
		'last': 'loomis',
		'location': 'woodsboro'
	},

	'WhiteMaskShape': {
		'first': 'michael',
		'last': 'myers',
		'location': 'haddonfield'
	},

	'BurnedNightmare': {
		'first': 'freddy',
		'last': 'kruger',
		'location': 'elm street'
	},

	'HockeyMaskKiller81': {
		'first': 'jason',
		'last': 'voorhees',
		'location': 'crystal lake'
	}
}

for username, user_info in users.items():
	print(f"\nUsername: {username}")
	full_name = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']

	print(f"\tFull Name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")