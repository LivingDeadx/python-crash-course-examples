""" Define a function that takes a city and a country
	and returns a formatted string with the two values.
	Do this for 3 different pairs """

def city_country(city, country):
	formatedCity = f'{city.title()}, {country.title()}'
	return formatedCity

country1 = city_country('Toronto', 'Canada')
country2 = city_country('bangkok', 'thailand')
country3 = city_country('seoul', 'south korea')

print(country1)
print(country2)
print(country3)