import pygame
from config import COLORS, CELL_SIZE, PIECE_RADIUS

class PieceRenderer:    
    def __init__(self, screen):
        self.screen = screen
    
    def draw_piece(self, row, col, piece):
        x = col * CELL_SIZE + CELL_SIZE // 2
        y = row * CELL_SIZE + CELL_SIZE // 2
        
        color = COLORS[f'piece_{piece}']
        #drawing circles in pygame https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle
        pygame.draw.circle(self.screen, color, (x, y), PIECE_RADIUS)
