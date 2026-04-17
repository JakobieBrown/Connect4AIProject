import pygame
from config import COLORS, BOARD_WIDTH, BOARD_HEIGHT, CELL_SIZE, PIECE_RADIUS
from graphics.piece_renderer import PieceRenderer

class BoardRenderer:    
    def __init__(self, screen):
        self.screen = screen
        self.piece_renderer = PieceRenderer(screen)
    
    def draw_board(self, board_state):
        # - fill pygame surface with color https://www.pygame.org/docs/ref/surface.html#pygame.Surface.fill
        self.screen.fill(COLORS['background'])
        
        # drawing the board state
        for row in range(BOARD_HEIGHT):
            for col in range(BOARD_WIDTH):
                piece = board_state[row][col]
                self.piece_renderer.draw_piece(BOARD_HEIGHT-row, col, piece)
    
    def draw_column_indicator(self, hovered_col, piece):
        if hovered_col is None:
            return
        x = hovered_col * CELL_SIZE + CELL_SIZE // 2
        y = CELL_SIZE // 2
        color = COLORS[f'piece_{piece}']
        #drawing circles in pygame https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle
        pygame.draw.circle(self.screen, color, (x, y), PIECE_RADIUS)
