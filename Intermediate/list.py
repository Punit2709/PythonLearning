# list : ordered, mutable and Allow Duplicates

myList = ["Phone", "Laptop", "Book"]
print(myList)

# create empty List
myList2 = list()
print(myList2)

# list with diff Data types
myList3 = [2, True, "Punit", "Punit"]
print(myList3)

#iterate List: for-in loop
for item in myList3:
    print(item)
    
#check itemp in list or not

if 4 in myList3:
    print("Yes Present")
else:
    print("Not Present")

# lenght of list
print("length of List: ", len(myList3))

# append: insert at last 
myList2.append("Banana")
print(myList2)

myList2.append("Apple")
print(myList2)

myList2.insert(1, "Orange")
print(myList2)

lastItem = myList2.pop()
print(lastItem)

# remove method, if item not present in list than give: ValueError
myList3.remove("Punit");
print(myList3)

# clear list
myList.clear()
print(myList)

#reverse and Sort
myList2.sort()
myList2.reverse()
print(myList2)

#not want to change original List
new_list = sorted(myList2)
print(new_list)
print(myList2)

list1 = [0] * 5
list2 = [1, 2, 3, 4, 5]
list3 = list1 + list2
print(list3)

print(min(max(False, -3, -4), 2, 7))
print(min(max(False, -3, 1), 2, 7))

sliceList = [1, 2, 3, 4, 5, 6, 7]
print(sliceList[1:5])
print(sliceList[1:])
print(sliceList[:5])

#step one
print(sliceList[::2])

# reverse List
print(sliceList[::-1])


# Copying List
copy_list = sliceList 
copy_list.insert(0, 0)
print(copy_list)
print(sliceList)
#above method share same memory for original and new list
# so new list can change original list


copy_list1 = sliceList.copy()
print(copy_list1)

copy_list2 = list(sliceList)
print(copy_list2)

copy_list3 = sliceList[:]
print(copy_list3)

#list compehension
comp_List = [i*i for i in sliceList]
print(comp_List)

comp_List2 = [i*2 for i in sliceList]
print(comp_List2)