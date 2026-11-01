from life.board import ALIVE, DEAD

CHAR_TO_STATE = {"0": DEAD, "1": ALIVE}


def load_board_state(path):
    with open(path) as f:
        lines = [line.strip() for line in f if line.strip()]

    if not lines:
        raise ValueError(f"{path} is empty")

    width = len(lines[0])
    board = []
    for number, line in enumerate(lines, start=1):
        if len(line) != width:
            raise ValueError(
                f"{path}: row {number} has {len(line)} cells, expected {width}"
            )
        row = []
        for char in line:
            if char not in CHAR_TO_STATE:
                raise ValueError(f"{path}: row {number} has invalid character {char!r}")
            row.append(CHAR_TO_STATE[char])
        board.append(row)
    return board