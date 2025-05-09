#imports
import os
import time

from Agents.RandomAgent import random_agent_move
from Agents.SmartAgent import smart_agent_move
from Agents.MiniMaxAgent import Minimax_Agent
from Agents.MachineLearningAgent import MachineLearningAgent

#starts the machine learning agent
ml_agent = MachineLearningAgent()

# manual game where player against ai
def manual_play_game(display_function, check_winner_function, is_full_function, selected_agent):
    board = [[" " for _ in range(7)] for _ in range(6)]

    #checks if there is a win
    def check_win_only(board, player):
        result = check_winner_function(board, player)
        return result if isinstance(result, bool) else result[0]

    os.system('cls||clear')
    print("Game Start!")
    display_function(board)

    #if the player chose minimax agent it initializes
    minimax_agent = None
    if selected_agent == "MiniMax":
        minimax_agent = Minimax_Agent()

    #game loop
    while True:
        # player move
        player_move(board, display_function)
        won = check_win_only(board, '●')
        #checks if player won
        if won:
            print("You win!")
            return
        #checks for draw
        if is_full_function(board):
            print("It's a draw.")
            return

        #random agent if chosen
        if selected_agent == "Random":
            random_agent_move(board, display_function, '○', displayed=True)

        #smart agent if chosen
        elif selected_agent == "Smart":
            smart_agent_move(board, display_function, lambda b, p: check_winner_function(b, p), '○', displayed=True)

        #minimax agent if chosen
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

        #machine learning if chosen
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

        #checks ai win
        won = check_win_only(board, '○')
        if won:
            print("AI wins!")
            return
        #checks draw
        if is_full_function(board):
            print("It's a draw.")
            return

#player makes a move
def player_move(board, display_function):
    while True:
        #makes a loop until the player enters a valid column and then drops it if free
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

    #displays player move on screen
    os.system('cls||clear')
    display_function(board)
