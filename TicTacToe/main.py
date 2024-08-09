board = [[" ", " ", " "], 
         [" ", " ", " "], 
         [" ", " ", " "]]

lastMove = ""
isEnd = False

def checkWinOrTie():
    global board
    global isEnd 
    
    for i in range(3):
        
        #check for row
        if board[i][0] == board[i][1] == board[i][2] != " ":
            print(f"Winner is : {board[i][0]}")
            isEnd = True
            return
        
        #check for colunm
        if board[0][i] == board[1][i] == board[2][i] != " ":
            print(f"Player {board[0][i]} wins!")
            isEnd = True
            return
        
        #check for diagonals
        if board[0][0] == board[1][1] == board[2][2] != " ":
            print(f"Player {board[0][0]} wins!")
            isEnd = True
            return
        
        if board[0][2] == board[1][1] == board[2][0] != " ":
            print(f"Player {board[0][2]} wins!")
            isEnd = True
            return
        
        #check for tie
        isEnd = True
        for row in board:
            for cell in row:
                if cell == " ":
                    isEnd = False
                    break
            
            if not isEnd:
                break;
        
        if isEnd:
            print(f"Match is Tie")

def nextMove():
    global lastMove
    if lastMove == "" or lastMove == "O":
        print('Next move is: X')
        lastMove = "X"
    elif lastMove == "X":
        print('Next move is: O')
        lastMove = "O"
    
def choosePos():
    global lastMove
    nextMove()
        
    print("Choose Your next Postion")
    print("Available Postions are: ")
    for i in range(0, 3):
        for j in range(0, 3):
            if(board[i][j] == " "):
                print(f"{i}{j}", end=", ")    
    print()
        
    try: 
        chosenPosX = int(input('Enter x: '))
        chosenPosY = int(input('Enter y: '))
        if board[chosenPosX][chosenPosY] == " ":
            board[chosenPosX][chosenPosY] = lastMove
        else: 
            print(f"Space is not Empty") 
            lastMove = "X" if lastMove == "O" else "O"
            
    except(IndexError, ValueError):
        print(f"You Have entered Invalid input")
        lastMove = "X" if lastMove == "O" else "O"
        

def printBoard():
    for x in board:
            print(f"|{x[0]}|{x[1]}|{x[2]}|" )
            
def start():
    while not isEnd:
        printBoard()
        choosePos()
        checkWinOrTie()
    printBoard()
    print("Game Over")

start()