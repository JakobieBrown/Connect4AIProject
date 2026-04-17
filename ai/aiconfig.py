class AIConfig:
    def __init__(self, player1, player2):
        self.config = {
            1: player1,
            2: player2
        }
    
    def is_ai(self, player):
        return self.config[player]