# Simple tic tac toe game with AI
# Mohamad Nachat Karime
# 08.22.2022

board = [' ' for x in range(10)]

# Insert the specified letter at the specified position (pos)
def insertLetter(letter, pos):
    board[pos] = letter

# Check if the specified pos is empty
def spaceIsFree(pos):
    return board[pos] == ' '

# Print a tic tac toe game board
def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

# Check if there is a winner with the same letter across, diagonally, or vertically
def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)

# Takes input from player and makes the specified move
def playerMove():
    run = True
    while run:
        move = input('Select a position to place your X (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('The position you chose already has a letter')
            else:
                print('You entered an invalid position, please type a number withint the range')
        except:
            print('Please enter a number')

# AI algorithm for making moves to win the game or block a player's move
def computerMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    openedCorners = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            openedCorners.append(i)
    if len(openedCorners) > 0:
        move = selectRandom(openedCorners)
        return move
        
    if 5 in possibleMoves:
        move = 5
        return move

    openedEdges = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            openedEdges.append(i)
    if len(openedEdges) > 0:
        move = selectRandom(openedEdges)
        return move

# Selects a random position on the board to place an 0 for computerMove
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

# Check if the board is full
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print('Welcome to Tic Tac Toe!')
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('O has won the game, try again...')
            break

        if not(isWinner(board, 'X')):
            move = computerMove()
            if move == 0:
                print('Its a tie!') 
            else:
                insertLetter('O', move)
                print('The computer placed an O in position:', move)
                printBoard(board)
        else:
            print('You are the winner!')
            break
        
    if isBoardFull(board):
        print('Its a tie!')


main()