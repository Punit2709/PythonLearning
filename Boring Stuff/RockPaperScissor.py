import random

print('ROCK, PAPER, SCISSOR')
print('0 wins, 0 Loose, 0 Ties')

while True :
    print('Enter : (R)ock, (P)aper, (S)cissor or (Q)uit')

    playerChoice = input()
    
    if (playerChoice == 'Q') or (playerChoice == 'q') :
        break
    
    elif (playerChoice == 'R') or (playerChoice == 'r') :
        print('Rock versus...')
        randomNumber = random.randint(1,3)
        
wins = 0
lose = 0
ties = 0
print(wins, lose, ties)