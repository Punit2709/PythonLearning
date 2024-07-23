# #  Learning Function

# def sum(a , b) :
#     return a + b

# var1 = 'hello'
# var2 = 'punit'
# ans = sum(var1,var2)
# print(ans)

# spam = print("chal n")
# None == spam


# # by default print function puts 'new line' character at the end of arg.
# # we cAN change it by using end=""

# print("Hello")
# print('World')
# #  these  will print Hello and world in two diff lines coz it ends with 'new line' character 

# print('Hello', end=" ")     # now it ends with space
# print('World')

# print('Hello','Howdy','USA') 
# print('Hello','Howdy','USA',sep=", ") 



# local and global variable scope
# locat variable can't call outside of scope and aslo scope of other function
# global and local variable can have a same name but need to use 

eggs = 'global'

def local() :
    eggs = 'Local eggs'
    print(eggs)
    global eggs
    print(eggs)

local()
print(eggs)