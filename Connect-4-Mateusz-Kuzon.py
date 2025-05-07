import random
import os
import time


def display(board):
    
    for row in board:
        print(" | ".join(row))
        print("-"*25)
    print("0 | 1 | 2 | 3 | 4 | 5 | 6")

#def check_winner(board,player):
 #   for row in board:
 #       for i in row:
 #           if board[i]
        

def random_agent_move(board):
  print("AI Move...")
  time.sleep(2)
  random_cell = random.randint(0,6)
  while True:
    if board[0][random_cell] == " ":
        
        row = range(5,-1,-1)
        for i in row:
            if board[i][random_cell] == " ":
                board[i][random_cell] = '○'
                os.system('cls||clear')
                display(board)
                print(f"Random Agent placed at ({random_cell}).")
                break
        break
    else:
        random_cell = random.randint(0,6)

def is_full(board):
    return all(board[row][col] != " " for row in range(6) for col in range(7))

def col_free(board, column):
    if board[0][column] == " ":
        return True
    else:
        return False

def player_move(board):
    while True:
        try:
            col = int(input("Enter your move (0-6): "))
            if col < 0 or col > 6:
                raise ValueError
            if col_free(board, col):
                row = range(5,-1,-1)
                for i in row:
                    if board[i][col] == " ":
                        board[i][col] = '●'
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
    



def play_game():
    board = [[" " for _ in range(7)] for _ in range(6)]
    display(board)

    while True:

        player_move(board)

        #check winner

        if is_full(board):
            print("The game resulted in a draw")
            break


        #random agent
        random_agent_move(board)


        #check winner

        if is_full(board):
            print("The game resulted in a draw")
            break








play_game()
