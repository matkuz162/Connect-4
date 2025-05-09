import numpy as np
import joblib
import random
import pandas as pd

class MachineLearningAgent:
    def __init__(self, model_path="machine_learning_model.joblib", encoder_path="machine_learning_label_encoder_y.joblib", player_symbol='○'):
        self.model = joblib.load(model_path)
        self.encoder = joblib.load(encoder_path)
        self.player_symbol = player_symbol
        self.opponent_symbol = '●' if player_symbol == '○' else '○'
        self.mapping = {' ': 0, self.player_symbol: 1, self.opponent_symbol: -1}

    def get_valid_columns(self, board):
        return [col for col in range(7) if board[0][col] == " "]

    def simulate_move(self, board, col, player):
        temp_board = [row[:] for row in board]
        for row in range(5, -1, -1):
            if temp_board[row][col] == " ":
                temp_board[row][col] = player
                break
        return temp_board

    def board_to_features(self, board):
        flat = [self.mapping[cell] for row in board for cell in row]
        df = pd.DataFrame([flat], columns=[f"pos_{i}" for i in range(42)])
        return df

    def choose_move(self, board):
        valid_moves = self.get_valid_columns(board)
        best_move = None
        best_score = -1

        for col in valid_moves:
            simulated = self.simulate_move(board, col, self.player_symbol)
            features = self.board_to_features(simulated)
            prediction = self.model.predict(features)[0]
            outcome_label = self.encoder.inverse_transform([prediction])[0]

            score = {"win": 2, "draw": 1, "loss": 0}.get(outcome_label, 0)

            if score > best_score:
                best_score = score
                best_move = col

        return best_move if best_move is not None else random.choice(valid_moves)
