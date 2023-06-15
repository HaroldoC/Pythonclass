class Oldest_cat:
    def init(self, name, age):
        self.name = name
        self.age = age


class Cat:
    def init(self, name, age):
        self.name = name
        self.age = age


def oldest_cat(cat1, cat2, cat3):
    x = max(cat1.age, cat2.age, cat3.age)
    return x


cat1 = Cat("Bill", 21)
cat2 = Cat("Bell", 14)
Cat3 = Cat("Tom", 20)
oldest = Cat.oldest_cat(cat1, cat2, Cat3)
print(f"The oldest cat is {oldest} years old")
