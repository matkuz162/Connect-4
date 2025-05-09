#imports
import os
import time
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import csv
import tracemalloc

from Agents.RandomAgent import random_agent_move
from Agents.SmartAgent import smart_agent_move
from Agents.MiniMaxAgent import Minimax_Agent
from Agents.MachineLearningAgent import MachineLearningAgent



#first ai matchup
def random_vs_smart(display_function, check_winner_function, is_full_function):
    #runs 500 times since its a fast one
    runs = 500
    os.system('cls||clear')
    print("Loading...")

    #opens and overwrites into csv file
    with open("random_vs_smart_per_game.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        #writes heading
        writer.writerow(["Game", "Winner", "Execution Time (s)", "Memory Usage (KB)", "Win Type"])


        for game_num in range(0, runs):
            board = [[" " for _ in range(7)] for _ in range(6)]

            #tracks memory
            tracemalloc.start()
            #tracks time
            start_time = time.time()
            #tracks who won
            winner = "Draw"
            win_type = "None"

            while True:
                #random agent moves
                random_agent_move(board, display_function, '●', displayed=False)
                won, win_type_candidate = check_winner_function(board, '●')
                #checks if won
                if won:
                    winner = "Random"
                    win_type = win_type_candidate
                    break
                
                #checks if draw
                if is_full_function(board):
                    break

                smart_agent_move(board, display_function, check_winner_function, '○', displayed=False)
                won, win_type_candidate = check_winner_function(board, '○')
                if won:
                    winner = "Smart"
                    win_type = win_type_candidate
                    break
                if is_full_function(board):
                    break

            #ends timer
            end_time = time.time()
            #gets memory
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            #how long it took to run and memory used
            execution_time = round(end_time - start_time, 4)
            memory_kb = round(peak / 1024, 2)

            #writes into csv the statistics of the game after every game
            writer.writerow([game_num, winner, execution_time, memory_kb, win_type])

    os.system('cls||clear')

    #reads from the csv
    df = pd.read_csv("random_vs_smart_per_game.csv")

    #plots winrate
    sns.countplot(data=df, x="Winner", palette="pastel")
    plt.title("Game Outcomes: Random vs Smart")
    plt.show()

    #plots time taken
    sns.lineplot(data=df, x="Game", y="Execution Time (s)", label="Time per Game")
    plt.title("Execution Time per Game")
    plt.ylabel("Time (s)")
    plt.grid(True)
    plt.show()

    #plots memory usage
    sns.lineplot(data=df, x="Game", y="Memory Usage (KB)", color="purple")
    plt.title("Memory Usage per Game: Random vs Smart")
    plt.ylabel("Memory (KB)")
    plt.xlabel("Game Number")
    plt.grid(True)
    plt.show()

    win_type_counts = df[df["Win Type"] != "None"]["Win Type"].value_counts()
    sns.barplot(x=win_type_counts.index, y=win_type_counts.values, palette="muted")
    plt.title("Overall Win Type Distribution")
    plt.ylabel("Number of Wins")
    plt.xlabel("Win Type")
    plt.grid(axis="y")
    plt.show()

    #determines what type of win
    df_wins = df[df["Winner"] != "Draw"]
    random_wins_df = df_wins[df_wins["Winner"] == "Random"]
    smart_wins_df = df_wins[df_wins["Winner"] == "Smart"]

    random_win_types = random_wins_df["Win Type"].value_counts()
    smart_win_types = smart_wins_df["Win Type"].value_counts()

    #plors win type for random
    sns.barplot(x=random_win_types.index, y=random_win_types.values, palette="Blues")
    plt.title("Win Type Distribution - Random Agent")
    plt.ylabel("Number of Wins")
    plt.xlabel("Win Type")
    plt.grid(axis="y")
    plt.show()

    #plots win type for rule based
    sns.barplot(x=smart_win_types.index, y=smart_win_types.values, palette="Greens")
    plt.title("Win Type Distribution - Smart Agent")
    plt.ylabel("Number of Wins")
    plt.xlabel("Win Type")
    plt.grid(axis="y")
    plt.show()


def smart_vs_minimax(display_function, check_winner_function, is_full_function):
    import os, time, tracemalloc, csv
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt

    #only 100 runs because it takes a while to load only 100 on my laptop
    runs = 100
    os.system('cls||clear')
    print("Loading...")

    with open("smart_vs_minimax_per_game.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Game", "Winner", "Execution Time (s)", "Memory Usage (KB)", "Win Type"])

        for game_num in range(0, runs):
            board = [[" " for _ in range(7)] for _ in range(6)]
            tracemalloc.start()
            start_time = time.time()

            winner = "Draw"
            win_type = "None"

            while True:
                # Smart Agent move
                col = smart_agent_move(board, display_function, check_winner_function, '●', displayed=False)
                won, win_type_candidate = check_winner_function(board, '●')
                if won:
                    winner = "Smart"
                    win_type = win_type_candidate
                    break
                if is_full_function(board):
                    break

                # MiniMax Agent move
                minimax_agent = Minimax_Agent(depth=4)
                col = minimax_agent.best_move(board, check_winner_function, is_full_function)
                for row in range(5, -1, -1):
                    if board[row][col] == " ":
                        board[row][col] = '○'
                        break
                won, win_type_candidate = check_winner_function(board, '○')
                if won:
                    winner = "MiniMax"
                    win_type = win_type_candidate
                    break
                if is_full_function(board):
                    break

            end_time = time.time()
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            execution_time = round(end_time - start_time, 4)
            memory_kb = round(peak / 1024, 2)

            writer.writerow([game_num, winner, execution_time, memory_kb, win_type])

    os.system('cls||clear')

    # Load data
    df = pd.read_csv("smart_vs_minimax_per_game.csv")

    # Plot win counts
    sns.countplot(data=df, x="Winner", palette="pastel")
    plt.title("Game Outcomes: Smart vs MiniMax")
    plt.show()

    # Plot execution time per game
    sns.lineplot(data=df, x="Game", y="Execution Time (s)", label="Execution Time")
    plt.title("Execution Time per Game")
    plt.ylabel("Time (s)")
    plt.grid(True)
    plt.show()

    # Plot memory usage per game
    sns.lineplot(data=df, x="Game", y="Memory Usage (KB)", color="purple")
    plt.title("Memory Usage per Game")
    plt.ylabel("Memory (KB)")
    plt.xlabel("Game Number")
    plt.grid(True)
    plt.show()

    # Plot overall win type distribution (excluding draws)
    win_type_counts = df[df["Win Type"] != "None"]["Win Type"].value_counts()
    sns.barplot(x=win_type_counts.index, y=win_type_counts.values, palette="muted")
    plt.title("Overall Win Type Distribution")
    plt.ylabel("Number of Wins")
    plt.xlabel("Win Type")
    plt.grid(axis="y")
    plt.show()

    # Separate graphs for each agent
    df_wins = df[df["Winner"] != "Draw"]
    smart_wins_df = df_wins[df_wins["Winner"] == "Smart"]
    minimax_wins_df = df_wins[df_wins["Winner"] == "MiniMax"]

    smart_win_types = smart_wins_df["Win Type"].value_counts()
    minimax_win_types = minimax_wins_df["Win Type"].value_counts()

    sns.barplot(x=smart_win_types.index, y=smart_win_types.values, palette="Greens")
    plt.title("Win Type Distribution - Smart Agent")
    plt.ylabel("Number of Wins")
    plt.xlabel("Win Type")
    plt.grid(axis="y")
    plt.show()

    sns.barplot(x=minimax_win_types.index, y=minimax_win_types.values, palette="Blues")
    plt.title("Win Type Distribution - MiniMax Agent")
    plt.ylabel("Number of Wins")
    plt.xlabel("Win Type")
    plt.grid(axis="y")
    plt.show()



def ml_vs_minimax(display_function, check_winner_function, is_full_function):
    import os, time, tracemalloc, csv
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt

    #only 100 runs because it takes a while to load only 100 on my laptop
    runs = 100
    os.system('cls||clear')
    print("Loading...")

    ml_agent = MachineLearningAgent(player_symbol='●')

    with open("ml_vs_minimax_per_game.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Game", "Winner", "Execution Time (s)", "Memory Usage (KB)", "Win Type"])

        for game_num in range(runs):
            board = [[" " for _ in range(7)] for _ in range(6)]
            minimax_agent = Minimax_Agent(depth=4)

            tracemalloc.start()
            start_time = time.time()

            winner = "Draw"
            win_type = "None"

            while True:
                col = ml_agent.choose_move(board)
                for row in range(5, -1, -1):
                    if board[row][col] == " ":
                        board[row][col] = '●'
                        break

                won, win_type_candidate = check_winner_function(board, '●')
                if won:
                    winner = "Machine Learning"
                    win_type = win_type_candidate
                    break
                if is_full_function(board):
                    break

                minimax_agent = Minimax_Agent(depth=4)
                col = minimax_agent.best_move(board, check_winner_function, is_full_function)
                for row in range(5, -1, -1):
                    if board[row][col] == " ":
                        board[row][col] = '○'
                        break

                won, win_type_candidate = check_winner_function(board, '○')
                if won:
                    winner = "MiniMax"
                    win_type = win_type_candidate
                    break
                if is_full_function(board):
                    break

            end_time = time.time()
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            execution_time = round(end_time - start_time, 4)
            memory_kb = round(peak / 1024, 2)

            writer.writerow([game_num, winner, execution_time, memory_kb, win_type])

    os.system('cls||clear')

    # Load and visualize results
    df = pd.read_csv("ml_vs_minimax_per_game.csv")

    sns.countplot(data=df, x="Winner", palette="Set2")
    plt.title("Game Outcomes: Machine Learning vs MiniMax")
    plt.show()

    sns.lineplot(data=df, x="Game", y="Execution Time (s)")
    plt.title("Execution Time per Game")
    plt.ylabel("Time (s)")
    plt.grid(True)
    plt.show()

    sns.lineplot(data=df, x="Game", y="Memory Usage (KB)", color="purple")
    plt.title("Memory Usage per Game")
    plt.ylabel("Memory (KB)")
    plt.xlabel("Game Number")
    plt.grid(True)
    plt.show()

    win_type_counts = df[df["Win Type"] != "None"]["Win Type"].value_counts()
    sns.barplot(x=win_type_counts.index, y=win_type_counts.values, palette="muted")
    plt.title("Overall Win Type Distribution")
    plt.ylabel("Number of Wins")
    plt.xlabel("Win Type")
    plt.grid(axis="y")
    plt.show()

    df_wins = df[df["Winner"] != "Draw"]
    ml_wins_df = df_wins[df_wins["Winner"] == "Machine Learning"]
    minimax_wins_df = df_wins[df_wins["Winner"] == "MiniMax"]

    ml_win_types = ml_wins_df["Win Type"].value_counts()
    minimax_win_types = minimax_wins_df["Win Type"].value_counts()

    sns.barplot(x=ml_win_types.index, y=ml_win_types.values, palette="Blues")
    plt.title("Win Type Distribution - Machine Learning Agent")
    plt.ylabel("Number of Wins")
    plt.xlabel("Win Type")
    plt.grid(axis="y")
    plt.show()

    sns.barplot(x=minimax_win_types.index, y=minimax_win_types.values, palette="Oranges")
    plt.title("Win Type Distribution - MiniMax Agent")
    plt.ylabel("Number of Wins")
    plt.xlabel("Win Type")
    plt.grid(axis="y")
    plt.show()
