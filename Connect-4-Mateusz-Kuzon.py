import random

def display(board):
    for row in board:
        print(" | ".join(row))
        print("-"*9)

board = [[" " for _ in range(3)] for _ in range(3)]

display(board)