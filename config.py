from math import sqrt

COLORS = {
    'background': (0, 96, 192),  # light blude
    'piece_0': (0, 48, 96),      # dark blue
    'piece_1': (255, 0, 0),      # red
    'piece_2': (255, 255, 0),    # yellow
}

BOARD_WIDTH = 7
BOARD_HEIGHT = 6
CELL_SIZE = 80
PIECE_RADIUS = (CELL_SIZE-sqrt(CELL_SIZE)) // 2
WINNING_NUMBER = 4
