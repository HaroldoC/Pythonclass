from collections import Counter, defaultdict, OrderedDict

# Counter - counts the number of occurences of each item in a list
# li = [1, 2, 3, 4, 5, 6, 7, 7]
# sentence = "blah blah blah thinking about python"
# print(Counter(li))
# print(Counter(sentence))

# defaultdict - never raises a KeyError.  It provides a default value for the key that does not exists. 
# dictionary = defaultdict(lambda: 5, {"a": 1, "b": 2})
# print(dictionary["c"])

# OrderedDict - remembers the order in which the keys are inserted
# d = OrderedDict()
# d["a"] = 1
# d["b"] = 2

# d2 = OrderedDict()
# d2["b"] = 2
# d2["a"] = 1

# print(d2 == d)

# Useful Modules 2 - datetime, time, array, math, os, sys, urllib   

# datetime - allows us to work with dates and times

import datetime

print(datetime.time(5, 45, 2))
print(datetime.date.today())

# time - allows us to work with time

# import time

# print(time.time())

# array - allows us to work with arrays

# import array

# arr = array.array("i", [1, 2, 3])

# print(arr[0])