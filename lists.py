#LIST
# Lists are used to store multiple items in a single variable. 
# It is ordered and changeable.
# Lists are written with sqaure brackets
# They allow duplicates.

# mylist = ["apple", "banana", "cherry"]

# thislist = ["apple", "banana", "cheery"]
# print(thislist)   
# print(thislist[1])
# print(thislist[-1])
# print(len(thislist))
# print(type(thislist))

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])
# print(thislist[:4]) #print all except kiwi
# print(thislist[2:]) #prints all from cherry to end
# print(thislist[-4:-1]) #reverse

# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#     print("Item does exist.")

#CHANGE ITEMS
# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackberry"
# print(thislist)
# thislist[1:3] = ["blackberrr", "watermelon"]
# print(thislist)

#INSERT ITEMS
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

#APEND LIST
# thislist = ["apple", "banana", "cherry"]
# thislist.apend("watermelon")
# print(thislist)

#EXTEND LIST
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

#REMOVE ITEMS
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

#REMOVE ITEMS ON SPECIFIED INDEX
# thislist = ["apple", "banana", "cherry"]
# # thislist.pop(1)
# thislist.pop() #removes last item in list
# print(thislist)

#DELETE ENTIRE LIST
# thislist = ["apple", "banana", "cherry"]
# del thislist

#COPY LIST
# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)

#JOIN TWO LSITS
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list3)

#SORT LIST
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# thislist.sort(reverse = True) #reverse sort
# print(thislist)