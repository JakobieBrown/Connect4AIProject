from config import BOARD_WIDTH, CELL_SIZE

class InputHandler:
    
    @staticmethod
    def get_hovered_column(mouse_pos):
        x = mouse_pos[0]
        if 0 <= x < BOARD_WIDTH * CELL_SIZE:
            return x // CELL_SIZE
        return None
    
    @staticmethod
    def get_column_from_click(mouse_pos):
        col = InputHandler.get_hovered_column(mouse_pos)
        return col if col is not None else None
