from employee import Employee 

# i have just import but all methdos run by just importing
# so need to do something so it will not run by only importing file
# Solution :- if __name__ = "__main__"

e = Employee("HEllo","HEllo", 2500)
print(e) # this will invoke (__str__) in Employee Class (__str__) :- should have return type
         # if (__str__) not found then call (__repr__)

print(repr(e))

# Another Dunder Method is __call__ which is called as 
print(e())