import random
import time
import os


def smart_agent_move(board, display_function, check_winner_function,icon,displayed):

    if icon == '○':
        opposite_icon ='●'
    elif icon =='●':
        opposite_icon = '○'


    #rule 1 - win if possible
    for col in get_available_moves(board):
        row = find_row_for_col(board, col)
        board[row][col] = icon
        if check_winner_function(board, icon):
            if displayed == True:
                os.system('cls||clear')
                display_function(board)
                print(f"Smart Agent placed at ({col}).")
            return col
        board[row][col] = ' '

    #rule 2 - block if possible
    for col in get_available_moves(board):
        row = find_row_for_col(board, col)
        board[row][col] = opposite_icon
        if check_winner_function(board, opposite_icon):
            board[row][col] = icon
            if displayed == True:
                os.system('cls||clear')
                display_function(board)
                print(f"Smart Agent placed at ({col}).")
            return col
        board[row][col] = ' '

    #rule 3 - random move
    random_col = random.randint(0,6)
    while True:
        if board[0][random_col] == " ":
            
            row = range(5,-1,-1)
            for i in row:
                if board[i][random_col] == " ":
                    board[i][random_col] = icon
                    if displayed == True:
                        os.system('cls||clear')
                        display_function(board)
                        print(f"Smart Agent placed at ({random_col}).")
                    return random_col
            break
        else:
            random_col = random.randint(0,6)


def find_row_for_col(board, col):
    for row in range(5, -1, -1):
        if board[row][col] == " ":
            return row
    return None

def get_available_moves(board):
    available_move = [col for col in range(7) if board[0][col] == " "]
    return available_move