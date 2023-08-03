# import re

# pattern = re.compile("search inside of this text please!")
# string = "search inside of this text please!"
# a = pattern.search(string)
# b = pattern.findall(string)
# c = pattern.fullmatch(string)
# d = pattern.match(string)
# print(a)


# regular expressions 3

import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = "b@b.com"
a = pattern.search(string)
print(a)

# exercise password checker

import re

pattern = re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")
string = "Aig2025hc$"
a = pattern.search(string)
print(a)


# def check(email):
#     if re.search(regex, email):
#         print("Valid Email")
#     else:
#         print("Invalid Email")


# if __name__ == "__main__":
#     email = "rohit.gupta@mcnsolutions.net"
#     check(email)

#     email = "praveen@c-sharpcorner.com"
#     check(email)

#     email = "inform2atul@gmail.com"
#     check(email)
