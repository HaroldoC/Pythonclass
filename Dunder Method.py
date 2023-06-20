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


action_figure = toy("red", 0)
print(action_figure.__str__())
print(str(action_figure))
