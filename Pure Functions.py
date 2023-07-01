# Functional Programing is a style of programming that (as the name suggests) is based around functions.
# A key part of functional programming is higher-order functions. We have seen this idea briefly in the previous lesson on functions as objects. Higher-order functions take other functions as arguments, or return them as results.

# Pure Functions
# Pure functions are functions that have no side effects, that is they don't modify any state or variables outside of their local scope, and they don't rely on side effects from other code, such as modifying a global variable or changing the parameter passed to them.

# wizard = {"name": "Merlin", "power": 50}
# map, filter, zip and reduce


# def multiply_by2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item * 2)
#     return new_list


# print(multiply_by2([1, 2, 3]))


# # Map
# def multiply_by2(item):
#     return item * 2


# print(list(map(multiply_by2, [1, 2, 3])))
# print(list(map(lambda item: item * 2, [1, 2, 3])))
# print(list(filter(lambda item: item % 2 != 0, [1, 2, 3])))
# print(list(zip([1, 2, 3], [10, 20, 30])))
# print(reduce(lambda acc, item: acc + item, [1, 2, 3], 0))


# def greet(func):
#     func()


# def greet2():
#     def func():
#         return 5

#     return func


# print(greet2()())

# Filter - filter out items from a list

# my_list = [1, 2, 3]


# def only_odd(item):
#     return item % 2 != 0


# print(list(filter(only_odd, my_list)))

# Zip - zip together two lists
# my_list = [1, 2, 3]
# your_list = [10, 20, 30]
# their_list = (5, 4, 3)

# print(list(zip(my_list, your_list, their_list)))

# Reduce - reduce a list down to a single value
from functools import reduce

my_list = [1, 2, 3]


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 10))
