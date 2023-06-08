# *args **kwargs

# *args
# **kwargs


def myfunc(a, b):
    # returns 5% of the sum of a and b
    return sum((a, b)) * 0.05


myfunc(40, 60)


def myfunc(a, b, c=0, d=0, e=0):
    # returns 5% of the sum of a and b
    return sum((a, b, c, d, e)) * 0.05


myfunc(40, 60, 100, 100, 100)


def myfunc(*args):
    return sum(args) * 0.05


myfunc(40, 60, 100, 1, 34)


def myfunc(*args):
    print(args)


# myfunc(40,60,100,1,34)

# def myfunc(*args):
#     for item in args:
#         print(item)

# myfunc(40,60,100,1,34)

# def myfunc(**kwargs):
#     print(kwargs)
#     if 'fruit' in kwargs:
#         print('My fruit of choice is {}'.format(kwargs['fruit']))
#     else:
#         print('I did not find any fruit here')

# myfunc(fruit='apple',veggie='lettuce')

# def myfunc(*args,**kwargs):
#     print(args)
#     print(kwargs)
#     print('I would like {} {}'.format(args[0],kwargs['food']))

# myfunc(10,20,30,fruit='orange',food='eggs',animal='dog')

# def myfunc(*args):
#     mylist = []
#     for num in args:
#         if num % 2 == 0:
#             mylist.append(num)
#         else:
#             pass
#     return mylist
