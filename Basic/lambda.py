
def sum(a , b):
    return a + b

sum = lambda a,b : a + b
avg = lambda a,b: (a + b) // 2
square = lambda x : x*x
cube = lambda x : x*x*x

print(sum(3,5))
print(avg(3,5))

print(square(5))
print(cube(5))

# lamda function in function
apply = lambda df,value : df(value) + value
print(apply(lambda y : (y*y*y)/3 , 3))

# print(lambda lambda value : (value*value)//2 : )
# y = 3
# print(lambda y : (y*y))
#  above few lines dosen't make sence