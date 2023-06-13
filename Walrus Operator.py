# This is a walrus operator :=
# It is used to assign values to variables as part of a larger expression
# It is also called assignment expression
# It assigns values to variables as part of a larger expression
# It assigns values to variables that can be used elsewhere in the expression

a = "hello"
if (n := len(a)) > 10:
    print(f"Too long {n} elements")
else:
    print(f"OK {n} elements")
