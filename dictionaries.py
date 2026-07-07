# DICTIONARIES
# Dictionaries are used to store data values in key:value pairs
# Dictionary items are ordered, changeable, and do not allow duplicates.
# They can be referred to by using the key name.

# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }
# print(thisdict)
# print(len(thisdict))

#ACCESS ITEMS
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["model"])
# print(thisdict.keys()) #prints only the keys
# print(thisdict.values()) #prints only the values

#ADD ITEMS
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "white"
# print(thisdict)

#CHANGE ITEMS
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["year"] = 2018
# print(thisdict)

#UPDATE ITEMS #for update, key value pair needs to be provided to update
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020})
# print(thisdict)

#IF EXISTS
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")