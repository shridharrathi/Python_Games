import random

num_board = [1,2,3,4,5,6,7,8,9]

def drawBoard(board):
    c = 9
    print 'Input Board \t\t\tBoard Position'
    for i in range(3):
        print '| ' + str(board[c-3]) + ' | ' + str(board[c-2]) + ' | ' + str(board[c-1]) +' |',
        print '\t\t\t',
        print '| ' + str(num_board[c-3]) + ' | ' + str(num_board[c-2]) + ' | ' + str(num_board[c-1]) +' |'
        c -=3
    
def selectLetter():
    letter =''
    while not (letter == 'X' or letter == 'O'):
        letter = raw_input('Please select the Letter(X/O) :' ).upper()
    return letter

def whoGoesFirst():
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'
    
def playAgain():
    return raw_input('Do you want to play again Y/N: ').lower().startswith('y')
    
def isWinner(bo, le):
    return ((bo[7] == le and bo[8] ==le and bo[9] == le)or
            (bo[4] == le and bo[5] ==le and bo[6] == le) or
            (bo[1] == le and bo[2] ==le and bo[3] == le) or

            (bo[7] == le and bo[4] ==le and bo[1] == le) or
            (bo[8] == le and bo[5] ==le and bo[2] == le) or
            (bo[9] == le and bo[6] ==le and bo[3] == le) or

            (bo[7] == le and bo[5] ==le and bo[3] == le) or
            (bo[9] == le and bo[5] ==le and bo[1] == le)
            )
            
def getBoardCopy(bo):
    dupe_Bo = []

    for i in bo:
        dupe_Bo.append(i)

    return dupe_Bo

def isSpaceFree(bo, move):
    return bo[move] == ' '

def getPlayerMove(bo):
    move =' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(bo, int(move)):
        move = raw_input('What is your next move: ')

    return int(move)

def chooseRandomMovesFromList(bo, moveList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(bo, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(bo, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter ='X'

    for i in range(1,10):
        copy = getBoardCopy(bo)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i


    for i in range(1,10):
        copy = getBoardCopy(bo)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    move = chooseRandomMovesFromList(bo, [1,3,7,9])
    if move != None:
        return move

    if isSpaceFree(bo, 5):
        return 5

    return chooseRandomMovesFromList(bo, [2,4,6,8])

def isBoardFull(bo):
    for i in range(1,10):
        if isSpaceFree(bo, i):
            return False

    return True


print 'Welcome to Tic Tac Toe'
print

while True:
    theBoard = [' '] * 10
    playerLetter = selectLetter()
    turn = whoGoesFirst()
    print 'The ' + turn + ' will go first'
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            
    


drawBoard(theBoard)
getPlayerMove(theBoard)
print playAgain()


