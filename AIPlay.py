import random
import os
import time
import numpy as np
import psutil
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import csv

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


# Game-Level Metrics ( Winning Patterns: frequency of horizontal, vertical, diagonal winning strategies
# Resource Utilization Metrics (i.e., memory usage)


def random_vs_smart(display_function, check_winner_function, is_full_function):
    random_wins = 0
    smart_wins = 0
    draws = 0

    runs = 500

    game_times = []

    os.system('cls||clear')
    print("Loading...")

    for game in range(0, runs):
        
        board = [[" " for _ in range(7)] for _ in range(6)]

        individual_game = time.time()

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

        end_individual_game = time.time()
        game_times.append(end_individual_game - individual_game)

    total_time = sum(game_times)
    average_time = total_time / runs
    random_winrate = round((random_wins/runs) * 100, 1)
    smart_winrate = round((smart_wins/runs) * 100, 1)
    drawrate = round((draws/runs) * 100, 1)


    os.system('cls||clear')

    print(f"Random Agent won: {random_wins} times.")
    print(f"Smart Agent won: {smart_wins} times.")
    print(f"The game ended in a draw: {draws} times.")

    random_winrate = round((random_wins/(runs))*100,1)
    smart_winrate = round((smart_wins/(runs))*100,1)
    drawrate = round((draws/runs)*100,1)

    print(f"\nRandom Agent winrate: {random_winrate}%")
    print(f"Smart Agent winrate: {smart_winrate}%")
    print(f"Drawrate: {drawrate}%")

    if random_winrate > smart_winrate:
        print("\nRandom Agent Performs Better.")
    elif smart_winrate > random_winrate:
        print("\nSmart Agents Performs Better.")
    elif drawrate > random_winrate and drawrate > smart_winrate:
        print("\nThe Agents are evenly matched.")

    print(f"\nTotal execution time for {runs} games: {total_time:.2f} seconds")
    print(f"Average time per game: {average_time:.4f} seconds")










def smart_vs_minimax(display_function, check_winner_function, is_full_function):
    smart_wins = 0
    minimax_wins = 0
    draws = 0
    runs = 500
    os.system('cls||clear')
    print("Loading...")

    for game in range(0, runs):
        
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
    runs = 500
    os.system('cls||clear')
    print("Loading...")

    ml_agent = MachineLearningAgent(player_symbol='●')
    minimax_agent = Minimax_Agent(depth=4)

    for game in range(0, runs):
        
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