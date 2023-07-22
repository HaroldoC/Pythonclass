# generate a random number between 1 and 10
# if user input matches the random number, print "you win"
# if user input does not match the random number, print "you lose"

# import random

# from random import randint

# random_number = random.randint(1, 10)

# user_input = input("Guess a number between 1 and 10: ")

# if user_input == random_number:
#     print("You win!")
# else:
#     print("You lose!")

# print(random_number)

# print(user_input)

# print(type(random_number))

# print(type(user_input))

from random import randint

answer = randint(1, 10)

while True:
    try:
        guess = input("Guess a number between 1 and 10: ")
        if int(guess) > 0 or int(guess) < 11:
            print('all good')
            break
    except ValueError:
        print("Please enter a number")
        continue
