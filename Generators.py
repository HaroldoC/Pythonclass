# Genarators are used to create iterators, but with a different approach. Generators are simple functions which return an iterable set of items, one at a time, in a special way.

range(100)
list(range(100))
# print(list(range(100)))


def make_list(num):
    result = []
    for i in range(num):
        result.append(i * 2)
    return result


my_list = make_list(100)
print(my_list)

Generator 2

def generator_function(num):
    for i in range(num):
        yield i * 2


for item in generator_function(1000):
    print(item)

my_gen = generator_function(100)
print(next(my_gen))


# When an iteration over a set of item starts using the for statement, the generator is run. Once the generator's function code reaches a "yield" statement, the generator yields its execution back to the for loop, returning a new value from the set. The generator function can generate as many values (possibly infinite) as it wants, yielding each one in its turn.

# Here is a simple example of a generator function which returns 7 random integers:

import random


def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)
    # returns a 7th number between 1 and 15
    yield random.randint(1, 15)


for random_number in lottery():
    print("And the next number is... %d!" % (random_number))

# This function decides how to generate the random numbers on its own, and executes the yield statements one at a time, pausing in between to yield execution back to the main for loop.
