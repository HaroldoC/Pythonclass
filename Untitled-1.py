class Dog:
    """
    This class represents a dog with the ability to sit and roll over
    """

    def __init__(self, name: str, age: int):
        """
        Initializes the instance variables "name" and "age"
        """
        self.name = name
        self.age = age

    def sit(self):
        """
        Accesses the instance variable "name" and prints a message indicating the dog is sitting
        """
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """
        Accesses the instance variable "name" and prints a message indicating the dog rolled over
        """
        print(f"{self.name} rolled over!")


my_dog = Dog("Willie", 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
