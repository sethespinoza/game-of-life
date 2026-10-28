from life.board import ALIVE, DEAD, dead_state


def count_live_neighbors(board, row, col):
    height = len(board)
    width = len(board[0])
    count = 0
    for d_row in (-1, 0, 1):
        for d_col in (-1, 0, 1):
            if d_row == 0 and d_col == 0:
                continue
            r = row + d_row
            c = col + d_col
            if 0 <= r < height and 0 <= c < width:
                if board[r][c] == ALIVE:
                    count += 1
    return count

def next_cell_state(current, live_neighbors):
    if current == ALIVE:
        if live_neighbors == 2 or live_neighbors == 3:
            return ALIVE
        return DEAD
    if live_neighbors == 3:
        return ALIVE
    return DEAD

def next_board_state(board):
    height = len(board)
    width = len(board[0])
    new_board = dead_state(width, height)
    for row in range(height):
        for col in range(width):
            neighbors = count_live_neighbors(board, row, col)
            new_board[row][col] = next_cell_state(board[row][col], neighbors)
    return new_board

