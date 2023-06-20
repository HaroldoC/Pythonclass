class user:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("logged in")


class wizard(user):
    def __init__(self, name, power, email):
        # user.__init__(self, email)
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")

    def sign_in(self):
        print(f"logged in as {self.name}")

    def __str__(self):
        return f"{self.name} has {self.power} power"

    def __len__(self):
        return 5

    def __del__(self):
        print("deleted")


wizard1 = wizard("Merlin", 50, "merlin@gmail.comm")

print(wizard1.email)

# Introspection - the ability to determine the type of an object at runtime
