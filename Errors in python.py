# Error handling in python

# age = input("Age: ")
# print(age)
# print(int(age) * 12)


# while True:
#     try:
#         age = int(input("what's your age? "))
#         10 / 0
#         print(age)
#     except ValueError:
#         print("Please enter a number")
#     except ZeroDivisionError:
#         print("Please enter age higher than 0")
#     else:
#         print("Thank you!")
#         break


# try:
#     age = int(input("Age: "))
#     income = 20000
#     risk = income / age
#     print(age)
# except ValueError:
#     print("Invalid value")
# except ZeroDivisionError:
#     print("Age cannot be 0")
# except Exception:
#     print("Something went wrong")
# else:
#     print("No exceptions")
# print("Execution continues")

# Error handling in python 2


def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f"Please enter numbers {err}")


# # Exercise
# def divide(num1, num2):
#     try:
#         return num1 / num2
#     except (TypeError, ZeroDivisionError) as err:
#         print(err)
#
#
# print(divide(1, 0))
#
# # Comments
