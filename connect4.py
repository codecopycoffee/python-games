import numpy as np

ROW_COUNT = 6
COL_COUNT = 7

#Create a game board with six rows and seven columns of 0s
def create_board():
    board = np.zeros((6, 7))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

#Check if the desired move is able to be made based on whether there is a 0 in that location
def check_location(board, col):
    return board[5][col] == 0

#When a column is selected, get the first available row that a piece can occupy
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

#Initial game conditions
board = create_board()
print(board)
game_over = False
turn = 0

while not game_over:
    #Ask for Player 1 Input
    if turn == 0:
        col = int(input("Player 1 Make Your Selection (0-6):"))

        if check_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)
            print(board)

    #Ask for Player 2 Input
    else:
        col = int(input("Player 2 Make Your Selection (0-6):"))

        if check_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
            print(board)

    #Alternate turns
    turn += 1
    turn = turn % 2
