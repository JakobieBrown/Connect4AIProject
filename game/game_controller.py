from game.board import Board
from config import BOARD_WIDTH, BOARD_HEIGHT

class GameController:    
    def __init__(self):
        self.board = Board(BOARD_WIDTH, BOARD_HEIGHT)
        self.current_player = 1  # Player 1 starts
        self.game_over = False
        self.winner = None
    
    def process_move(self, col):        
        self.board.make_move(col, self.current_player)
        if self.check_win(col, self.current_player):
            self.game_over = True
            self.winner = self.current_player
        elif self.check_draw():
            self.game_over = True
            self.winner = 0
        else:
            self.current_player = (self.current_player % 2) + 1

    # def revert_move(self, col):
    #     self.board.undo_move(col)
    #     self.game_over = False
    #     self.winner = None
    #     self.current_player = (self.current_player % 2) + 1
            
    def check_win(self, col, player):
        # Get the row where the piece was placed
        row = self.board.column_heights[col] - 1
        
        # Check horizontal, vertical, and diagonal
        return (self._check_direction(row, col, 0, 1, player) or   # Horizontal
                self._check_direction(row, col, 1, 0, player) or   # Vertical
                self._check_direction(row, col, 1, 1, player) or   # Diagonal /
                self._check_direction(row, col, 1, -1, player))    # Diagonal \
    
    def check_draw(self): #return true if no valid moves remain
        if len(self.board.get_valid_moves()):
            return False
        return True
    
    def _check_direction(self, row, col, dr, dc, player):
        count = 1  # Count the piece we just placed
        
        # Check in positive direction
        r, c = row + dr, col + dc
        while 0 <= r < self.board.height and 0 <= c < self.board.width:
            if self.board.grid[r][c] == player:
                count += 1
            else:
                break
            r, c = r + dr, c + dc
        
        # Check in negative direction
        r, c = row - dr, col - dc
        while 0 <= r < self.board.height and 0 <= c < self.board.width:
            if self.board.grid[r][c] == player:
                count += 1
            else:
                break
            r, c = r - dr, c - dc
        
        # return true if the total counted pieces from both directions is greater than or equal to 4 else false
        return count >= 4 
    
    def reset(self):
        self.board.reset()
        self.current_player = 1
        self.game_over = False
        self.winner = None

    def is_valid_move(self, col):
        return self.board.is_valid_move(col)
    
    def get_valid_moves(self):
        return self.board.get_valid_moves()
    
    def get_heights(self):
        return self.board.get_heights()

    def get_successor(self, col):
        successor = GameController()
        successor.current_player = self.current_player
        successor.game_over = self.game_over
        successor.winner = self.winner
        successor.board = Board(self.board.width,self.board.height)
        successor.board.column_heights = self.board.get_heights()
        successor.board.grid = self.board.get_grid()
        successor.process_move(col)
        return successor

    def get_hash(self):
        return str(self.current_player) + self.board.get_hash()        
            
            
