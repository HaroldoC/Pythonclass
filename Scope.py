# Scope - what variables do I have access to?

if True:
    x = 10
print(x)


def some_func():
    total = 100
    print(total)


total = 100
print(total)


num = 10


def confusion():
    num = 100
    return num


print(num)
print(confusion())


def parent():
    num = 3

    def confusion():
        return num

    return confusion()


print(parent())
print(confusion())


# Scope rules:
# 1 - Start with local
# 2 - Parent local?
# 3 - Global
# 4 - Built in python functions
