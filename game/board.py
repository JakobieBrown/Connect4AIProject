class Board:    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.column_heights = [0] * width  # Track next available row in each column
    
    def make_move(self, col, player):
        row = self.column_heights[col]
        self.grid[row][col] = player
        self.column_heights[col] += 1

    def undo_move(self, col):
        self.column_heights[col] -= 1
        row = self.column_heights[col]
        self.grid[row][col] = 0
    
    def get_grid(self):
        return [row[:] for row in self.grid]
    
    def get_heights(self):
        return [e for e in self.column_heights]
    
    def is_valid_move(self, col):
        return 0 <= col < self.width and self.column_heights[col] < self.height
    
    def get_valid_moves(self):
        return [col for col in range(self.width) if self.is_valid_move(col)]
    
    def reset(self):
        self.grid = [[None for _ in range(self.width)] for _ in range(self.height)]
        self.column_heights = [0] * self.width
    
    def get_hash(self):
        ''' builds hash string by columns'''
        hash = ""
        rotated = [list(row) for row in zip(*self.grid[::-1])]
        for row in rotated:
            for element in row:
                hash = hash + str(element)
        return hash