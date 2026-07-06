# TUPLES
# Tuples are used to store multiple items in a single variable.
# It is ordered and un-changeable.
# Tuples are written with round brackets.
# They allow duplicates.
# You are allowed to add tuples to tuples

# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))

#CREATE TUPLE WITH ONE ITEM
# thistuple = ("apple",) #this is a tuple
# thistuple = ("apple") #not a tuple, without "," this is considered as string

#PRINT TUPLES
# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])
# print(thistuple[-1]) #reverse print
# print(thistuple[1:3]) #range of indexes

#CHECK IF ITEM IN TUPLE EXISTS
# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#     print("yes, it does exist")
# else:
#     print("does not exist")

#UPDATE TUPLE
# TUPLE will be converted to LIST to change it
# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "orange"
# print(y)

#ADD ITEM TO TUPLE
# TUPLE will be converted to LIST to change it
# x = ("apple", "banana", "cherry")
# y = list(x)
# y.append("orange")
# print(y)

#REMOVE ITEM FROM TUPLE
# TUPLE will be converted to LIST to change it
# x = ("apple", "banana", "cherry")
# y = list(x)
# y.remove("apple")
# print(y)

#REMOVE TUPLE
# TUPLE will be converted to LIST to change it
# x = ("apple", "banana", "cherry")
# del x

#ADD TUPLE TO TUPLE
# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y
# print(thistuple)

#UNPACK TUPLE
# fruits = ("apple", "banana", "cherry")
# (green, yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)

#LOOP TUPLE
# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#     print(x)

#LOOP THROUGH INDEX
# thistuple = ("apple", "banana", "cherry")
# for i in range(len(thistuple)):
#     print(thistuple[i])

#WHILE LOOP
# thistuple = ("apple", "banana", "cherry")
# i=0
# while i < len(thistuple):
#     print(thistuple[i])
#     i+=1
