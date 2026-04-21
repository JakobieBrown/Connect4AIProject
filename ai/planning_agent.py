import random 
class PlanningAgent:
    def __init__(self):
        self.eval_look_up = dict()
        self.move = None
        self.heat_map = [[3,4,5,7,5,4,3],
                         [4,6,8,10,8,6,4], 
                         [5,8,11,13,11,8,5],
                         [5,8,11,13,11,8,5],
                         [4,6,8,10,8,6,4],
                         [3,4,5,7,5,4,3]]

    def MiniMax(self, game_state, depth):
        alpha = float("-inf")
        beta = float("inf")
        is_maximizing = game_state.current_player == 1
        best = float("-inf") if is_maximizing else float("inf")
        #valid_moves = self.prioritize_queue(game_state, game_state.get_valid_moves())
        valid_moves = game_state.get_valid_moves()
        best_move = valid_moves[0]
        for move in valid_moves:
            successor_state = game_state.get_successor(move)
            value = self.MiniMaxValue(successor_state,depth -1,alpha,beta)
            if is_maximizing:
                if value > best:
                    best = value
                    best_move = move
                alpha = max(alpha,best)
            else:
                if value < best:
                    best = value
                    best_move = move
                beta = min(beta,best)
            if beta <= alpha:
                break
        return best_move    
    


    def MiniMaxValue(self, game_state, depth, alpha, beta):
        if depth == 0 or game_state.game_over:
            return self.evaluation_function(game_state)
        is_maximizing = game_state.current_player == 1
        best = float("-inf") if is_maximizing else float("inf")
        for move in game_state.get_valid_moves():
            successor_state = game_state.get_successor(move)
            value = self.MiniMaxValue(successor_state, depth-1,alpha, beta)
            if is_maximizing:
                best = max(best,value)
                alpha = max(alpha, best) 
            else:
                best = min(best, value)
                beta = min(beta, best)
            if beta <= alpha:
                break
        return best  

    def evaluation_function(self, game_state):
        return self.evaluate_state(game_state)
        
        
    def evaluate_state(self, game_state):
        if game_state.game_over:
            match(game_state.winner):
                case 1:
                    return float("inf")
                case 2:
                    return float("-inf")
                case _:
                    return 0
        else:
            eval = self.get_board_evaluation(game_state)
            return eval
        
    def get_board_evaluation(self, game_state):

        def mirror(hash):
            '''the hash is 43 chars in length
            [0] indicates the player
            [1]-[42] indicates the elemenents in a grid
            [1]-[6] 0th column
            [7]-[12] 1st column
            [13]-[18] 2nd column
            [19]-[24] 3rd column
            [25]-[30] 4th column
            [31]-[36] 5th column
            [37]-[42] 6th column
            '''
            m_hash = hash[:1]
            for i in range(6,-1,-1): #loops in reverse
                m_hash = m_hash + hash[(6*i):(6*i+6)+1] #builds string from slices
            return m_hash
        
        try:
            return self.eval_look_up[hash]
        except KeyError:
            return self.eval_look_up[mirror(hash)]
        finally:
            eval = self.evaluate_board(game_state)
            self.eval_look_up[hash] = eval
            return eval
        
    def evaluate_board(self, game_state):
        # Add board evaluation Logic here
        return 0

    def prioritize_queue(self, game_state, moves):
        ls = []
        for col in moves:
            row = game_state.get_heights()[col]
            ls.append({'move':col, 'priority':self.heat_map[row][col]})
        ls.sort(key=lambda x: x["priority"], reverse=True)
        return [x["move"] for x in ls]


        
    def get_move(self, controller, depth):
        self.move = self.MiniMax(controller, depth)

    def reset(self):
        self.move = None

        
        
    

