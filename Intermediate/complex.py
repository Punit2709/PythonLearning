# python have data type complex number 😲😲

c1 = 1 + 2j
print(type(c1))

c2 = 1 + 3j

c3 = c1 + c2
print(c3)
print(c3.real)
print(c3.imag)

print("conjugate of c3:",c3.conjugate())

# multiplication
mulc = c1 * c2
print("multiplication of c1 and c2 :", mulc)

com1 = complex(3, 4)
com2 = complex(3/25, -4/25)
print(com2.real)
print(com2.imag)
print("multiplication: ", com1 * com2)

# inverse of complex number
com3= 1 / com2
print(com3)
print(com2 * com3)

# modulus
mod_of_com3 = abs(com3)
print(mod_of_com3)