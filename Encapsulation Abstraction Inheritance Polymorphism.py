# 4 pillars of OOP
# Encapsulation -> grouping of public and private attributes and methods into a programmatic class, making abstraction possible
# Abstraction -> hiding of private attributes and methods from the user
# Inheritance -> passing of attributes and methods from parent to child class
# Polymorphism -> ability to change methods and attributes of instances of child classes


class user:
    def sign_in(self):
        print("logged in")


class wizard(user):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")


class archer(user):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"attacking with arrows: arrows left - {self.num_arrows}")


wizard1 = wizard("Merlin", 50)
archer1 = archer("Robin", 100)


def player_attack(char):
    char.attack()


player_attack(wizard1)
player_attack(archer1)

wizard1.attack()
archer1.attack()
print(wizard1.sign_in())
print(archer1.sign_in())
