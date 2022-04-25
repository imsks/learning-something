# print("Hello, World!")

"""
This is multi-line comment
if 5 > 2:
  print("Five is greater than two!")
"""

# x = float(5)
# print(x)

# my_variable_name = "s"

# x, y, z = 1, 2, 3
# print(x, y)

# x = y = z = 5
# x = 2
# print(x, y)

# fruits = ["Banana", "Apple"]
# x, y = fruits
# print(x ,y)

# x = 5
# y = "Sachin"
# print(x + y)

# x = 5
# print(type(x))

# x = 2
# print(complex(x))

# import random
# print(random.randrange(0, 5))

# x = "5"
# print(int(x))

# for x in "Sachin":
#     print(x)

# x = "A{}  B{} C{}"
# print(len(x))
# print(x[-2:])
# print(x.lower())
# print(x.format(1, 2, 3))

# print(bool(None))
# print(bool(0))

# x = 5
# y = 2
# if x is y:
#     print(True)
# else:
#     print(False)

# list = ["Banana", "Apple"]
# print(list[-1])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.append("Orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#     print(thislist[i])
# [print(x) for x in thislist]
# new_list = [x for x in thislist if "app" in x]
# print(new_list)
# thislist.sort()
# print(thislist)
# thislist.sort(reverse=True)
# print(thislist)

# another_list = thislist.copy()
# print(another_list)

# thislist[0] = "A"
# print(another_list)
# print(thislist)

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[-1])

# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y
# print(thistuple)

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)

# thistuple = ("apple", "banana", "cherry")
# for x in range(len(thistuple)):
#     print(x)

# tuple1 = ("a", "b", "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(fruits.count("apple"))
