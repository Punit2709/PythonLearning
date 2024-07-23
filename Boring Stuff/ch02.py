import time

# ------------------------------     conditional statement      -------------------------------------------

# name = input('Enter The Name :')

# if name == 'Punit' :
#     print("Hello Punit")
#     password = input('Enter Passcode : ')

#     if password == 'nahiBataunga' :
#         print('Get Access')
#     else :  
#         print('Wrong PassWord')
# else : 
#     print('Kon hai tu')


# --------------------------------       elif statement     ------------------------------------------------------
# name1 = 'Carol'
# age = 3000
# if name1 == 'Alice':
#     print('Hi, Alice.')
# elif age < 12:
#     print('You are not Alice, kiddo.')
# elif age > 100:
#     print('You are not Alice, grannie.')
# elif age > 2000:
#     print('Unlike you, Alice is not an undead, immortal vampire.')

# # in above code if age = 950  means you want to print immortal vampire 
# # But it prints grannie cause 950 > 100 so 
# # In elif case ORDER MATTERS

# --------------------------------------        Break in loop       ----------------------------------------------
# age = input('Enter Your Age : ')
# age = int(age)

# while (age > 18) :
#     print('Ready For Driving Test : ')
#     ans = input()
#     if ( (ans == 'YES') or (ans == 'yes') or (ans == "Yes") )  :
#         print("Good")
#         break;
#     else :
#         print('Go and Prepare')
#         time.sleep(3);

# if(age < 18) :
#     print('Under Age ')


# --------------------  For Loop  ----------------------------------

# name = input('Enter Your name ')

# for i in range(5) :
#     if i == 2 :
#         continue
#     print('My name is ' + name + ' ' +str(i) )


# total = 0
 
# for i in range(10000) :
#     total += i 

# print(total)
    
#  ---------------------------      for loop with range(start, stop)     -----------------------------

# Total = 0
# for i in range(11, 10000) :
#     Total += i

# print(Total)

#  -----------------------------      for loop with step (start, stop, step)    ---------------------------

evenTotal = 0

for i in range(0, 20000, 2) :
    evenTotal += i

print(evenTotal)
