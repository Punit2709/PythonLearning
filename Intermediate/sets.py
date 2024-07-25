# set : unordered, mutable, not allow duplicates
myset = {1, 2, 3, 4, 5, 6, 7, 4, 7}
print(myset)

mySet = set(['a', 'b', 'c', 'd', 'f', 'g'])
print(mySet)

# adding value
mySet.add('h')
mySet.add('i')
mySet.add('j')
print(mySet)

# remove : raise keyError
mySet.remove('h')
print(mySet)

# discard
mySet.discard('k')
print(mySet)

for x in mySet:
    print("x: ", x)
    
if 'b' in mySet:
    print("Yesss")   
    
person = {
    "name" : "Punit", 
    "age": 20, 
    "college": "LDCE"
}    

#################################################################
# Performing Set Operations

numSet = {1, 2, 3, 4, 5, 6, 7}
alphaSet = {'a', 'b', 'c', 'd', 'e'}
alphaNumSet = {1, 2, 'a', 'b'}

uniounSet = numSet.union(alphaSet)
print("Union: ", uniounSet)

intersectionSet = numSet.intersection(alphaNumSet)
print("intersectionSet: ", intersectionSet)

diffSet = numSet.difference(alphaNumSet)
print("Diff: ", diffSet)

symDiff = numSet.symmetric_difference(alphaNumSet)
print("Sym: ", symDiff)

# update set 
numSet.update(alphaSet)
print("After Update: ", numSet)

numSet.difference_update(alphaNumSet)
print("After Diff Update: ", numSet)

numSet.intersection_update(alphaSet)
print("After Intsert Update: ", numSet)

numSet.symmetric_difference_update(alphaSet)
print("After Symm Diff Update: ", numSet)

# cheking for subset
print(numSet.issubset(alphaSet))
print(alphaSet.issuperset(numSet))

print(f"Hello i am {person['name']}, a {person['age']} year old boy who studied in {person['college']} Eng College")

