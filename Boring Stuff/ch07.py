import re


# number = input("Enter The Phone Number is Patter xxx-xxx-xxxx :- ")
# print((len(number)))
# print(len('852-896-8965'))

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if  text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True
         
print(isPhoneNumber('444-555-9696'))
print(isPhoneNumber('444-555-969a'))

# Finding the number if String
message   = 'Write My Number 854-475-9696.'

for i in range(len(message)):
    chunk = message[i : i + 12]
    if isPhoneNumber(chunk):
        print('Number is :- ',chunk)        


# here we are using a lot code to find the Phone Number it can be reduce by using regex
# we need to import re.
# created phone num Regex.
# (\d\d\d-\d\d\d-\d\d\d\d)

phoneNumReg = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  #here we use r:- to make raw string so it wiil not neglect '\'
mo = phoneNumReg.search('My Number is 951-048-3539');
print( mo.group() )

# pattern = r'[A-Z]+ello'  #it will Phello , Bello,Cello

# match = re.finditer(pattern,'Hello Punit Buy Cello')

# for match in range :
#     print(match)

superHero = re.compile(r'Batman|Superman')
hero = superHero.search("I am Batman")
print(hero)

hero  = superHero.search("I am Superman")
print(hero)

# so re.compile(r'Batman|Superman')  :- will find any one of them Batman and Superman

hero  = superHero.search("I am Superman and Batman too")
print(hero)

hero  = superHero.search("I am Batman and Superman too")
print(hero)


# if something is optional in matching it can done by using :- '?'
# below will find Superwoman but 'wo' is optional so it can aslo accept Superman

optional = re.compile(r'Super(wo)?man')
woman = optional.search("I am not Superwoman")
print(woman)


woman = optional.search("I am not Superman")
print(woman)

# so it can also work with Superman

phoneNumberFinder = re.compile(r'(91)?\d\d\d-\d\d\d-\d\d\d\d')
mobile = phoneNumberFinder.search('My Nuber is +91951-048-3539')
print(mobile)

mobile = phoneNumberFinder.search('My Nuber is 951-048-3539')
print(mobile)