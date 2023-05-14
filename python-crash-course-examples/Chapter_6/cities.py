# Make a dictionary called cities with cities as keys
# with dictionaries as the values that share information
# about each city

cities = {
	'denver': {
		'country': 'United States',
		'population': '715,522',
		'fact': 'Denver has 6 professional sports teams'
	},
	'orlando': {
		'country': 'United States',
		'population': '307,570',
		'fact': 'Orlando is home of Universal Studios and Disney World'
	},
	'new york city': {
		'country': 'United States',
		'population': '8,800,000',
		'fact': 'New York was one of the original thirteen colonies that formed the United States'
	}
}

for name, city_info in cities.items():
	print(f'Country, Population, and Fact about {name.title()}')
	country = {city_info['country'].title()}
	population = {city_info['population'].title()}
	fact = {city_info['fact'].title()}
	print(f'\tCountry: {country}')
	print(f'\tPopulation: {population}')
	print(f'\tFact: {fact}')