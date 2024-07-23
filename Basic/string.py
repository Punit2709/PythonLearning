# learning String

str = 'Hello'
str2 = 'World'

concat = str + str2

print(concat)


# -------------------------------  Slicing Of String ---------------------------------

# "Punit's" --> tu use single quote inside use double outside and vice versa
# String Slicing --> str[start : end]   
# string also work like Array and index

print(str[0:3])
print(concat[0 : -2])
print(concat[5])
print(concat[-2])  # negative index access from end

# concat[5] = 'g'  --> is not allowded
#  print(concat[150]) --> can't access


print(concat[0: 10 : 2])




story = "Once upon a time there is youtuber name is Harry who uploaded course name Lorry"
print("story is typr of : - " , type(story))
print("length os story is :- " ,len(story))

print(story.endswith('Lorry'))
print(story.count('o'))
print(story.count('rry'))

print(story.capitalize())
print(story.find('upon'))

print(story.replace('Harry' , 'Lorry'))
print(story)

story = story.replace('Harry' , 'Lorry')
print(story)

if 'l' in str :
    print("yesss")
else :
    print("NO")