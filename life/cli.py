import time

from life.board import random_state
from life.render import board_to_text
from life.rules import next_board_state

WIDTH = 40
HEIGHT = 20
DELAY = 0.1
CLEAR = "\033[H\033[J"


def run(board, delay=DELAY):
    generation = 0
    try:
        while True:
            print(CLEAR + board_to_text(board))
            print(f"Generated: {generation} boards (Ctrl+C to quit)")
            board = next_board_state(board)
            generation += 1
            time.sleep(delay)
    except KeyboardInterrupt:
        print("\nStopped.")


def main():
    run(random_state(WIDTH, HEIGHT))


if __name__ == "__main__":
    main()
