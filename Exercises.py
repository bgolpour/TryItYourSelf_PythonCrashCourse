
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

### Page 108
## 6-4. Glossary 2

for key, value in Glossary.items(): 
        print("\nIn Pyhton " + key + "means: " + Glossary[key].title() + ".")

## 6-5. Rivers
rivers = {
        'nile': 'egypt',
        'Chobe': 'Namibia',
        'Congo': 'Republic of Congo',
        'Lawrence': 'canada',
        }
for name, river in rivers.items():
        print("The " + name.title() + " is running through " + river.title() + ".")

## 6-6. Polling
favorite_languages = {
        'jen' : 'python',
        'sarah' : 'c',
        'edward' : 'ruby',
        'phil': 'python'
        }

people = ['jen', 'sarah', 'Judi', 'Jacob']
for name in people:
    # print(name + "Thank you for taking the poll!!")

    if name in favorite_languages:
        print("Dear " + name.title() + " Thank you for taking the poll!!")
    else:
        print(" Dear" + name.title() + " don't forget to take the poll.")

### Page 114
## 6-7. People
people= {
    'Sarah': {
    'first_name': 'sarah',
    'last_name': 'bing',
    'age': 25,
    'city': 'chicago',
    },
    'Jen': {
    'first_name': 'jen',
    'last_name': 'james',
    'age': 35,
    'city': 'charslton',
    },
    'Jesse': {
    'first_name': 'jesse',
    'last_name': 'jackson',
    'age': 45,
    'city': 'denver',
    },
}
for user, user_info in people.items():
    fullname = user_info['first_name'] + " " + user_info['last_name']
    loacation =  user_info['city']
    print("\n Full name: " + fullname.title())
    print("Location: " + loacation.title())

### Page 121
##7-1. Rental Car
message = input("What kind of car you would like today?")
print("\nLet me see if I can find you a Subaru.")

##7-2. Restaurant Seating
number = input("How many people are in your dinner table tonight?")
number = int(number)
if number >8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")

##7-3. Multiple of Ten
number = input("Tell me a number, and I'll tell you it is multiple of 10 or not.")
number = int(number)
if number %10 == 0:
    print("\nThe number: " + str(number) + " is a multiple of ten.")
else:
    print("\nThe number: " + str(number) + " is a multiple of ten.")

### Page 127
## 7-4. Pizza Toppings
prompt = "\nAdd a topping to your pizza."
prompt += "\n(Enter 'quit', If you are finished with toppings.)"

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else: 
        print(topping + " will add to your pizza.")


## 7-5. Movie Tickets
age = input("\nHow old are you?" )
age = int(age)

if age < 3:
    print("The ticket is free for 3 years old and less.")
elif (age >= 3) and (age < 12):
    print("The ticket is $12.")
elif age > 12:
    print("The ticket is $15.")


## 7-6. Three Exits
# Conditional Test


# Active variable
prompt = "\nAdd a topping to your pizza."
prompt += "\n(Enter 'quit', If you are finished with toppings.)"
active = True
while active :
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else: 
        print(topping + " will add to your pizza.")
# Break statement
prompt = "\nAdd a topping to your pizza."
prompt += "\n(Enter 'quit', If you are finished with toppings.)"

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else: 
        print(topping + " will add to your pizza.")


### Page 131
## 7-8. Deli
Sandwich_orders = ['American_sub', 'Beef_on_weck', 'BLT', 'Bologna', 'Cheese_dream']
finished_sandwiches = []
while Sandwich_orders:
    InprocessSandwiches = Sandwich_orders.pop()
    print("I made a: " + InprocessSandwiches.title())
    finished_sandwiches.append(InprocessSandwiches)
print("\n The following are include in Sandwich orders: ")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche)

## 7-9. No Pastrami
Sandwich_orders = ['Pastrami','American_sub','Pastrami','Beef_on_weck','BLT','Bologna','Pastrami','Cheese_dream']
finished_sandwiches = []
# print("The Deli has run out of Pastrami")
while 'Pastrami'in Sandwich_orders:
    Sandwich_orders.remove('Pastrami')
print(Sandwich_orders)

## 7-10. Dream Vacations
prompt = "\n Where the hell you wanna go for the vacation?"
prompt += "\n(Enter 'quit' when you are finished.)"
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'll go to: " + city.title() + "!")

### Page 135
## 8-1. Messages
def display_message(chapter):
    """display sth."""
    print("I learned how to make a function in chapter: " + chapter.title() + ".")
display_message('eight')

## 8-2. Favorite Book
def favorite_book(Book):
    """Anything"""
    print("My favorite book is: " + Book.title() + ".")
favorite_book('Alice in Wonderland')

### Page 141
## 8-3. T-Shirt
# Positional
def make_shirt(size, text):
    """Anything"""
    print("This shirt size is: " + size + " Print this as the text: " + text.upper())
make_shirt('XL', 'I Love Newyork')

# Keyword 
def make_shirt(size, text):
    """Anything"""
    print("This shirt size is: " + size + " Print this as the text: " + text.upper())
make_shirt(size= 'XL', text='I Love Newyork')

## 8-4. Large Shirts
def make_shirt(text, size='Large'):
    """Anything"""
    print("This shirt size is: " + size + "." + " Print this as the text: " + text.upper())
make_shirt(text='I Love Python')

## 8-5. Cities
def describe_city(city, country='Iceland'):
    print(city.title() + " is in " + country.title() + ".")
describe_city('Reykjavik')
describe_city('Tehran', 'Iran')
describe_city(city='Paris', country= 'France')

### Page 146
## 8-6. City Names
def city_country(city, country):
    city_names = city + ' , ' + country
    return city_names.title()

city_country_names = city_country('santiago','chile')
city_country_names = city_country('paris', 'france')
city_country_names = city_country('london', 'britian')
print(city_country_names)

## 8-7. Album
def make_album(artist_name, album_title, number_of_tracks=''):
    music_album = {'artist': artist_name,'title': album_title}
    return music_album
album_made = make_album('bonjovi', 'bounce')
album_made = make_album('guns n roses', 'apetite for destruction')
print(album_made)

## 8-8 User Albums
def make_album(artist_name, album_title):
    music_album = {'artist': artist_name,'title': album_title}
    return music_album
while True:
    print("\nenter the artist name and album title.")
    print("\nenter 'q' to quit.")
    artist_n = input("artist_name: ")
    if artist_n == 'q':
        break
    album_t = input("album_name: ")
    if album_t == 'q':
        break
    album_made = make_album(artist_n, album_t)
    print(album_made)

### Page 150
## 8-9. Magicians
def show_magicians(names):
    print("These are magician's names: ")
    for name in names:
        print("-" + name.title())
names = ['hannah','ty','margot']
show_magicians(names)

## 8-10. Great Magicians
def show_magicians(names):
    for name in names:
        print(name)

def make_great(names):
    print("These are magician's names: ")
    for name in names:
        print("-The Great " + name.title() + ".")
names = ['hannah','ty','margot']
show_magicians(names)
make_great(names[:])

## 8-11. Unchanged Magicians
def show_magicians(names):
    for name in names:
        print(name)

def make_great(names):
    print("These are magician's names: ")
    for name in names:
        print("-The Great " + name.title() + ".")
names = ['hannah','ty','margot']
make_great(names[:])
separate_list = ['not_hana', 'not_ty', 'not_ty']
show_magicians(separate_list)

### Page 154
## 8-12. Sandwiches
def make_sandwich(bread, sauce, *ingrediants):
    print("\nMaking the sandwich with " + bread + " and " + sauce + " which will have: ")
    for ingrediant in ingrediants:
        print( "- " + ingrediant)
make_sandwich('whole wheat bread', 'mayo', 'tuna', 'letucs', 'tomato')
make_sandwich('whole wheat bread', 'mayo', 'tuna', 'letucs')
make_sandwich('whole wheat bread', 'mayo', 'tuna')

## 8-13. User Profile
def my_profile(first, last, **my_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in my_info.items():
        profile[key] = value
    return profile
user_profile = my_profile('Banafshe', 'Golpour', location = 'Toronto', field = 'Python')
print(user_profile)

## 8-14. Cars
def car_info(manufacturer_name, model_name, **optional_features):
    profile = {}
    profile['manu_name'] = manufacturer_name
    profile['mod_name'] = model_name
    for key, value in optional_features.items():
        profile[key] = value 
    return profile

car_profile = car_info('subaru', 'outback', color = 'blue', two_package = 'True')
print(car_profile)

### Page 159
## 8-15. Printing Models
## The solutions are in seprated .py files with related names
## 8-16. Imports
## 8-17. Styling Functions

### Page 166
## 9-1. Restaurant
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name 
        self.cuisine_type = cuisine_type  
    def describe_restaurant(self):
        print("The name of this restaurant is: " + self.restaurant_name.title() + " and they serve: " + self.cuisine_type.title() + ".")
    def open_restaurant(self):
        print(self.restaurant_name.title() + " is now open.")
    
restaurant = Restaurant('Jacobs', 'Steak')
print("This restaurant name is: " + restaurant.restaurant_name + ".")    
print("They serve: " + restaurant.cuisine_type.title() + ".")

restaurant.describe_restaurant()
restaurant.open_restaurant()

## 9-2. Three Restuarants

restaurant_a = Restaurant('Anne Market', 'Italian')
restaurant_a.describe_restaurant()
restaurant_a.open_restaurant()

restaurant_b = Restaurant('Haro', 'Sushi')
restaurant_b.describe_restaurant()
restaurant_b.open_restaurant()

restaurant_c = Restaurant('Oxley', 'anything')
restaurant_c.describe_restaurant()
restaurant_c.open_restaurant()

## 9-3. Users
class User():
    def __init__(self, first_name, last_name, age, weigth, height):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.weigth = weigth
        self.height = height
    def describe_user(self):
        print("The user's full name is: " + self.first_name.title() + ' ' + self.last_name.title())

    def greet_user(self):
        print("Hello Dear " + self.first_name.title())

user_info = User('bax','croft', 15, 45, 150)

user_info.describe_user()
user_info.greet_user()
print(user_info.first_name.title() + " is " + str(user_info.age) + " years old. ")

### Page 171
## 9-4. Number Served
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name 
        self.cuisine_type = cuisine_type 
        self.number_served = 0
    def customers_number(self):
        print("The name of this restaurant is: " + self.restaurant_name.title() + " and they serve: " + str(self.number_served) + " customers.")


restaurant = Restaurant('Jacobs', 'Steak')
restaurant.number_served = 500
restaurant.customers_number()

# Add a method called set_number_served() that lets you set the number of customers that have been served.
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name 
        self.cuisine_type = cuisine_type 
        self.number_served = 0
    def set_number_served(self):
        print("The name of this restaurant is: " + self.restaurant_name.title() + " and they serve: " + str(self.number_served) + " customers.")


restaurant = Restaurant('Jacobs', 'Steak')
restaurant.number_served = 500
restaurant.set_number_served()

# Add a method called increment_number_served() that lets you increment the number of customers who've been served.
    def increment_number_served(self, customers):
        self.number_served += customers

restaurant = Restaurant('Jacobs', 'Steak')
restaurant.increment_number_served(1500)
restaurant.customers_number()

## 9-5. Login Attempts
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.user_login_attempts = 0
    def describe_user(self):
        print("The user's full name is: " + self.first_name.title() + ' ' + self.last_name.title())
    def assess_login_attempts(self):
        print("This user tried " + str(self.user_login_attempts) + " times to login.")

    def update_login_attempts(self, login_attempts):
        self.user_login_attempts = login_attempts

    def increment_login_attempts(self, attempt):
        self.user_login_attempts += attempt

user_info = User('bax','croft')
print(user_info.describe_user())

user_info.update_login_attempts(300)
user_info.increment_login_attempts(1)
user_info.assess_login_attempts()

### Page 178
## 9-6. Ice Cream Stand
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name 
        self.cuisine_type = cuisine_type  
    def describe_restaurant(self):
        print("The name of this restaurant is: " + self.restaurant_name.title() + " and they serve: " + self.cuisine_type.title() + ".")
    def open_restaurant(self):
        print(self.restaurant_name.title() + " is now open.")
    
restaurant = Restaurant('Jacobs', 'Steak')
print("This restaurant name is: " + restaurant.restaurant_name + ".")    
print("They serve: " + restaurant.cuisine_type.title() + ".")

restaurant.describe_restaurant()
restaurant.open_restaurant()

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = []

    def ice_cream_falvors(self):
        print("The ice cream falvors are: " + str(self.flavors) + ".")
flavors_instance = IceCreamStand('Robins','Ice Cream')
flavors_instance.flavors = ['vanilla', 'chocolate', 'black cherry']
flavors_instance.describe_restaurant()
flavors_instance.ice_cream_falvors()

## 9-7.Admin
class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def describe_user(self):
        print("The user's full name is: " + self.first_name.title() + ' ' + self.last_name.title())

    def greet_user(self,first_name, last_name, age):
        print("Hello Dear " + self.first_name.title())

class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = []
    def show_privileges(self):
        print(" -" + str(self.privileges))
admin_instance = Admin('bax', 'croft', 65)
admin_instance.privileges = ['can add post', 'can delete post', 'can ban user']
admin_instance.show_privileges()

### Page 199
## 10-3. Guest
prompt = "Tell me your name."
prompt += "\nenter 'q' for quit"
while True:
    name = input(prompt)
    if name == 'q':
        break
    else:
        filename = 'programming.txt'
        with open(filename, 'a') as file_object:
            file_object.write(name)

## 10-4. Guest Book 

prompt = "And Your name is? " 
prompt += "Enter 'q' to quite"

while True:
    name = input(prompt)

    if name == 'q':
        break
    else:
        filename = 'guest_book.txt'
        with open(filename, 'a') as file_object:
            file_object.write(name)
            print("Dear " + name.title() + " Welcome back!!!")

## 10-5. Programming Poll
prompt = "Tell the reasons why you like programming? "
prompt += "Enter 'q' to quit"

while True:
    answer = input(prompt)
    if answer == 'q':
        break
    else:
        filename = 'all_the_responses.txt'
        with open(filename, 'a') as file_object:
            file_object.write(answer)


### Page 207
## 10-6. Addition
print("Give me two numbers, I will add them up and give you the result.")
print("Enter 'q' to quit.")

while True:
    first_number = input("First_number")
    if first_number == 'q':
        break
    second_number = input("Second_number")
    try:
        sum = int(first_number) + int(second_number)
    except TypeError:
        print("please use numbers instead of text.")
    else:
        print(sum)


## 10-7. Addition Calculator
# same solution as previous question.

## 10-8. Cats and Dogs
filename = 'cats.txt'
try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print("Sorry the file is not excists.")
else:
    print(contents)

## 10-9 Silent Cats and Dogs
filename = 'cats.txt'
try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    pass
else:
    print(contents)

## 10-10 Common Words
filename = 'gutenberg_first.txt'
with open(filename) as file_object:
    content = file_object.read()
    the_counts = content.count('the')
    print(the_counts)


