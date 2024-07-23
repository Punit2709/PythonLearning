

# this will raise exception cause file not exixst 
# try:
#     with open("Advanced Python/text1.txt",'r') as f:
#         pass
# except Exception as e:
#     print( "File no Exist" ) 
# finally:
#     print("Block completed") 


# def :- Write the program to print 3rd 5th and 7th  element from list using enumarater
 
# list1 = [1 , 1.5 ,6.7, 'Hello', True, 'Bye', 9.0, 15] 
# print(list1)

# for index,item in enumerate(list1) :
#     if index == 2 or index == 4 or index == 6 :
#         print(f"Ans is {index + 1 }  {item} ")
    


# def :- Write the table of any numbebr using List Comprehension

num = int(input("Enter The number :- "))

list = [num*i for i in range (1, 11)]
print(list)


with open("Tables.txt", 'w+') as f:
    f.write(str(list))
    f.write("\n")