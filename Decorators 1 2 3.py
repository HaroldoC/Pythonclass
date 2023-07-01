# decorator is a function that takes another function as an argument, adds some kind of functionality, and then returns another function.
# All of this without altering the source code of the original function that we passed in.

# @classmethod
# @staticmethod

# Decorator 1 - Simple Decorator

# def hello():
#     print("helloooo")


# greet = hello
# del hello
# print = greet()


# def hello(func):
#     func()


# def greet():
#     print("still here!")


# a = hello(greet)

# print(a)


# Decorator 2 - Decorator Function


# def my_decorator(func):
#     def wrap_func():
#         print("**********")
#         func()
#         print("**********")

#     return wrap_func


# @my_decorator
# def hello():
#     print("hello")


# @my_decorator
# def bye():
#     print("see ya later")


# hello()
# bye()

# Decorator 3 - Decorator with Parameters


# def my_decorator(func):
#     def wrap_func(*args, **kwargs):
#         print("**********")
#         func(*args, **kwargs)
#         print("**********")

#     return wrap_func


# @my_decorator
# def hello(greeting, emoji=":("):
#     print(greeting, emoji)


# hello("hiiii")

# Decorator 4 - Performance Decorator
# why decorator are useful

from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"took {t2-t1} s")
        return result

    return wrapper


@performance
def long_time():
    for i in range(100000000):
        i * 5


long_time()


# def special_greeting(func):
#     def wrapper(*args, **kwargs):
#         print("**********")

#         func(*args, **kwargs)

#         print("**********")

#     return wrapper


# @special_greeting
# def hello():
#     print("hello")


# hello()
