
# how python knows it is String , OInt, or Float

a = 'hello World'
b = 14.56
c = True
d = None

print(a)
print(b)
print(c)
print(d)
print()

#printing the type  of variable
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print()

# dealing with operator
# 1. arithmetic opreator :- +, -, *, /, //, **
print("Sum of 3 + 2 is : ", 3 + 2)
print("Sub of 3 - 2 is : ", 3 - 2)
print("Mul of 3 * 2 is : ", 3 * 2)
print("Div of 3 / 2 is : ", 3 / 2)
print("Power of 3^2 =  ", 3**2)
print("Div with int ans 3 // 2 = ", 3 // 2)
print()

# 1. asiignment opreator : =, +=, -=
A = 5
print(" A = " , A)
A += 5              # means add  5 to A
print("A += ", A)  
A -= 5              # means subtract 5 to A
print("A -= ", A)
print()

# 1. comparison opreator : ==, > , >= , < , <=, !=
boolean = (5 == 3)
print(" 5 == 3 ,", boolean)

boolean = ( 5 > 3)
print(" 5 > 3 ,", boolean)

boolean = ( 5 >= 3)
print(" 5 >= 3 ,", boolean)

boolean = ( 5 < 3)
print(" 5 < 3 ,", boolean)

boolean = ( 5 <= 3)
print(" 5 <= 3 ,", boolean)

boolean = (5 != 3)
print(" 5 != 3 ,", boolean)
print()

# 1. logical opreator : and , or , not
logic1 = False
logic2 = True
print("And of True and Flase = ", logic1 and logic2)
print("And of True or Flase = ", logic1 or logic2)
print("Not of True = " , not True)
print("Not of false = ", not False)

# typre casting
typeInt = int(34.5)
print(typeInt)

typeInt = int(A)        # this print ASCII value of "A"
print(typeInt)

typeString = str(3546)
print(typeString)

typeString = str(356.22)
print(typeString)

typeFloat = float(35)
print(typeFloat)