# Write a 10 conditional tests, 5 true and 5 false and print out a statement describing the test and the prediction of the test
car = 'subaru'
print("Is car == 'subaru'? I predict that it is true!")
print(car == 'subaru')

print("\nIs car =='audi'? I predict that it is false!")
print(car == 'audi')

team = 'broncos'
print("\nIs team == 'broncos'? I predict that it is true!")
print(team == 'broncos')

print("\nIs team == 'ravens'? I predict that it is false!")
print(team == 'ravens')

super_hero = 'spider-man'
print("\nIs super_hero == 'spider-man'? I predict that it is true!")
print(super_hero == 'spider-man')

print("\nIs super_hero == 'thor'? I predict that it is false!")
print(super_hero == 'thor')

holiday = 'halloween'
print("\nIs holiday == 'halloween'? I predict that it is true!")
print(holiday == 'halloween')

print("\nIs holiday == 'easter'? I predict that it is false!")
print(holiday == 'easter')

movie = 'minions'
print("\nIs movie == 'minions'? I predict that it is true!")
print(movie == 'minions')

print("\nIs movie == 'top gun'? I predict that it is false!")
print(movie == 'top	gun')

# Conditional Tests with the lower() method
game = 'MineCraft'
print("\nIs game == 'minecraft'? I predict that it is false!")
print(game == 'minecraft')

print("\nIs game.lower() == 'minecraft'? I predict that it is true")
print(game.lower() == 'minecraft')

# Numerical Conditional Tests
age = 21
print("\nIs age == 21? I predict that it is true!")
print(age == 21)

print("\nIs age == 18? I predict that it is false!")
print(age == 18)

print("\nIs age < 20? I predict that it is false!")
print(age < 20)

print("\nIs age > 20? I predict that it is true!")
print(age > 20)

print("\nIs age >= 21? I prdict that it is true!")
print(age >= 20)

print("\nIs age <= 21? I predict that it is true!")
print(age <= 21)

# Conditional Test using the keywords and & or
age_0 = 23
age_1 = 20
print("\nIs age_0 == 23 and age_1 == 20? I predict that it is true!")
print(age_0 == 23 and age_1 == 20)

print("\nIs age_0 == 23 and age_1 == 21? I predict that it is false!")
print(age_0 == 23 and age_1 == 21)

print("\nIs age_0 == 22 or age_1 == 20? I predict that it is true!")
print(age_0 == 22 or age_1 == 20)

print("\nIs age_0 == 22 or age_1 == 18? I predict that it is false!")
print(age_0 == 22 or age_1 == 18)

# Conditional Test if an item is in a list
toys = ['football', 'lego', 'moon sand', 'silly putty']
print("\nIs 'lego' in toys? I predict that is is true!")
print('lego' in toys)

print("\nIs 'slime' in toys? I predict that is it false!")
print('slime' in toys)