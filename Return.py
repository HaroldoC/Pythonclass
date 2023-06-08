def sum(num1, num2):
    return num1 + num2


print(sum(4, 5))

total = sum(10, 5)
print(total)


def sum(num1, num2):
    def another_func(n1, n2):
        return n1 + n2

    return another_func


total = sum(10, 20)
print(total(10, 20))


def sum(n1, n2):
    def another_func(n1, n2):
        return n1 + n2

    return another_func(n1, n2)


total = sum(10, 20)
print(total)

# def sum(n1, n2):
#     def another_func(n1, n2):
#         return n1 + n2
#     return another_func


# total = sum(10, 20)
# print(total(10, 20))
