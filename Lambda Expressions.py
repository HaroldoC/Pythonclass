# Lambda expressions are a way to write anonymous functions, functions without a name.

from functools import reduce

my_list = [1, 2, 3]


def multiply_by2(item):
    return item * 2


def only_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(list(map(lambda item: item * 2, my_list)))

print(list(filter(lambda item: item % 2 != 0, my_list)))

print(reduce(lambda acc, item: acc + item, my_list, 0))

print(my_list)

# print(reduce(accumulator, my_list, 0))

# lambda param: action(param)


# def multiply_by2(item):
#     return item * 2


# print(list(map(multiply_by2, [1, 2, 3])))
# print(list(map(lambda item: item * 2, [1, 2, 3])))
# print(list(filter(lambda item: item % 2 != 0, [1, 2, 3])))
# print(list(zip([1, 2, 3], [10, 20, 30])))
# print(reduce(lambda acc, item: acc + item, [1, 2, 3], 0))
