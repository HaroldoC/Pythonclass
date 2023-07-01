# Square
my_list = [5, 4, 3]

new_list = list(map(lambda item: item * item, my_list))
print(new_list)

# def square(item):
#     return item * item

# print(list(map(square, my_list)))

# List Sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)
