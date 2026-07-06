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
# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
# thisset.update(tropical)
# print(thisset)

#REMOVE ITEMS
# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")
# print(thisset)

#POP ITEM (REMOVE)
# thisset = {"apple", "banana", "cherry"}
# x = thisset.pop()
# print(x)
# print(thisset)

#LOOP ITEMS
# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#   print(x)

#JOIN SETS
#Union - returns a new set with all items from both sets
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3)
#Update - inserts all items from one set into another (does not create new set)
# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
# set1.update(set2)
# print(set1)
#Intersection - returns a new set, that only contains the items that are present in both sets
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.intersection(set2)
# print(set3)
#Difference - returns a new set, containing only items from first set not present in other set
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.difference(set2)
# print(set3)
#Symmetric Difference - keeps only the elements that are NOT present in both sets
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.symmetric_difference(set2)
# print(set3)