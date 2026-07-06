a = "Hello, World!"
# print(a[1]) # outputs 'e'

for x in "banana":
    print(x)
    
print(len(a))

a = "my name is anas"
print("anas" in a) # checks if string has 'anas'

if("anas" in a):
    print('yes anas is present in the "a" text')
    
if("gut" not in a):
    print('"gut" is not present in "a" text')
    
print(a[3:7]) #slice
print(a[:2]) #slicing from the start
print(a[-4:-2]) # slicing from the end
print(a.replace('m', 'j')) #replace
print(a.split()) #split

#FORMAT STRINGS
age = 5
format = f"my age us {age}" #can use numbers in string this way
format = f"result is: {age+5}" #age+5
format = f"result is: {age+5:.2f}" #age+5 and 2 decimal points
print(format)

#ESCAPE CHARACTERS
escape = "we are the \"vikings\" from the north" #allows double quotes
print(escape)
