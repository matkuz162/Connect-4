#imports
import os
import numpy as np
import seaborn as sns
import matplotlib as plt
import pandas as pd

from AIPlay import random_vs_smart, smart_vs_minimax, ml_vs_minimax
from ManualPlay import manual_play_game

#title
def title():
    print(" _____                             _       ___ ")
    print("/  __ \                           | |     /   |")
    print("| /  \/ ___  _ __  _ __   ___  ___| |_   / /| |")
    print("| |    / _ \| '_ \| '_ \ / _ \/ __| __| / /_| |")
    print("| \__/\ (_) | | | | | | |  __/ (__| |_  \___  |")
    print(" \____/\___/|_| |_|_| |_|\___|\___|\__|     |_/\n")
    
    
#menu
def menu():
    title()
    print("[1] Play Manually")
    print("[2] AI vs AI")
    print("[3] Quit")


#options
def options(option):
    if option == 1:
        while True:
            os.system('cls||clear')
            title()
            #lets the user choose what agent they want to play against manually
            print("Choose an agent to play against:")
            print("[1] Random Agent")
            print("[2] Smart Agent")
            print("[3] Mini-Max Agent")
            print("[4] Machine Learning Agent")

            #try and catch to confirm the user input
            try:
                agent_option = int(input("Enter agent option (1-4): "))
                agents = {
                    1: "Random",
                    2: "Smart",
                    3: "Mini-Max",
                    4: "ML"
                }
                # depending on what agent they choose it will choose which win checker it chooses
                if agent_option in agents:
                    agent_name = agents[agent_option]
                    winner_function = check_winner if agent_name == "Mini-Max" else check_winner_bool_only
                    #runs the game against the agent chosen
                    manual_play_game(display, winner_function, is_full, agent_name)
                    break
                else:
                    print("Invalid agent selected. Please enter a number between 1 and 4.")
                    input("Press Enter to try again.")
            except ValueError:
                print("Invalid input. Must be a number.")
                input("Press Enter to try again.")
    # if the user chooses to play ai against eachother
    elif option == 2:
        while True:
            os.system('cls||clear')
            title()
            #which agents play against eachtother
            print("Choose which agents play against eachother:")
            print("[1] Random Agent VS Smart Agent")
            print("[2] Smart Agent VS Mini-Max Agent")
            print("[3] Mini-Max Agent VS Machine Learning Agent")
            try:
                agent_option = int(input("Enter agent option (1-3): "))
                matchups = {
                
                    1: random_vs_smart,
                    2: smart_vs_minimax,
                    3: ml_vs_minimax,
                }
                #runs the agents against eachother
                if agent_option in matchups:
                    matchups[agent_option](display,check_winner,is_full)
                    break
                else:
                    print("Invalid option selected. Please enter a number between 1 and 4.")
                    input("Press Enter to try again.")
            except ValueError:
                print("Invalid input. Must be a number.")
                input("Press Enter to try again.")
    #closes the game
    elif option == 3:
        print("Quitting...")
        exit()

#starts the game by letting them choose what they want to do
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


#displays the game board
def display(board):
    
    for row in board:
        print(" | ".join(row))
        print("-"*25)
    print("0 | 1 | 2 | 3 | 4 | 5 | 6")


# checks for wins and returns what type of direction it was a win in
def check_winner(board, move):

    #horizontal win
    for row in range(6):
        for col in range(4):
            if all(board[row][col + i] == move for i in range(4)):
                return True, "Horizontal"
            
    #vertical win
    for col in range(7):
        for row in range(3):
            if all(board[row + i][col] == move for i in range(4)):
                return True, "Vertical"

    #positive diagonal win  
    for row in range(3):
        for col in range(4):
            if all(board[row + i][col + i] == move for i in range(4)):
                return True, "Diagonal"

    #negative diagonal win      
    for row in range(3, 6):
        for col in range(4):
            if all(board[row - i][col + i] == move for i in range(4)):
                return True, "Diagonal"
    return False, None

# checks win but doesnt return what direction since some dont need it
def check_winner_bool_only(board, move):
    result, _ = check_winner(board, move)
    return result

#checks if full board
def is_full(board):
    return all(board[row][col] != " " for row in range(6) for col in range(7))

#checks if a column is free
def col_free(board, column):
    if board[0][column] == " ":
        return True
    else:
        return False
    












            


    








