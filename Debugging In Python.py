#Debugging in Python - Debugging is a very important part of programming.

# litning bolt is for debugging
# IDE - Integrated Development Environment
# Editors - Sublime, Atom, Notepad++, VS Code, PyCharm, Spyder, Jupyter Notebook
# IDE - PyCharm, Spyder, Jupyter Notebook
# Read error message carefully
# PDB - Python Debugger

import pdb
pdb.set_trace()
name = input("Please enter your name: ")
age = input("Please enter your age: ")
print(f"Hello {name} you are {age} years old")
