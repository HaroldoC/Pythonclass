# OOP
class PlayerCharacter:
    membership = True  # class object attribute

    def __init__(self, name, age):
        # if self.membership:
        # self.name = name
        self.name = name  # atributes
        self.age = age

    # def run(self):
    #     print("run")
    #     return "done"

    def shout(self):
        print(f"My name is {self.name}")

    @classmethod
    def adding_things(cls, num1, num2):
        return cls("Teddy", num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player3 = PlayerCharacter.adding_things(2, 3)
print(player3.age)

# return "done"

# def attack(self):
#     print(f"{self.name} is attacking")
#     return "done"

# def checkMembership(self):
#     print(f"{self.name} is a member? {self.membership}")
#     return "done"

# def changeMembership(self):
#     self.membership = not self.membership
#     print(f"{self.name} is a member? {self.membership}")
#     return "done"

# def changeName(self, newName):
#     self.name = newName
#     print(f"Name changed to {self.name}")
#     return "done"


# player1 = PlayerCharacter("Çindy", 21)
# player2 = PlayerCharacter("Tom", 44)
# player2.attack = 50
# print(player1.shout())
# print(player2.age)
# print(player2.membership)
