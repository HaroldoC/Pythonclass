# Hight Order Functions (HOF) are functions that either:

# 1. Take a function as an argument


def greet(func):
    func()


def greet2():
    def func():
        return 5

    return func


print(greet2()())
