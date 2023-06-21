class User(object):
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("logged in")


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def check_arrows(self):
        print(f"{self.num_arrows} remaining")

    def run(self):
        print("ran really fast")

    def attack(self):
        print(f"attacking with arrows: arrows left - {self.num_arrows}")


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, num_arrows, email):
        Archer.__init__(self, name, num_arrows)
        Wizard.__init__(self, name, power, email)


hb1 = HybridBorg("borgie", 50, 100, "")
# print(hb1.sign_in())
# print(hb1.attack())
# print(hb1.email)
# print(hb1.num_arrows)
# print(hb1.power)
# print(hb1.name)
# print(dir(hb1))
# print(HybridBorg.__mro__)
# print(help(HybridBorg))
# print(isinstance(hb1, Wizard))
# print(isinstance(hb1, Archer))
# print(isinstance(hb1, User))
# print(isinstance(hb1, object))
# print(issubclass(Wizard, User))
# print(issubclass(Archer, User))
# print(issubclass(HybridBorg, Wizard))
# print(issubclass(HybridBorg, Archer))
# print(issubclass(HybridBorg, User))
# print(issubclass(HybridBorg, object))
# print(hb1)
# print(len(hb1))
# del hb1
# print(hb1)
# print(help(list))
