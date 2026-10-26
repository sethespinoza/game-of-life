import random

ALIVE = 1
DEAD = 0

def dead_state(width, height):
    board = []
    for row in range(height):
        new_row = []
        for col in range(width):
            new_row.append(DEAD)
        board.append(new_row)
    return board

def random_state(width, height):
    board = dead_state(width, height)
    for row in range(height):
        for col in range(width):
            if random.random() >= 0.5:
                board[row][col] = ALIVE
    return board

