import random
board=["-","-","-","-","-","-","-","-","-"]
currentPlayer="X"
winner=None
gameRunning=True
def PrintBoard(board):
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("----------")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("----------")
    print(board[6]+" | "+board[7]+" | "+board[8])


def playerInput(board):
    global currentPlayer
    a=int(input("enter any number from 1-9:"))
    if a>=1 and a<=9 and board[a-1]=="-":
        board[a-1]=currentPlayer
    else:
        print("player is already in that spot ")
        if currentPlayer=="X":
            currentPlayer="O"
        else:
            currentPlayer="X"


def checkRow(board):
    global winner
    if board[0] == board[1] == board[2] and board[1]!="-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4]!="-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[7]!="-":
        winner = board[6]
        return True

def checkColumn(board):
    global winner
    if board[0] == board[3] == board[6] and board[3]!="-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[4]!="-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[5]!="-":
        winner = board[2]
        return True

def checkCross(board):
    global winner
    if board[0] == board[4] == board[8] and board[0]!="-":
        winner=board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4]!="-":
        winner=board[2]
        return True

def checkWin():
    global gameRunning
    if checkColumn(board) or checkRow(board) or checkCross(board):
        print(f"The winner is {winner}")
        gameRunning = False

def checkTie(board):
    global gameRunning
    if "-" not in board:
        PrintBoard(board)
        print("Tie Game")
        gameRunning = False

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer="O"
    else:
        currentPlayer="X"

def printFinalBoard(board):
    if gameRunning == False:
        PrintBoard(board)

def computer(board):
    while currentPlayer == "O":
        position = random.randint(0,8)
        if board[position]=="-":
            board[position]="O"
            switchPlayer()

    
while gameRunning:
    PrintBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    # to play with computer uncomment these below
    #computer(board) 
    #checkWin()
    #checkTie(board)
    printFinalBoard(board)