from life.board import ALIVE

ALIVE_CHAR = "#"
DEAD_CHAR = " "

def board_to_text(board):
    width = len(board[0])
    border = "-" * (width + 2)

    rows = []
    for row in board:
        cells = ""
        for cell in row:
            if cell == ALIVE:
                cells += ALIVE_CHAR
            else:
                cells += DEAD_CHAR
        
        rows.append("|" + cells + "|")
    return "\n".join([border] + rows + [border])


def render(board):
    print(board_to_text(board))
