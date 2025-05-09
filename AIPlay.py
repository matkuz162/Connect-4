import random
import os
import time
import numpy as np

from Agents.RandomAgent import random_agent_move
from Agents.SmartAgent import smart_agent_move
from Agents.MiniMaxAgent import AI_minimax_Agent

def random_vs_smart(display_function, check_winner_function, is_full_function):
    random_wins = 0
    smart_wins = 0
    draws = 0

    os.system('cls||clear')
    print("Loading...")

    for game in range(0, 500):
        
        board = [[" " for _ in range(7)] for _ in range(6)]

        while True:

            random_agent_move(board,display_function,'●',displayed=False)
            if check_winner_function(board, '●'):
                random_wins += 1
                break

            if is_full_function(board):
                draws += 1
                break


            smart_agent_move(board, display_function, check_winner_function,'○',displayed=False)

            if check_winner_function(board, '○'):
                smart_wins += 1
                break

            if is_full_function(board):
                draws += 1
                break

    os.system('cls||clear')
    print(f"Random Agent won: {random_wins} times.")
    print(f"Smart Agent won: {smart_wins} times.")
    print(f"The game ended in a draw: {draws} times.")




def smart_vs_minimax(display_function, check_winner_function, is_full_function):
    smart_wins = 0
    minimax_wins = 0
    draws = 0
    os.system('cls||clear')
    print("Loading...")

    for game in range(0, 500):
        
        board = [[" " for _ in range(7)] for _ in range(6)]

        while True:

            col = smart_agent_move(board, display_function, check_winner_function, '●', displayed=False)
            if check_winner_function(board, '●'):
                smart_wins += 1
                break

            if is_full_function(board):
                draws += 1
                break


            minimax_agent = AI_minimax_Agent(depth=4)
            col = minimax_agent.best_move(board, check_winner_function, is_full_function)
            for row in range(5,-1,-1):
                if board[row][col] == " ":
                    board[row][col] = '○'
                    break

            if check_winner_function(board, '○'):
                minimax_wins += 1
                break

            if is_full_function(board):
                draws += 1
                break

    os.system('cls||clear')
    print(f"Smart Agent won: {smart_wins} times.")
    print(f"Mini-Max Agent won: {minimax_wins} times.")
    print(f"The game ended in a draw: {draws} times.")


def ml_vs_minimax():
    print("not implemented")