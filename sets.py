# Set
# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# Set items are unordered, unchangeable, and do not allow duplicate values.
# Duplicates not allowed

# myset = {"apple", "banana", "cherry"}
# print(myset)
# print(len(myset))

#ACCESS DATA
# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#   print(x)

#IF DATA PRESENT IN SET
# thisset = {"apple", "banana", "cherry"}
# print("banana" in thisset) #returns true if banana is present in set

#ADD ITEMS
# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# print(thisset)

#ADD SETS
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)