""" Write a function that accepts a city with
	the country that it is located in. Print a message
	detailing the information that is given """

def describe_city(city, country = 'united states'):
	print(f"{city.title()} is in {country.title()}.")

describe_city('Orlando')
describe_city('Dallas')
describe_city(city = 'Hokkaido', country = 'Japan')