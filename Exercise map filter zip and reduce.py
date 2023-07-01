# from functools import reduce

my_pets = ["sisi", "bibi", "titi", "carla"]


def cap(item):
    return item.upper()


print(list(map(cap, my_pets)))
print(my_pets)
# 2
my_strings = ["a", "b", "c", "d", "e"]
my_numbers = [5, 4, 3, 2, 1]

print(list(zip(my_strings, sorted(my_numbers))))
# 3
scores = [73, 20, 65, 19, 76, 100, 88]


def pass_over(item):
    return item > 50


print(list(filter(pass_over, scores)))


# 4
def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, (my_numbers + scores)))
