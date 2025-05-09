import joblib
import numpy as np
import os
import pandas as pd

class MLAgent:
    def __init__(self, model_path="knn_model.pkl"):
        self.model = joblib.load(model_path)
        self.column_order = ['col_' + str(i) for i in range(42)]  # 6x7 board
        self.mapping = {' ': 0, 'x': 1, 'o': 2}  # match the training encoding

    def encode_board(self, board, player='x'):
        # Flatten and encode the board
        flat = [self.mapping.get(cell, 0) for row in board for cell in row]
        return pd.DataFrame([flat], columns=self.column_order)

    def get_valid_columns(self, board):
        return [i for i in range(7) if board[0][i] == " "]

    def make_temp_move(self, board, col, player):
        temp = [row.copy() for row in board]
        for row in reversed(range(6)):
            if temp[row][col] == " ":
                temp[row][col] = player
                break
        return temp

    def best_move(self, board, player_token='○'):
        possible_moves = self.get_valid_columns(board)
        move_scores = []

        for col in possible_moves:
            temp_board = self.make_temp_move(board, col, 'x')  # ML model is trained with 'x' as first player
            input_df = self.encode_board(temp_board)
            prediction = self.model.predict(input_df)[0]  # 'win', 'loss', 'draw'
            score = {'win': 2, 'draw': 1, 'loss': 0}.get(prediction, 0)
            move_scores.append((col, score))

        # Pick the move with highest score
        best = max(move_scores, key=lambda x: x[1])
        return best[0]
