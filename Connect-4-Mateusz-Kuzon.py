import random
import os
os.system('color')

red='\33[31m'
yellow='\33[33m'
default='\033[0m'

def display(board):
    
    for row in board:
        print(" | ".join(row))
        print("-"*25)
    print("0 | 1 | 2 | 3 | 4 | 5 | 6")

#def check_winner(board,player):


def is_full(board):
  return all(board[row][col]!=" " for row in range(7) for col in range(6))

def random_agent_move(board):
  empty_cells = [(row,col) for row in range(7)for col in range(6) if board[0][col] ==  " " ]
  return random.choice(empty_cells)

def play_game():
    board = [[" " for _ in range(7)] for _ in range(6)]
    display(board)

    while True:
        try:
            col = int(input("Enter your move (0-6): "))
            if board[0][col] == " ":
                row = range(5,0,-1)
                for i in row:
                    if board[i][col] == " ":
                        board[i][col] = red+u'\u25CF'+default
                        break
                break
            else:
                print("Column Full. Try again.")
        except (ValueError, IndexError):
             os.system('cls||clear')
             display(board)
             print("Invalid input. Enter column numbers between 0 and 6.")
    os.system('cls||clear')
    display(board)



play_game()



#print(red+u'\u25CF')
#print(yellow+u'\u25CF')
