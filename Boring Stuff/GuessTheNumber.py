import random
scereteNumber = random.randint(1 , 20)

for i in range (7) :  # player will guess 7 times

    print('Enter Your Number :')
    inputNumber = int(input())
    
    if inputNumber < scereteNumber :
        print('Your Number is Small')
    elif inputNumber > scereteNumber :
        print('Your Number is large')
    else :
        break

# check the value of entered Number
if (inputNumber == scereteNumber) :
    print('Yesss, It is my Number too 🥳🥳')
else :
    print('You fail to Guess My Number 😩😩')
