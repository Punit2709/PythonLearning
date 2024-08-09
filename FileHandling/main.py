import os
file = open(".\hello.txt", 'r')

# reading file
# print(file.read())

#read line
# print(file.readline())

#read line by line
# for x in file:
#     print(x)
    
# It is a good practice to always close the file when you are done with it.
file.close() 

f = open("hello.txt", "a+")
f.write("Now the file has more content!")
f.close()

f = open("hello.txt", "r")
for x in f:
    print(x)
    
if os.path.exists("delete.txt"):
  os.remove("delete.txt")
else:
  print("The file does not exist")