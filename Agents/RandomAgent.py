

import random
import os
import time


def random_agent_move(board, display_function, icon, displayed):

  random_cell = random.randint(0,6)
  while True:
    if board[0][random_cell] == " ":
        
        row = range(5,-1,-1)
        for i in row:
            if board[i][random_cell] == " ":
                board[i][random_cell] = icon

                if displayed:
                    print("Random move...")
                    time.sleep(1)
                    os.system('cls||clear')
                    display_function(board)
                    print(f"Random Agent placed at ({random_cell})")
                break
            elif all(board[0][col] != " " for col in range(7)):
                return

        break
    else:
        random_cell = random.randint(0,6)