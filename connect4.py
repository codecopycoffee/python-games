import numpy as np

def create_board():
    board = np.zeros((6, 7))
    return board

#Initial game conditions
board = create_board()
game_over = False
turn = 0

while not game_over:
    #Ask for Player 1 Input
    if turn == 0:
        selection = int(input("Player 1 Make Your Selection (0-6):"))

    #Ask for Player 2 Input
    else:
        selection = int(input("Player 2 Make Your Selection (0-6):"))

    #Alternate turns
    turn += 1
    turn = turn % 2
