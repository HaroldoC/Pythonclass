# __name__ is a built-in variable which evaluates to the name of the current module.

print(__name__)


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def max():
    return "oops"


def main():
    print("utility.py is being run directly")
    print(multiply(2, 3))
    print(divide(2, 3))

    # if __name__ == "__main__":
    # main()
    # else:
    #  print("utility.py is being imported into another module")
