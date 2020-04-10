from random import randrange


def DisplayBoard(board):
#
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#    
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   {}   |   {}   |   {}   |'.format(board[0][0],board[0][1],board[0][2]))
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   {}   |   {}   |   {}   |'.format(board[1][0],board[1][1],board[1][2]))
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   {}   |   {}   |   {}   |'.format(board[2][0],board[2][1],board[2][2]))
    print('|       |       |       |')
    print('+-------+-------+-------+')


def EnterMove(board):
#
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
#
    free_squares = MakeListOfFreeFields(board)
    user = int(input('Select the Box to mark :  '))
    if  0 < user <10:
        if free_squares[user-1] == 'R':
            print('Box alreay Occopied. Select another')
        else:
            i,j = free_squares[user-1]
            board[i][j] = 'O'
    return board        


def MakeListOfFreeFields(board):
#
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#
    free_squares = list()
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X' or board[i][j] == 'O':
                free_squares.append('R')
            else:
                free_squares.append((i,j))
    #print(free_squares)
    return free_squares


def VictoryFor(board, sign):
#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
# 
    check =  True
    count = 0

    combinations = [
        [(0,0),(0,1),(0,2)],
        [(1,0),(1,1),(1,2)],
        [(2,0),(2,1),(2,2)],
        [(0,0),(1,0),(2,0)],
        [(0,1),(1,1),(2,1)],
        [(0,2),(1,2),(2,2)],
        [(0,0),(1,1),(2,2)],
        [(0,2),(1,1),(2,0)]
    ]

    for row in combinations:
        for pair in row:
            i,j = pair
            if board[i][j] == sign:
                count += 1
                if count == 3:
                    check = False
                    break 
            else:
                count = 0
        count = 0

    if check == False and sign == 'X':
        print('Computer Won!')
    elif check == False and sign == 'O':
        print('You Won!')
    return check
 
    """
    #check Rows
    for i in range(3):
        for j in range(3):
            if board[i][j] == sign:
                count += 1
                if count == 3:
                    check = False
                    break 
            else:
                count = 0
    #check Columns
    for i in range(3):
        for j in range(3):
            if board[j][i] == sign:
                count += 1
                if count == 3:
                    check = False
                    break 
            else:
                count = 0

    #check left middles
    for i in range(3):
        for j in range(i,i+1):
            if board[i][j] == sign:
                count += 1
                if count == 3:
                    check = False
                    break 
            else:
                count = 0

    #check Right middles
    
    for i in range(2,-1,-1):
        for j in range():
            if board[i][j] == sign:
                count += 1
                if count == 3:
                    check = False
                    break 
            else:
                count = 0
"""
        
def DrawMove(board):
#
# the function draws the computer's move and updates the board
#
    if type(board[1][1]) == int:
        board[1][1] = 'X'
    else:
        free_squares = MakeListOfFreeFields(board)
        while True:
            comp = randrange(10)
            if free_squares[comp-1] == 'R':
                continue
            else:
                i,j = free_squares[comp-1]
                board[i][j] = 'X'
                return board
    return board
            

def main():
    count = 0
    board = [[1,2,3],[4,5,6],[7,8,9]]
    check = True 
    while check and count < 4:    
        board = DrawMove(board)
        check = VictoryFor(board, 'X')
        DisplayBoard(board)
        
        #if computer win no need to take user input so use continue
        if check == False:
            continue
        board = EnterMove(board)
        check = VictoryFor(board, 'O')
        
        #if use wins dispaly the Board
        if check == False:
            DisplayBoard(board)
        count +=1 
        
        #if no one wins and turns completed then display the board
    if count == 4:
        DisplayBoard(board)
    
if __name__ == "__main__":
    main()

