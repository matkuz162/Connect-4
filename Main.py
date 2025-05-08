import random
import os
import time
import numpy as np

from Agents.RandomAgent import random_agent_move
from Agents.SmartAgent import smart_agent_move
from Agents.MiniMaxAgent import AI_minimax_Agent
from AIPlay import random_vs_smart, smart_vs_minimax, minimax_vs_ml
from ManualPlay import manual_play_game, player_move

def title():
    print(" _____                             _       ___ ")
    print("/  __ \                           | |     /   |")
    print("| /  \/ ___  _ __  _ __   ___  ___| |_   / /| |")
    print("| |    / _ \| '_ \| '_ \ / _ \/ __| __| / /_| |")
    print("| \__/\ (_) | | | | | | |  __/ (__| |_  \___  |")
    print(" \____/\___/|_| |_|_| |_|\___|\___|\__|     |_/\n")
    
    

def menu():
    title()
    print("[1] Play Manually")
    print("[2] AI vs AI")
    print("[3] View Statistics")
    print("[4] Quit")



def options(option):
    if option == 1:
        while True:
            os.system('cls||clear')
            title()
            print("Choose an agent to play against:")
            print("[1] Random Agent")
            print("[2] Smart Agent")
            print("[3] Mini-Max Agent")
            print("[4] Machine Learning Agent")
            try:
                agent_option = int(input("Enter agent option (1-4): "))
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
        while True:
            os.system('cls||clear')
            title()
            print("Choose which agents play against eachother:")
            print("[1] Random Agent VS Smart Agent")
            print("[2] Smart Agent VS Mini-Max Agent")
            print("[3] Mini-Max Agent VS Machine Learning Agent")
            try:
                agent_option = int(input("Enter agent option (1-3): "))
                matchups = {
                
                    1: random_vs_smart,
                    2: smart_vs_minimax,
                    3: minimax_vs_ml
                }
                if agent_option in matchups:
                    matchups[agent_option](display,check_winner,is_full)  # Call the appropriate function
                    break
                else:
                    print("Invalid option selected. Please enter a number between 1 and 4.")
                    input("Press Enter to try again.")
            except ValueError:
                print("Invalid input. Must be a number.")
                input("Press Enter to try again.")
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
        



def is_full(board):
    return all(board[row][col] != " " for row in range(6) for col in range(7))

def col_free(board, column):
    if board[0][column] == " ":
        return True
    else:
        return False
    







startfunction()





            


    








