import os


from Agents.RandomAgent import random_agent_move
from Agents.SmartAgent import smart_agent_move
from Agents.MiniMaxAgent import AI_minimax_Agent

def manual_play_game(display_function, check_winner_function, is_full_function, selected_agent):
    board = [[" " for _ in range(7)] for _ in range(6)]

    os.system('cls||clear')
    print("Game Start!")
    display_function(board)

    minimax_agent = None
    if selected_agent == "MiniMax":
        minimax_agent = AI_minimax_Agent()

    while True:
        # Player move
        player_move(board, display_function)
        if check_winner_function(board, '●'):
            print("You win!")
            return
        if is_full_function(board):
            print("It's a draw.")
            return

        # AI move
        if selected_agent == "Random":
            random_agent_move(board, display_function, '○', displayed=True)

        elif selected_agent == "Smart":
            smart_agent_move(board, display_function, check_winner_function, '○', displayed=True)

        elif selected_agent == "MiniMax":
            col = minimax_agent.best_move(board, check_winner_function, is_full_function)
            for row in range(5, -1, -1):
                if board[row][col] == " ":
                    board[row][col] = '○'
                    break
            os.system('cls||clear')
            display_function(board)
            print(f"MiniMax Agent placed at ({col}).")

        elif selected_agent == "ML":
            print("ML agent not implemented yet.")
            return

        if check_winner_function(board, '○'):
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
