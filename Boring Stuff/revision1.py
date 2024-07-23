
"""

myList = ['My', 'List', 'This', 'is']
print(myList, end='\n\n')

# lIst by using list constructor
myList = list((4,5,6,7,8,5,9)) # aloows duplicate values
print(type(myList))
print(myList)

print(myList[-4:-1])

myList[3] = 8
print(myList)
if myList[-2] is 5 :
    print('Balle Balle')


# adding in List 1.Inster   2.Append    3.Extend
# 1.Inster :- add at specific Index
# 2.Append :- add at at the End of List
# 3.Extend :- add onther list at the end of List 

myList.insert(5, 45)
print(myList)

myList.append(89)
print(myList)

tempList =[75,72,71,78]
myList.extend(tempList)
print(myList)

myList.sort()
print(myList)

# Removing Item From List 
# 1. del   :- remove from specific Index. by this Wed can also Delete the List so No longer Lost is avilable
# 2. pop   :- remove from last Index
# 3. cleaf :- Clear the list, No loanger any item present in list

del myList[5]
print(myList)

del tempList
# print(tempList)  #generate the error cause whole List is deleted

myList.pop()
print(myList)

myList.clear()
print(myList)


"""

# -------------------------------------------------- Ch 2 Tuple -------------------------------------------------- 

# Tuple is immutable so can't change the data in tupple
"""
myTuple = ('hello', 'hiii', 'kemchoo', 'majama n')
print(type(myTuple))
print(myTuple)

# indexing and Slicing Similar to List
#immutabel so can't chage directly

myList = list(myTuple)
print(myList)
myList.append('Haa Majama')
myList.append('Tame kem ?')
myTuple = tuple(myList)
print(myTuple)

# can't remove direclty so make List then change accordingly

# marks = (45,45,48,47)  this is Packing
# (48,48,47,48) = marks this is unpacking

# joining In Tuple 
tuple1 = (45,45,48,47)
tuple2 = (48,48,47,48)
tuple3 = tuple1 + tuple2
print(tuple3)

print(tuple3.count(48))
"""


# -------------------------------------------------- Ch 3 Dictionary -------------------------------------------------- 
# denoted by curly bracket 
# ordered and duplicate are not allowded

"""
myDict ={
    "fruit": "apple",
    "Biscuit": "parleg",
    "Laptop":"Dell",
    "College":"LDCE"
}

print(myDict)
print(type(myDict))
print()
# here index is Key
# Acceing Item  1.Index(key)    2.getMethod 

print(myDict["College"])
print(myDict.get("Biscuit"))
print()

print(myDict.keys())
print(myDict.values())
print(myDict.items())
print()

# change Item ans Add
myDict.update({"fruit":"Banana"})
print(myDict)

myDict["Game"] ="AnyGame"
print(myDict)

myDict.update({"Language":"Python"})
print(myDict)


"""


# -------------------------------------------------- Ch 4 Set -------------------------------------------------- 
# A set :-  unordered, unchangeable, and unindexed.
# allow duplicate value but only consider once


"""
mySet = {"PUNIT","ARYAN","DHRUV","SMIT"}
print(mySet)
print(type(mySet))

# Access items :- 1. For loop 

for x in mySet:
    print(x)

print("PUNIT" in mySet)

# add in Set

mySet.add("RAJA")
print(mySet)

# removing from Set 
# 1. Discard :- not present -> not error  
# 2. Remove  :- not present -. yeah Error(Error type -> keyError)
# 3. pop     :- pop randomly not know which one
# 4. clear   :- Clear the whole Set and now set is empty
# 5. del     :- set not exsist 

mySet.remove("RAJA")

mySet.discard("RAJA")
mySet.pop()
print(mySet)
mySet.clear()
print(mySet)
# del mySet
# print(mySet)


# --------------------------------------    Set Operation    -----------------------------------------------------
# 1.intersection    2.Union     3.difference    4.symmetric_difference

set1 = {"A","B","C","D","E","E"}
print(set1)
set2 = {"D","E","F","G","H"}
print(set2)

print()

print("Intersection :- " , set1.intersection(set2))
print("Union :-" , set1.union(set2))
print("set1 - set2 :-" , set1.difference(set2))
print("set2 - set1 :-" , set2.difference(set1))

print("set1 sydiff set2 :-" , set1.symmetric_difference(set2))
print("set2 sydiff set1 :-" , set2.symmetric_difference(set1))

"""