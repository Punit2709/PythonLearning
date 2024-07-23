# tuple : ordered, immutable, allow duplicates
# tuple is more efficient than list

myTuple = ("Max", 2, True, "Punit", "Punit")
print(myTuple)

singleEleTuple = ("Single",)
print(type(singleEleTuple))

myList = [2, 3, 4, 5]
listTuple = tuple(myList)
print(listTuple)

# indexing in tuple
first = myTuple[1]
print(first)

second = myTuple[2]
print(second)

subTuple = myTuple[2:]
print(subTuple)

# myTuple[0] = "Punit"
# give an error of TypeError

if "Punit1" in myTuple:
    print("Yesss Present")
else:
    print("Not, Present")
    
for x in myTuple:
    print("Item: ", x)    
    
#length 
print(len(myTuple))

#count element
print(myTuple.count("Punit"))

# index of Element: return First Occurance
print(myTuple.index("Punit"))

# Tuple --> List --> Tuple
myList = list(myTuple)
print(myList)

myTuple2 = tuple(myList)
print(myTuple2)

# Slicing Don't Include Last mention Index
a = myTuple2[:-1]
print(a)

a = myTuple2[::-1] # reverse tuple
print(a)


# unpacking Tuple
# require exact number of variables
tupleX = "Punit", "20", "LDCE", "Python"
name, age, college, course = tupleX
print(name + " " + age + " " + college + " " + course)

name, *extra,  course = tupleX
print(name)
print(extra) # this will be List
print(course)

