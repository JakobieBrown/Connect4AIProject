import pygame
from graphics.board_renderer import BoardRenderer
from config import BOARD_WIDTH, BOARD_HEIGHT, CELL_SIZE
from ui.input_handler import InputHandler

class GameWindow:    
    def __init__(self, fps):
        # - initializing pygame https://www.pygame.org/docs/
        pygame.init()
        self.fps = fps
        self.width = (BOARD_WIDTH * CELL_SIZE)
        self.height = (BOARD_HEIGHT * CELL_SIZE + CELL_SIZE)  # extra space for column/turn indicator
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Connect Four")
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.board_renderer = BoardRenderer(self.screen)
        self.hovered_col = None
        self.selected_col = None
    
    def handle_events(self):
        # - handling pygame events https://www.pygame.org/docs/ref/event.html
        self.selected_col = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.WINDOWLEAVE:
                # mouse left window, remove indicator
                self.hovered_col = None
            elif event.type == pygame.MOUSEMOTION:
                # getting mouse position during Mouse Motion event
                self.hovered_col = InputHandler.get_hovered_column(event.pos)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # handling mouse down event
                if event.button == 1:  # Left click
                    self.selected_col = InputHandler.get_column_from_click(event.pos)
        
    
    def render_board(self, board_state):
        self.board_renderer.draw_board(board_state)


    def render_indicator(self, player):
        self.board_renderer.draw_column_indicator(self.hovered_col, player)
        
    def render_results(self, winner):
        font = pygame.font.Font(None,92)
        output_string = f"Player {winner} wins!" if winner else "Draw!"
        text = font.render(output_string, True, (255,255,255))
        # - using Surface.get_rect() for easy centering https://www.pygame.org/docs/ref/surface.html#pygame.Surface.get_rect
        rect = text.get_rect(center = (BOARD_WIDTH*CELL_SIZE//2, CELL_SIZE//2))
        self.screen.blit(text, rect)

    def update(self):
        # - update pygame display https://www.pygame.org/docs/ref/display.html#pygame.display.flip
        self.clock.tick(self.fps)
        pygame.display.flip()

    def close(self):
        # - quit pygame before closing https://www.pygame.org/docs/ref/pygame.html#pygame.quit
        pygame.quit()

