# dictionary : Key-Value Paired, Unordered, Mutable

myDict = {"name": "Punit", "age":20, "College": "LDCE"};
print(myDict)

myDict["email"] = "punitsp2003@gmail.com"
value = myDict["email"]
print(value)

try:
    print(myDict["city"])
except KeyError:
    print("No City")

# value = myDict("city") genarate error


for key in myDict:
    print(key)

for key in myDict.keys():
    print(key)

for value in myDict.values():
    print(value)
    
for key, value in myDict.items():
    print(key + " : " + str(value))

    
# copy dictionary
copy_dict = myDict.copy()
print(copy_dict)

copy_dict2 = dict(myDict)
print(copy_dict2)

del myDict
# myDict is deleted
# print(myDict)

try:
    print(myDict)
except NameError:
    print("myDict is deleted")

# number and tuples can also used as Key
myDictNumber = {3: 4, 4:5, 5:6, 6:7}
print(myDictNumber)

myTuple = (4, 5)
myList = [1, 2, 3]
myDictTuple = {myTuple: 5}
print(myDictTuple)

myTupeDict = {"a": myTuple, "b": myList}
print(myTupeDict)