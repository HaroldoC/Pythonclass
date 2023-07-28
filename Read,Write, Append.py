# My_file = open("Pythonclass\Read,Write, Append.txt", "a")
# My_file.write("This is a new line")
# My_file.close()
# # Path: Pythonclass\Read,Write, Append.py

with open("Pythonclass\Read,Write, Append.txt", mode="w") as My_file:
    text = My_file.write("This is a new line")
    My_file.write("\nHey whats good today")

# File paths - Windows - C:\Program Files\Microsoft
# File paths - Mac - /usr/bin/
# File paths - Linux - /usr/local/bin/
# File paths - Python - Pythonclass\Read,Write, Append.txt
# pathlib

# file I/O errors - FileNotFoundError, PermissionError, IOError, UnsupportedOperation, NotADirectoryError, IsADirectoryError

try:
    with open("Pythonclass\Read,Write, Append.txt", mode="r") as My_file:
        print(My_file.read())
except FileNotFoundError as err:
    print("File does not exist")
#     raise err
# except IOError as err:
#     print("IO error")
#     raise err
# except UnsupportedOperation as err:
#     print("Unsupported Operation")
#     raise err
# except NotADirectoryError as err:
#     print("Not a directory")
#     raise err
# except IsADirectoryError as err:
#     print("Is a directory")
#     raise err
# except PermissionError as err:
#     print("Permission error")
#     raise err
# else:
#     print("Success")
# finally:
#     print("I always run no matter what")
