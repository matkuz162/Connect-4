import random
import os
import time
import numpy as np




def menu():
    print("[1] Play Manually")
    print("[2] AI vs AI")
    print("[3] View Statistics")
    print("[4] Quit")

def options(option):
    if option == 1:
        while True:
            os.system('cls||clear')
            print("Select an agent to play against:")
            print("[1] Random Agent")
            print("[2] Smart Agent")
            print("[3] Mini-Max Agent")
            print("[4] Machine Learning Agent")
            try:
                agent_option = int(input("Enter agent option (1–4): "))
                agents = {
                    1: "Random",
                    2: "Smart",
                    3: "Mini-Max",
                    4: "ML"
                }
                if agent_option in agents:
                    manual_play_game(agents[agent_option])
                    break
                else:
                    print("Invalid agent selected. Please enter a number between 1 and 4.")
                    input("Press Enter to try again.")
            except ValueError:
                print("Invalid input. Must be a number.")
                input("Press Enter to try again.")
    elif option == 2:
        print("AI vs AI selected.")
        input("Press Enter to return.")
    elif option == 3:
        print("Statistics")
        input("Press Enter to return.")
    elif option == 4:
        print("Quitting...")
        exit()

def startfunction():
    while True:
        os.system('cls||clear')
        menu()
        try:
            option = int(input("Enter option: "))
            if option < 1 or option > 4:
                raise ValueError
            os.system('cls||clear')
            options(option)
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")



def display(board):
    
    for row in board:
        print(" | ".join(row))
        print("-"*25)
    print("0 | 1 | 2 | 3 | 4 | 5 | 6")


def check_winner(board, move):
    for row in range(6):
        for col in range(4):
            if all(board[row][col + i] == move for i in range(4)):
                return True

    for col in range(7):
        for row in range(3):
            if all(board[row + i][col] == move for i in range(4)):
                return True

    for row in range(3):
        for col in range(4):
            if all(board[row + i][col + i] == move for i in range(4)):
                return True

    for row in range(3, 6):
        for col in range(4):
            if all(board[row - i][col + i] == move for i in range(4)):
                return True

    return False
        

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

def smart_agent_move(board):
    print("AI Move...")
    time.sleep(2)

    #rule 1 - win if possible
    for col in get_available_moves(board):
        row = find_row_for_col(board, col)
        board[row][col] = '○'
        if check_winner(board, '○'):
            os.system('cls||clear')
            display(board)
            print(f"Smart Agent placed at ({col}).")
            return
        board[row][col] = ' '

    #rule 2 - block if possible
    for col in get_available_moves(board):
        row = find_row_for_col(board, col)
        board[row][col] = '●'
        if check_winner(board, '●'):
            board[row][col] = '○'
            os.system('cls||clear')
            display(board)
            print(f"Smart Agent placed at ({col}).")
            return
        board[row][col] = ' '

    #rule 3 - random move
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


def find_row_for_col(board, col):
    for row in range(5, -1, -1):
        if board[row][col] == " ":
            return row
    return None

def get_available_moves(board):
    available_move = [col for col in range(7) if board[0][col] == " "]
    return available_move


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
    



def manual_play_game(agent):
    os.system('cls||clear')
    board = [[" " for _ in range(7)] for _ in range(6)]
    display(board)

    while True:

        player_move(board)
        if check_winner(board, '●'):
            print("You win!")
            break

        if is_full(board):
            print("The game resulted in a draw")
            break


        if agent == "Random":
            random_agent_move(board)
        elif agent =="Smart":
            smart_agent_move(board)
        elif agent =="Mini-Max":
            print("mm")
        elif agent =="ML":
            print("ml")


        if check_winner(board, '○'):
            print("AI wins!")
            break

        if is_full(board):
            print("The game resulted in a draw")
            break

startfunction()