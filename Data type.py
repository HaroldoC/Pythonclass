""" # Fundamental Data Types
integers - Are numbers 2, 4, 5
float - a floating point number ex: 0.5
bool
str
list
tuple
set
dict
type - what data type 
# Classes -> Custom Types


# Specialized Data Types

None 

"""

# Fundamental Data Types

# print(type(2 + 4))
# print(type(2 - 4))
# print(type(2 * 4))
# print(type(2 / 4))

# print(2**3)
# print(2 // 4)
# print(5 % 4)

# Math Functions

# print(round(3.1))
# print(abs(-32))

# Operator precedence

# print(20 - 3 * 4)

# First ()
# **
# * /
# + -

# complex numbers
# complex
# Binary number
# print(bin(5))
# print(int("0b101", 2))

# Variables - store info that can be used in the programs

# user_iq = 190
# user_age = user_iq / 4
# print(user_age)


# sanke_case
# Start with lowercase or underscore
# Letters, Numbers, Underscores
# Case sensitive
# Don't overwrite keywords

# constatnts
# PI = 3.14

# DUNTHER __

# print(type(20.0 + 25.0))

# expression vs statment
# expression - produces a value
# statment - the whole body of code - action

# iq = 100
# user_age = iq / 5

# augmented assignment operator - +=/ -=/ *=

# some_value = 5
# some_value += 2
# some_value = some_value + 2
# print(some_value)


# strings - a pice of text

# "hi helooo"
# print(type("hi helooo"))

# username = "supercoder"
# password = "supersecret"
# long_string = """
# wow
# o o
# ---

# print(long_string)

# first_name = "Haroldo"
# last_name = "Carvalho"
# full_name = first_name + " " + last_name
# print(full_name)

# string concatenation - adding strings together

# print("Hello" + " Haroldo")

# type conversion

# a = str(100)
# b = int(a)
# c = type(b)
# print(c)

# escape sequence

# weather = "\t It\'s\ "kind of\" sunny"

# formatted strings

# name = "Johnny"
# age = 43
# print("Hi " + name + ". You are " + str(age) + " years old")
# print(f"Hi {name}. You are {age} years old!")

# string indexes

# selfish = "me me me"
#  01234567

# [start:stop:stepover]
# [-1] - start at the end
# print(selfish[0])

# immutability - the value does not change

# built-in-functions + methods
# len - means calculating the lenth
# greet = "hellloooo"
# print(greet[0 : len(greet)])
# quote = "to be or not ot be"
# print(quote.upper())

# booleans - bool - means true or false
# name = 'Haroldo'
# is_cool = False
# is_cool = True

# Exerceise type conversion

# name = "Haroldo"
# relationship_status = "single"

# birth_year = input("What year were you born?")
# age = 2023 - int(birth_year)
# print(f"your age is: {age}")


# birth_year = 1980
# age = 2023 - birth_year
# print(f"your age is: {age}")


# Exercise password

# input("Haroldo")
# input("secret")

# print("{username}, your passaword {******} is {6} letters long")

# username = input("what is your username? ")
# password = input("what is your password? ")

# password_length = len(password)
# hidden_password = "*" * password_length

# print(
#    f"{username}, your password, {hidden_password}, is {password_length} letters long. "
# )


# list - Order sequence of objects - a form of array

# li = [1, 2, 3, 4, 5]
# li2 = ["a", "b", "c"]
# li3 = [1, 2, "a", True]


# Data Structure - a way to organize our code
# list slicing
# amazon_cart = ["notebooks", "sunglasses", "toys", "grapes"]
# amazon_cart[0] = "laptop"
# new_cart = amazon_cart[0:3]
# print(new_cart)
# print(amazon_cart)


# matrix - to describe multidimentional lists
# matrix = [[1, 2, 3], [2, 4, 6], [7, 8, 9]]
# print(matrix[0][1])
# comes up a lot on machine learning


# list method
# basket = [1, 2, 3, 4, 5, 8, 12, 3, 5]


# adding
# basket.insert(4, 100)
# basket.extend([100, 122])
# new_list = basket
# print(new_list)


# removing method
# basket.pop()
# basket.remove(3)
# basket.clear()
# keyword
# print(2 in basket)
# print(basket.count())
# basket.sort()
# sorted()
# basket.reverse()
# print(basket)

# print(list(range(1, 100)))

# sentence = ""
# new_sentence = sentence.join(["Hello", " I am ok"])
# print(new_sentence)


# List unpacking

# a, b, c, *other = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(other)


# Dictionary
# dict
# user = {"a": [1, 2, 3], "b": "hello", "age": [23]}

# user2 = dict(name='jonny')
# print(user.get("age"))


# Tuple - are like list but imutable

# my_tuple = (1,2,3,4,5)
# print(my_tuple[1])


# Set - simply unorder colection of unique objects

# my_list = [1, 2, 3, 4, 5]
# print(my_list[1])
# my_set = {1, 2, 3, 4, 5}
# my_set.add(100)
# print(my_set)

# my_set = {1, 2, 3, 4, 5}
# your_set = {4, 5, 6, 7, 8, 9, 10}


# print(my_set.difference(your_set))
# .discard()
# .difference_update()
# .intersection() can use shortcut &
# .isdisjoint()
# .issubset()
# .issuperset()
# .union() can use the shortcut |


# conditional logic
# is_old = True
# is_licenced = True

# if is_old and is_licenced:
# print(" you are old enough to drive! ")
# elif is_licenced:
# print(" You can drive now! ")
# else:
# print("checheck")

# print("okokok")


# Truthy and Falsy
# Tenary operator - conditional expression

# is_friend = True
# can_message = "message allowed" if is_friend else "not allowed to message "

# print(can_message)

# Short Circuiting
# is_Friend = True
# is_User = True
# if is_Friend or is_User:
#     print("best friends forever")


# logical operators

# is_magician = True
# is_expert = False

# if is_magician or is_expert:
#     print("You are a master magician")

# elif is_magician and not is_expert:
#     print("at least you've tried")

# elif not is_magician:
#     print("You need magic powers")


# print(True is 1)
# print("1" is str(1))
# print([] is 1)
# print(10 is 10.0)
# print([] is [])

# Loop

user = {"name": "golem", "age": 5006, "can_swim": False}

for key, value in user.items():
    print(key, value)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

# for x in ["a", "b", "c"]:
# print(1, "c")

# interables - an object or colection that can be interated - list, dictionary, tuple, set, str
# intareted - one by one to check each item in the collection

# counter exercise

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# counter = 0
# for item in my_list:
#     counter = counter + item

# print(counter)

# # range function - start, stop, step
# for _ in range(2):
#     print(list(range(10)))
# print(range(100))


# enumerate function
# print(i, char)
# for i, char in enumerate(list(range(100))):
#     print(i, char)
#     if char == 50:
#         print(f"index of 50 is: {i}")

# while loop
# i = 0
# while i < 50:
#     print(i)
#     i += 1
# else:
#     print("done with all the work")

# while loop exercise
# my_list = [1, 2, 3]
# for item in my_list:
#     print(item)

# i = 0
# while i < len(my_list):
#     print(my_list[i])
#     i += 1
# else:
#     print("end of list")

# while True:
#     response = input("say something: ")
#     if response == "bye":
#         break

# brake, continue, pass
my_list = [1, 2, 3]
for item in my_list:
    pass
    print(item)

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    pass

# our first GUI
# next file
