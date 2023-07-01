# List set, dictionary

# List
# my_list = [char for char in "hello"]
# my_list2 = [num for num in range(0, 100)]
# my_list3 = [num * 2 for num in range(0, 100)]
# my_list4 = [num**2 for num in range(0, 100) if num % 2 == 0]
# print(my_list)
# print(my_list2)
# print(my_list3)
# print(my_list4)

# # Set
# my_list = {char for char in "hello"}
# my_list2 = {num for num in range(0, 100)}
# my_list3 = {num * 2 for num in range(0, 100)}
# my_list4 = {num**2 for num in range(0, 100) if num % 2 == 0}
# print(my_list)
# print(my_list2)
# print(my_list3)
# print(my_list4)

# # Dictionary
# simple_dict = {"a": 1, "b": 2}
# my_dict = {key: value**2 for key, value in simple_dict.items() if value % 2 == 0}
# my_dict2 = {num: num * 2 for num in [1, 2, 3]}
# print(my_dict)
# print(my_dict2)

# Exercise
some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]
duplicates = list(set([char for char in some_list if some_list.count(char) > 1]))
print(duplicates)

# Try Except
# while True:
#     try:
#         age = int(input('What is your age? '))
#         10 / age
#     except ValueError:
#         print('Please enter a number')
#     except ZeroDivisionError:
#         print('Please enter age higher than 0')
#     else:
#         print('Thank you!')
#         break
