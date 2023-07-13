# Error handling in python

age = input("Age: ")
print(age)
print(int(age) * 12)


while True:
    try:
        age = int(input("what's your age? "))
        10 / 0
        print(age)
    except ValueError:
        print("Please enter a number")
    except ZeroDivisionError:
        print("Please enter age higher than 0")
    else:
        print("Thank you!")
        break


try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("Age cannot be 0")
except Exception:
    print("Something went wrong")
else:
    print("No exceptions")
print("Execution continues")

Error handling in python 2


def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f"Please enter numbers {err}")


print(sum(1, 2))


Exercise
def divide(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(err)


# print(divide(1, 0))
# print(divide(1, 'a'))
# print(divide(1, 2))
# print(divide(1, []))
# print(divide(1, {}))
# print(divide(1, ()))
# print(divide(1, None))
# print(divide(1, True))
# print(divide(1, False))
# print(divide(1, 1))
# print(divide(1, 1.0))
# print(divide(1, -1))
# print(divide(1, -1.0))
# print(divide(1, 1j))
# print(divide(1, -1j))
# print(divide(1, 1+2j))

# Error handling in python 3

while True:
    try:
        age = int(input("what's your age? "))
        10 / 0
        raise ValueError("invalid value")
        print(age)
        continue
    except ValueError:
        print("Please enter a number")
    except ZeroDivisionError:
        print("Please enter age higher than 0")
    else:
        print("Thank you!")
    finally:
        print("ok, i am finally done")
    print("can you hear me?")


# raise ValueError("invalid value")
# raise Exception("invalid value")
# raise TypeError("invalid value")
# raise IndexError("invalid value")
# raise KeyError("invalid value")
# raise NameError("invalid value")
# raise AttributeError("invalid value")
# raise NotImplementedError("invalid value")
# raise SyntaxError("invalid value")
# raise IndentationError("invalid value")
# raise TabError("invalid value")
# raise RuntimeError("invalid value")
