# MRO - Method Resolution Order
# MRO is the order in which Python looks for a method in a hierarchy of classes.


# class A:
#     num = 10


# class B(A):
#     pass


# class C(A):
#     num = 1


# class D(B, C):
#     pass


# print(D.num)
# print(D.mro())
# print(D.__mro__)
# print(help(D))
# print(dir(D))
# print(D.__dict__)
# print(D.__class__)
# print(D.__bases__)
# print(D.__base__)
# print(D.__subclasses__())
# print(D.__mro__)
# print(D.__mro__[0].__subclasses__())


class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(M.mro())
# print(M.__mro__)
# print(help(M))
# print(dir(M))
# print(M.__dict__)
# print(M.__class__)
# print(M.__bases__)
# print(M.__base__)
# print(M.__subclasses__())
# print(M.__mro__)
# print(M.__mro__[0].__subclasses__())
