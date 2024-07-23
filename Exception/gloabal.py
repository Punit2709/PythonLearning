var = 8 # this is global

def fun1():
    # var = 80 # this is local
    global var  # now using gloabal variable
    var = 50
    print(var)

#  if the function using global Variable So need to declare First global 
#  if you declare Local Variable with same name as Global Variable After use Global keyword it cause error

fun1()
print(var)