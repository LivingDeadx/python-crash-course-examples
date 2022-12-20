
# Use a Dictionary to create a Glossary of programming terms and methods

glossary = {
	'.title()': 'Returns string value with the first letter capitalized.',
	'.append()': 'Adds a new value to a list.',
	'.upper()': 'Returns string value with each letter capitalized.',
	'.lower()': 'Returns string value with each letter lower-cased.',
	'Compile': 'Converts code into machine-code in order to be exucuted',
	'CamelCase': 'Practice of typing value names in a style that capitalizes every first letter without spaces or punctuation.',
	'snake_case': 'Practice of typing value names in a style that puts a underscore after every word instead of spaces.',
	'List': 'Collection which is ordered and changeable. Allows duplicate members.',
	'Dictionary': 'Collection of Key-Value pairs which each pair matches a key to its associated value.'
}

# Now print out each entry in the glossary with their meaning

for term, defintion in glossary.items():
	print(f"Term: {term} \n  Definition: {defintion}")
