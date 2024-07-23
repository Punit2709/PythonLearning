import sys

a = 10
b = 10.5
c ='hello'
d='hie'
e ='A'

h = True

complex = 2 + 4j

print(sys.getsizeof(a))  # integer takeks :- 28 bytes
print(sys.getsizeof(b))  # float takes :- 24 bytes
print(sys.getsizeof(c))
print(sys.getsizeof(d))
print(sys.getsizeof(e))
print(sys.getsizeof(h))     # bool takes :- 28 bytes
print(sys.getsizeof(complex))   # complex takes :- 32 byte


list = [1,2,3,4,5]
print(sys.getsizeof(list))