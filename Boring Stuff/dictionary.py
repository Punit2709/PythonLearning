
# myCat = { 'size ' : 'Big', 'color' : 'Black', 'type' : 'furry'} 
# # dectionary is key-value pair
# print(myCat)

# #accessing by index
# print( myCat['color'] )
# print( myCat['type'] )
# print( myCat['size '] )
# print()


# # list --> ordered
# # Dictionary --> unordered
# # respective index value should be same for List if two lost are same but not for dictinaory

# spamList1 = ['cat', 'dog', 'cow', 'tiger']
# spamList2 = ['dog', 'cow', 'tiger', 'cat']
# print( spamList1 == spamList2 ) 
# #  false cause order is not same
# print()

# myDog1 = { 'size ' : 'small', 'color' : 'Black', 'type' : 'furry'}
# myDog2 = {'color' : 'Black', 'type' : 'furry', 'size ' : 'small'}
# print(myDog1 == myDog2)
# true cause order not matter


# accessing key whivh is not present cause keyError
# myCat['food']


# Birthday program

birthday = {'Raja' : 'April', 'Chetan' : 'December', 'Dev' : 'August', 'Aditya' : 'February'}


# while True : 
#     name = input('Enter the name :- ')

#     if name == '' :
#         break

#     if name in birthday :
#         print( name + "'s birth month is " + birthday[name] )

#     else :
#         print('Birth Month Not Found : So provide it -')
#         month = input()
#         birthday[name] = month
#         print('Database is Updated : ')

 
# key() value() and items() ---  method 

for k in birthday.values() :
    print(k)

print()
for k in birthday.keys() :
    print(k)  

print()
for k in birthday.items() : 
    print(k)


