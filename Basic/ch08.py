# this chapter about function and recersion
# In Python Function consist :- def + funname :

def averageFun(a , b):
    return (a + b)/2

def sumfun(a , b) :
    return a + b


c = sumfun(10,15)
print(c)

avg = averageFun(14,18)
print(avg)


# ----------------------------------------------------------------------------------------------------------------------------------------------------

def factorial(n):
    if (n < 0) :
        return -1;
    elif ( n == 0 or n == 1):
        return 1
    else:
        return(n*factorial(n-1))
        
def fibbonacci(n):
    if(n < 1):
        print('Invalid')
    
    elif(n == 1):
        return 0

    elif( n == 2 or n == 3):
        return 1

    else:
        return fibbonacci(n-1) + fibbonacci(n-2)

# these all are function
# recersion is the function which call itself


fact = factorial(5)
print(fact)

print(fibbonacci(10))


# ----------------------------------------------------------------------------------------------------------------------------------------------------------

# lets see default aregument
# if we pass name the it will print -> (Hello name) else print->(Hello Strager)
def greet(name='Ajnabee'):
    print('Hello ' + name)

greet('Punit')
greet()  # print 'Hello Ajanabee'


def sumOfN(n):
    if(n == 0):
        return 0
    return n + sumOfN(n-1)

print(sumOfN(150))


# split the Sting and remove giviner world
# split - removing Spaces from start and end

def split_and_remove(str,word):
    newstr = str.replace(word, "")
    return newstr.strip()

print( split_and_remove("             Hello Punit Kese Ho ?             ", "Punit") )