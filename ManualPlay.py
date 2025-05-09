import os
import time

from Agents.RandomAgent import random_agent_move
from Agents.SmartAgent import smart_agent_move
from Agents.MiniMaxAgent import Minimax_Agent
from Agents.MachineLearningAgent import MachineLearningAgent

ml_agent = MachineLearningAgent()

def manual_play_game(display_function, check_winner_function, is_full_function, selected_agent):
    board = [[" " for _ in range(7)] for _ in range(6)]

    def check_win_only(board, player):
        result = check_winner_function(board, player)
        return result if isinstance(result, bool) else result[0]

    os.system('cls||clear')
    print("Game Start!")
    display_function(board)

    minimax_agent = None
    if selected_agent == "MiniMax":
        minimax_agent = Minimax_Agent()

    while True:
        # Player move
        player_move(board, display_function)
        won = check_win_only(board, '●')
        if won:
            print("You win!")
            return
        if is_full_function(board):
            print("It's a draw.")
            return

        # AI move
        if selected_agent == "Random":
            random_agent_move(board, display_function, '○', displayed=True)

        elif selected_agent == "Smart":
            smart_agent_move(board, display_function, lambda b, p: check_winner_function(b, p), '○', displayed=True)

        elif selected_agent == "Mini-Max":
            minimax_agent = Minimax_Agent()
            col = minimax_agent.best_move(board, check_winner_function, is_full_function)
            for row in range(5, -1, -1):
                if board[row][col] == " ":
                    board[row][col] = '○'
                    print("Mini-Max Move...")
                    time.sleep(1)
                    os.system('cls||clear')
                    break
            os.system('cls||clear')
            display_function(board)

        elif selected_agent == "ML":
            col = ml_agent.choose_move(board)
            for row in range(5, -1, -1):
                if board[row][col] == " ":
                    board[row][col] = '○'
                    print("Machine Learning Move...")
                    time.sleep(1)
                    os.system('cls||clear')
                    display_function(board)
                    break

        won = check_win_only(board, '○')
        if won:
            print("AI wins!")
            return
        if is_full_function(board):
            print("It's a draw.")
            return


def player_move(board, display_function):
    while True:
        try:
            col = int(input("Enter your move (0-6): "))
            if col < 0 or col > 6:
                raise ValueError
            if board[0][col] == " ":
                for i in range(5, -1, -1):
                    if board[i][col] == " ":
                        board[i][col] = '●'
                        break
                break
            else:
                print("Column Full. Try again.")
        except (ValueError, IndexError):
            os.system('cls||clear')
            display_function(board)
            print("Invalid input. Enter column numbers between 0 and 6.")

    os.system('cls||clear')
    display_function(board)
