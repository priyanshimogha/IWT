board = {1: ' ', 2: ' ', 3: ' ', 
         4: ' ', 5: ' ', 6: ' ', 
         7: ' ', 8: ' ', 9: ' ', }

moves = {1: '1', 2: '2', 3: '3', 
        4: '4', 5: '5', 6: '6', 
        7: '7', 8: '8', 9: '9', }

def printSampleBoard(board):
    print(moves[1]+ '|' +moves[2]+ '|' +moves[3])
    print('-*-*-')
    print(moves[4]+ '|' +moves[5]+ '|' +moves[6])
    print('-*-*-')
    print(moves[7]+ '|' +moves[8]+ '|' +moves[9])
    print('\n')

def printBoard(board):
    print(board[1]+ '|' +board[2]+ '|' +board[3])
    print('-*-*-')
    print(board[4]+ '|' +board[5]+ '|' +board[6])
    print('-*-*-')
    print(board[7]+ '|' +board[8]+ '|' +board[9])
    print('\n')

print("\nSample Moves :")
printSampleBoard(moves)
printBoard(board)


def spaceIsFree(position):
    return board[position] == ' '

# print(spaceIsFree(2))

def checkWin( ):
    if(board[1] != ' ' and board[1]==board[2]==board[3] ):
        return True
    elif(board[4] != ' ' and board[4]==board[5]==board[6] ):
        return True
    elif(board[7] != ' ' and board[7]==board[8]==board[9] ):
        return True
    elif(board[1] != ' ' and board[1]==board[4]==board[7] ):
        return True
    elif(board[2] != ' ' and board[2]==board[5]==board[8] ):
        return True
    elif(board[3] != ' ' and board[3]==board[6]==board[9] ):
        return True
    elif(board[1] != ' ' and board[1]==board[5]==board[9] ):
        return True
    elif(board[7] != ' ' and board[7]==board[5]==board[3] ):
        return True
    else:
        return False
    

def checkWhichMarkWin(mark):
    if(board[1] == mark and board[1]==board[2]==board[3] ):
        return True
    elif(board[4] == mark and board[4]==board[5]==board[6] ):
        return True
    elif(board[7] == mark and board[7]==board[8]==board[9] ):
        return True
    elif(board[1] == mark and board[1]==board[4]==board[7] ):
        return True
    elif(board[2] == mark and board[2]==board[5]==board[8] ):
        return True
    elif(board[3] == mark and board[3]==board[6]==board[9] ):
        return True
    elif(board[1] == mark and board[1]==board[5]==board[9] ):
        return True
    elif(board[7] == mark and board[7]==board[5]==board[3] ):
        return True
    else:
        return False


def checkDraw():
    for key in board.keys():
        if(board[key] == ' '):
            return False
    
    return True

def insertLetter(letter,position):
    if(spaceIsFree(position)):
        board[position] = letter
        printBoard(board)

        if(checkWin()):
            if(letter == 'X'):
                print("BOT WINS!")
            else:
                print("YOU WIN!")
            exit()

        if(checkDraw()):
            print("DRAW!")
            exit()
        
    else:
        while(True):
            print("CAN'T ISERT THERE!")
            position = int(input("Enter new position: "))
            if(spaceIsFree(position)):
                insertLetter(letter,position)
                break
    

player = 'O'
bot = 'X'
def checkPosition(position):
    if(checkDraw()):
        return False
    return 1<= position <= 9 and spaceIsFree(position)
    
def playerMove():

    if checkDraw():   # Check before allowing input
        print("Game Draw!")
        exit()

    while True:
        try:
            position = int(input("Enter the position for 'O' : "))
            if(checkPosition(position)):
                insertLetter(player, position)
                break
            else:
                print("POSITION IS ALREAY TAKEN OR INVALID! TRY AGAIN.")
        except ValueError:
            print("Invalid Input Please Enter a number ")

        


def compMove():
    if checkDraw():   # Stop AI move if it's a draw
        print("Game Draw!")
        exit()

    bestScore = -1000
    bestMove = None

    for key in board.keys():
        if(board[key] == ' '):
            board[key] = bot
            score = minimax(board,0,False)
            board[key] = ' '
            if(score > bestScore):
                bestScore = score
                bestMove = key
    if bestMove is not None:
        insertLetter(bot, bestMove)
    else:
        print("No available Moves")


def minimax(board, depth, isMaximizing):
    if(checkWhichMarkWin(bot)):
        return 100
    elif(checkWhichMarkWin(player)):
        return -100
    elif(checkDraw()):
        return 0

    if(isMaximizing):
        bestScore = -1000
        
        for key in board.keys():
            if(board[key] == ' '):
                board[key] = bot
                score = minimax(board,depth+1,False)
                board[key] = ' '
                if(score > bestScore):
                    bestScore = score
        return bestScore
    else:
        bestScore = 1000
        for key in board.keys():
            if(board[key] == ' '):
                    board[key] = player
                    score = minimax(board,depth+1,True)
                    board[key] = ' '
                    if(score < bestScore):
                        bestScore = score
        return bestScore


while True:
    playerMove()
    if (checkDraw() or checkWin()):
        break
    compMove()
    if (checkDraw() or checkWin()):
        break