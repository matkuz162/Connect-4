import random
import os
import time
import numpy as np



class AI_minimax_Agent:
    def __init__(self, ai_player='○', human_player='●', depth=4):
        self.ai_player = ai_player
        self.human_player = human_player
        self.max_depth = depth

    def get_valid_columns(self, board):
        return [i for i in range(7) if board[0][i] == " "]

    def make_move(self, board, col, player):
        for row in range(5,-1,-1):
            if board[row][col] == " ":
                board[row][col] = player
                return row
            
    def evaluate_board(self, board):
        def count_windows(window, player):
            return window.count(player) == 3 and window.count(" ") == 1

        score = 0

        # horizontal
        for row in board:
            for col in range(4):
                window = row[col:col+4]
                if count_windows(window, self.ai_player):
                    score += 5
                elif count_windows(window, self.human_player):
                    score -= 4

        # vertical
        for col in range(7):
            for row in range(3):
                window = [board[row+i][col] for i in range(4)]
                if count_windows(window, self.ai_player):
                    score += 5
                elif count_windows(window, self.human_player):
                    score -= 4

        # forward diagonal
        for row in range(3, 6):
            for col in range(4):
                window = [board[row-i][col+i] for i in range(4)]
                if count_windows(window, self.ai_player):
                    score += 5
                elif count_windows(window, self.human_player):
                    score -= 4

        # backwards diagonal
        for row in range(3):
            for col in range(4):
                window = [board[row+i][col+i] for i in range(4)]
                if count_windows(window, self.ai_player):
                    score += 5
                elif count_windows(window, self.human_player):
                    score -= 4

        return score
    
        

    def minimax(self, board, depth, alpha, beta, is_maximizing, check_winner_function, is_full_function):
        if check_winner_function(board, self.ai_player):
            return 1000 - depth
        elif check_winner_function(board, self.human_player):
            return depth - 1000
        elif is_full_function(board) or depth == self.max_depth:
            return self.evaluate_board(board)

        valid_columns = self.get_valid_columns(board)

        if is_maximizing:
            max_eval = float('-inf')
            for col in valid_columns:
                row = self.make_move(board, col, self.ai_player)
                eval = self.minimax(board, depth + 1, alpha, beta, False, check_winner_function, is_full_function)
                board[row][col] = " "
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for col in valid_columns:
                row = self.make_move(board, col, self.human_player)
                eval = self.minimax(board, depth + 1, alpha, beta, True, check_winner_function, is_full_function)
                board[row][col] = " "
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def best_move(self, board, check_winner_function, is_full_function):
        best_score = float('-inf')
        best_cols = []

        for col in self.get_valid_columns(board):
            row = self.make_move(board, col, self.ai_player)
            score = self.minimax(board, 0, float('-inf'), float('inf'), False, check_winner_function, is_full_function)
            board[row][col] = " "

            if score > best_score:
                best_score = score
                best_cols = [col]
            elif score == best_score:
                best_cols.append(col)

        return random.choice(best_cols)


