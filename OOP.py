# OOP


class BigObject:  # class
    # code
    pass


obj1 = BigObject()  # instanciate
obj2 = BigObject()  # instanciate
obj3 = BigObject()  # instanciate
print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type("hi"))
print(type([]))
print(type(()))
print(type({}))
print(type(set(BigObject())))

# Inheritance


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")


my_dog = Dog("Willie", 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

# Class -> Instantiate -> Instances
