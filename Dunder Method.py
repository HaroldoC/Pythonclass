# Dunder methods are special methods that allow us to emulate built-in behaviour within Python and it's also how we implement operator overloading


class toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age

    def __str__(self):
        return f"{self.color}"

    def __len__(self):
        return 5

    def __del__(self):
        return "deleted"

    def __call__(self):
        return "yes??"

    def __getitem__(self, i):
        return self.color[i]

    def __repr__(self):
        return f"toy('{self.color}', {self.age})"

    def __add__(self, other):
        return self.age + other.age

    def __mul__(self, other):
        return self.age * other.age

    def __len__(self):
        return self.age


action_figure = toy("red", 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure[0])
print(repr(action_figure))
print(action_figure + action_figure)
print(action_figure * action_figure)
print(len(action_figure))
