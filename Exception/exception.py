# a = 5
# b  = 0

# try:
#     c = a * ("Harry" / "HEllo")
#     print(c)
# except Exception as e:
#     print(e)

# print("Program Successful") 

# ---------------------------------------------     Raise Custom Exception        ------------------------------------------------

age  = input('Enter The age ')

try:
    age = int(age)
    if age < 18:
        print('Not allowded')
        exit()
    else:
        print("allowded")
        exit()
except Exception as e:
    raise ValueError("Not Valid Input")
except Exception as e:
    raise TypeError("Not Valid Input")
finally: 
    print("Sucessful")


