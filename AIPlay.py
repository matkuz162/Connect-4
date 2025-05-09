import random
import os
import time
import numpy as np

from Agents.RandomAgent import random_agent_move
from Agents.SmartAgent import smart_agent_move
from Agents.MiniMaxAgent import Minimax_Agent
from Agents.MachineLearningAgent import MachineLearningAgent

# win rate draw rate loss rate
#search performace metrics
#efficiency metrics execution time
#heuristic evaluation quality + counterplay ability
# game length, winning patterns - frequency of horizontal, vertical or diagonal wins
# robustness - performance against different agents
# memory usage


# Accuracy Metrics (win rate, draw rate & loss rate).Accuracy Metrics (win rate, draw rate & loss rate).
# Efficiency Metrics (Execution time
# Game-Level Metrics (Game Length, Winning Patterns: frequency of horizontal, vertical, diagonal winning strategies
# Robustness Metrics (i.e., performance against different opponents)
# Resource Utilization Metrics (i.e., memory usage)


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


            minimax_agent = Minimax_Agent(depth=4)
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


def ml_vs_minimax(display_function, check_winner_function, is_full_function):
    ml_wins = 0
    minimax_wins = 0
    draws = 0
    os.system('cls||clear')
    print("Loading...")

    ml_agent = MachineLearningAgent(player_symbol='●')
    minimax_agent = Minimax_Agent(depth=4)

    for game in range(0, 500):
        
        board = [[" " for _ in range(7)] for _ in range(6)]

        while True:
            col = ml_agent.choose_move(board)
            for row in range(5,-1,-1):
                if board[row][col] == " ":
                    board[row][col] = '●'
                    break

            if check_winner_function(board, '●'):
                ml_wins += 1
                break

            if is_full_function(board):
                draws += 1
                break


            minimax_agent = Minimax_Agent(depth=4)
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
    print(f"Machine Learning Agent won: {ml_wins} times.")
    print(f"Mini-Max Agent won: {minimax_wins} times.")
    print(f"The game ended in a draw: {draws} times.")