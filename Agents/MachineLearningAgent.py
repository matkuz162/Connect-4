import pandas as pd


def row_to_board(row_data):
    board = [["" for _ in range(7)] for _ in range(6)]
    label = row_data[-1]
    flat_board = row_data[:-1]

    for col in range(7):
        for row in range(6):
            board[row][col] = flat_board[col * 6 + row]

    return board, label


df = pd.read_csv("Data/connect-4.data", header=None)
board_data, outcome = row_to_board(df.iloc[0].tolist())

for row in board_data[::-1]:
    print(" ".join(row))

print(f"Result (from Player X's perspective): {outcome}")
