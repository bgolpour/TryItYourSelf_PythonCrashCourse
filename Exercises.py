
### Page 23
message = "Hi Saddeq, Sadegh?!"
print(message)

message = "Stupid change of practice."
print(message)


### Page 29
## 2-3. Personal Message
Message_to_eric = "Hello Eric, would you like to learn some Python today?"
print(Message_to_eric)

## 2-4. Name Cases
name = "Eric"
print(name.upper())
print(name.lower())
print(name.title())

## 2-5. Famous Quote
message = "A person who never made a mistake never tried anything new."
name = "Alber Eintein"
print(name + " once said," + message)

## 2-6. (already done in previous one)
## 2-7. Stripping is total nonesense

### Page 33
## 2-8. Number Eight
print(10-2)
print(5+3)
print(80/10)
print(4*2)

## 2-9. Favoritet Number
f_num = 4
print("my f number is: " + str(f_num) + ".")

### Page 40
## 3-1. Names
names = ["Jack", "Kale", "Sarah", "Daniel"]
print(names[0])
print(names[-1])

## 3-2. Greetings
Greeting = "Happy Quarantin Dear "
for name in names:
    print(Greeting + name.title() + ".\n")

## 3-3. Your Own List
Cars = ['a', 'b', 'c']
for car in Cars: 
    print("I would like to own a " + car + ".\n")

### Page 46
## 3-4. Guest List
guest_list = ['a','b','c']
for guest in guest_list:
    print("Dear " + guest + " just a call would be enough" + ".\n")

## 3-5. Changing Guest List
    print("Dear " + guest + " just a call would be enough" + ".\n")

## 3-6.More Guests
guest_list[0] = 'n'
print(guest_list)
guest_list.append('z')
print(guest_list)

names = ['Nick', 'Jack', 'Mick', 'Sara', 'James', 'Emmet', 'Fargo']
names.insert(2, 'Lara')
print(names)

for name in names:
    print("Dear " + name + " the party is cancelled" + ".\n")
### Page 47
## 3-7. Shrinking Guest List:
# 1
print("I can invite only two people for dinner" + ".\n")
# 2
popped_names = names.pop()
print(popped_names)
print(names)
remained_names = names.remove('Mick')
names.pop()
print(names)
names.pop()
print(names)
names.pop()
print(names)
names.pop()
print(names)
# 3
#### ?
message = "Dear " + str(names) + " u guys r so lucky because u r still invited" + "."
print(message)

# 4
del names[0:2]
print(names)

### Page 50
## 3-8.
# 1
f_places = ['nowhere', 'my_bed', 'mount_st_louis', 'hunted_house']

# 2
print(f_places)

# 3 
print(sorted(f_places))

# 4 (show it is still in original order)
print(f_places)

# 5 (use reverse sorted)
f_places.sorted(reverse=True)
sth = print(sorted(f_places)
sth.reverse()
# 6 (use reverse again)
f_places.reverse()
print(f_places)

# 7 sort
f_places.sort()
print(f_places)

# sort and reverse
f_places.sort(reverse=True)
print(f_places)
### Page 60
## 4-1. Pizzas
# for loop for pizza
pizzas = ['Nick', 'Jack', 'Mick']
for pizza in pizzas:
    print(pizza)
     
# How much I like pizza
for pizza in pizzas:
    print("I like " + pizza + ".\n")
## 4-2. Animals
animals = ['Meimun', 'Shir', 'Shotor']
for animal in animals:
    print(animal.title() + " will make a good pet" + ".\n")
    print(animal.title() + "is calm so it will make a good pet" + ".\n")
### Page 64
## 4-3.
counting_to_twenty = [value**1 for value in range(1,21)]
print(counting_to_twenty)

## 4-4.
One_million = [value for value in range(1,1000000)]
print(One_million)

## 4-5.
min(One_million)
max(One_million)
sum(One_million)

## 4-6.
# Odd Nmbers & Even Numbers.
odd_numbers = list(range(1,21,2))
print(odd_numbers)

even_numbers = list(range(2,21,2))
print(even_numbers)

## 4-7 Threes.
Threes = list(range(1,31,3))
print(Threes)

## 4-8 Cubes.
cubes = []
for value in range(1,10):
    cube = value**3
    cubes.append(cube)
print(cubes)

## 4-9 Cube Comprehension.
cubes = [value**2 for value in range(1,11)]
print(cubes)

### Page 69
## 4-10. Slices
# First Three items
names = ['a', 'b', 'c', 'd', 'e']
print("The first three items of the list are: ")
for name in names[:3]:
    print(name.title())

# Three items from the middle
print("The three items from the middle of the list are: ")
for name in names[1:3]:
    print(name.title())    

# Last three items
print("These are three last items of the list: ")
for name in names[-3:]:
    print(name.title())

## 4-11 My Pizzas, Your Pizzas
# Make a copy
my_pizzas = ['a', 'b', 'c', 'd', 'e']
# Make a copy
friends_pizzas = my_pizzas[:]
print(friends_pizzas)

# Add a new pizza
friends_pizzas.append('z')
print(friends_pizzas)

# Add another pizza
friends_pizzas.append('s')

# Prove that you have two separate lists. 
print("My favorite pizzas are: ")
for value in my_pizzas:
    print(value.title())
print("My friends' favorites are: ")
for value in friends_pizzas:
    print(value.title())

### Page 71
five_simple_foods = ('a', 'b', 'c', 'd', 'e')
# for loop to print each
for food in five_simple_foods:
    print(food)

# Try modify and get rejected 
five_simple_foods[0] = 'z'

# Changing the menue
five_simple_foods = ('x', 'y', 'z')
print("\nthe new menue is: ")
for value in five_simple_foods:
    print(value)

###  Page 82
## 5-1. 
cars = ['bmw']
for car in cars: 
    if car == 'benz':
        print("Is it a bmw? I predict True.")
    else:
        print(" I predict False")
## Create at least 10 tests
# 1
right_anwser = 25
if right_anwser != 25:
    print("That is not the correct answer. Please try again!")
else:
    print("Good Job!!")
# 2
age_0 = 12
age_1 = 25
if (age_0>11) and (age_1>24):
    print("True")
else:
    print("False")

# 3 
banned_users = ['a', 'b', 'c']
user = 'z'
if user not in banned_users:
    print(user.title() + "You may put comment.")
else:
    print(user.title() + "you are banned from any conversation.")

# 4 
car_1 = 'bmw'
car_2 = 'benz'
if car_1 == 'audi' or car_2 == 'porsch':
    print("sth")
else:
    print("something else")

# 5
age = 19
if age >= 18:
    print("You are old enough to vote.")

### Page 88 
## 5-3. Alien Colors #1:
# If the alien's color is green.
alien_color = ["green"]
if 'green' in alien_color:
    print("You earned 5 points.")

# Write one version that passes the if test and another that fails.(The version that fails will have no output.)
alien_color = ['green']
if 'green' in alien_color:
    print("You earned 5 points.")
elif 'blue' in alien_color:
    print("You earned 5 points.")

## 5-4. Alien Colors #2: Choose a color for an alien and write an if-else chain.
# If the alien's color is green, print a statement that the player just earned 5 points.
alien_color = ['green']
if 'green' in alien_color:
    print('You earned 5 points.')

# If the alien's color is not green.
alien_color = ['blue']
if 'green' in alien_color:
    print('You earned 5 points.')
if 'green' not in alien_color:
    print('You just earned 10 points.')

# Write one version that runs the if (which we did), and another that runs the else block.
alien_color = ['blue']
if 'green' in alien_color:
    print('You earned 5 points.')
else:
    print("Feel free to try again.")

## 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
# If the alien is green, print you earned 5 points.
alien_color = ['green', 'red', 'yellow']
if 'green' in alien_color:
    print('You earned 5 points.')
elif 'yellow' in alien_color:
    print('You earned 10 points.')
else:
    print('You earned 15 points.')

# If yellow you earne, 10 points.
alien_color = ['black', 'red', 'yellow']
if 'green' in alien_color:
    print('You earned 5 points.')
elif 'yellow' in alien_color:
    print('You earned 10 points.')
else:
    print('You earned 15 points.')

# If red you earne, 15 points.
alien_color = ['black', 'red', 'gray']
if 'green' in alien_color:
    print('You earned 5 points.')
elif 'yellow' in alien_color:
    print('You earned 10 points.')
else:
    print('You earned 15 points.')

## 5-6. Stages of Life: Write an if-elif-else chain that determines a person's stage of life. Set a value for the variable age, and then:
# If the person is less than 2 years old, print, person is a baby.
 age = 2
if age < 2:
    print("You are a Baby!")
elif age >=2 and age <4:
    print("You are a Toddler!")
elif age >=4 and age <13:
    print("You are a Kid!")
elif age >=13 and age <20:
    print("You are a Teenager!")
elif age >=20 and age >65:
    print("You are a Adult!")
elif age > 65:
    print("You are and Elder")

## 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statement that check for certain fruits in your list.
favoriteFruits = ['apple', 'orange', 'banana']
if 'apple' in favoriteFruits:
    print("Eat an apple a day keeps the doctor away.")
elif 'orange' in favoriteFruits:
    print('We pack the juice')
elif 'banana' in favoriteFruits:
    print('You really like the banana.')

### Page 93
## 5-8. Hello Admin. Male a list of five or more username, including the name 'admin'. 
# If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?

for usernames in usernames:
    if 'admin' in usernames:
        print("Hello Admin, do you like to see a status report?")
# Otherwise, print a generic greeting for everyone, such as Hello...
usernames = ['admin', 'santiago', 'pesarak', 'shangule', 'hooman']
admin_username = ['admin']
for usernames in usernames:
    if admin_username in usernames:
        print("Hello Admin, do you want to see a status report?")
    else:
        print("Hello" + usernames + "thank you for logging again.")

## 5-9. No Users. Add an if test to hello admin to make sure the list of users is not empty.
# If the list is empty, print the message, we need to find some users!
users = []
if users:
    for users in users:
        print("Thank you for logging again.")
else: 
    print("We need to find some users!")

## 5-10. Checking Usernames:
# Make a list of five or more usernames called current_users.
# Make another list of five or more usernames called new_users.
# Loop throgh the new_users list to see if each new username has already been used. Print message in both conditions.
current_users = ['admin', 'santiago', 'pesarak', 'shangule', 'hooman']
new_users = ['admin_1', 'admin_2', 'santiago', 'pesarak', 'shangule', 'hooman']
for new_user in new_users:
    if new_user in current_users:
        print("You need to enter a new username.")
    else:
        print("This username is available")

## 5-11. Ordinal Numbers.
# Store the numbers 1 through 9 in a list.
# Loop through the list.
# Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number.
ordinal_numbers = ['1st','2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th']
first_three = ['1st','2nd', '3rd']
the_rest = ['4th', '5th', '6th', '7th', '8th', '9th']
for first_three in first_three:
    if first_three in ordinal_numbers:
        print("For the first 3 the correct ordinal ending is st, nd, rd")
for the_rest in the_rest:
    if the_rest in ordinal_numbers:
        print("For the rest the correct ordinal ending will take th at the end.")
### Page 102
## 6-1. Person
Sarah = {
    'first_name': 'sarah',
    'last_name': 'bing',
    'age': 25,
    'city': 'chicago',
}
print("Sarah's last name is: " + Sarah['last_name'].title() + ".")
print("She is from " + Sarah['city'].title() + ".")
print("And she is " + str(Sarah['age']) + " years old ")

## 6-2. Favorite Numbers.
Favorite_Numbers = {
    'Jame': 25,
    'Jesse': 35,
    'Jack': 45,
    'Joi': 55,
}
print("Jack's favorite number is " + str(Favorite_Numbers['Jack']) + ".")

## 6-3. Glossary
Glossary  = {
    'Boolean': 'conditional test',
    'percentage': 'remainder operator',
    'tuples': 'unchangeable list',
    'statement': 'complete line of code',
    'expression': 'any section of the code that evaluates to a value',
}
print("\nIn Pyhton Boolean means: " + Glossary['Boolean'] + ".")
print("\nIn Pyhton percentage sign means: " + Glossary['percentage'] + ".")
print("\nIn Pyhton tuples means: " + Glossary['tuples'] + ".")
print("\nIn Pyhton statement  means: " + Glossary['statement'] + ".")
print("\nIn Pyhton expression means: " + Glossary['expression'] + ".")