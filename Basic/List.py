 
marks = [50, 49, 48, 45 ,50]
print(marks)
print( type(marks) )

print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

print()
print()
print("Negative Index :- ")
print( marks[-1] )
print( marks[-2] )
print( marks[-2] )
print( marks[-4] )
print( marks[-5] )

# negative idex can confuse so use :-  len(list) - index
print()
print()
print("Len(list) - index :- ")
print(marks[len(marks) - 1])
print(marks[len(marks) - 2])
print(marks[len(marks) - 3])
print(marks[len(marks) - 4])
print(marks[len(marks) - 5])

# is present in list or not
print("48 is present :- ")
if 48  in marks : 
    print("yes")
else :
    print("NO")


print(marks[0:3])
print(marks[0 : -2])
print(marks[0: 5 : 2])   # last digit for jump

print()
print()

lst = [i*i for i in range(10)]
print(lst)

lst2 = [i for i in range(100) if i%8 == 0]
print(lst2)

print()
print()
numList = [50, 48, 48 , 96 , 63 , 58, 41]
print("numList :- " , numList)
print("Let's talk about methos in python :- ")
print("Append by 53 :- ")
numList.append(53)

print("Sort method :- ")
numList.sort() 
print(numList)

print("count of 48 :- ", numList.count(48))
print("Reverse List :- ")
numList.reverse()
print(numList)


nlist =  numList # it will create refrance of numList with name 'nlist'
nlist[0] = 100      # so we can manupulate main list by new referance try to not using it 
print(numList)

# use copy functiion rather than referance
print()
print()
nlist = numList.copy()
print(nlist)
