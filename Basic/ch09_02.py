# in this 
import random
def game():
    return random.randint(1,1500)

highscore = game()

with open('Harry/highscore.txt', 'r') as f:
    prev = int(f.read())

if highscore > prev :
    with open('Harry/highscore.txt','w') as f:
        f.write( str(highscore) )
    print('Curent Score :- ' , highscore)
else:
    print('Curent Score :- ', prev)

