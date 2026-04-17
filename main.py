from ui.game_window import GameWindow
from game.game_controller import GameController
import random
from ai.aiconfig import AIConfig
import argparse


# -- Parsing command line arguments https://docs.python.org/3/library/argparse.html
def parse_arguments():
    """Parse command-line arguments for player control."""
    parser = argparse.ArgumentParser(
        description="Connect 4"
    )
    parser.add_argument('--player1', action='store_true')
    parser.add_argument('--player2', action='store_true')
    parser.add_argument('--ai-depth', type=int, default=5)
    
    args = parser.parse_args()
    
    return AIConfig(args.player1, args.player2), args.ai_depth

def main():
    window = GameWindow()
    controller = GameController()
    aiConfig, aiDepth = parse_arguments()
    
    # -- Pygame Game Loop https://www.pygame.org/docs/
    while window.running:
        window.handle_events()

        if not controller.game_over:
            if aiConfig.is_ai(controller.current_player):
                valid_moves = controller.board.get_valid_moves()
                if valid_moves:
                    ai_move = random.choice(valid_moves)
                    controller.process_move(ai_move)
            else:
                if window.selected_col is not None and controller.board.is_valid_move(window.selected_col):
                    controller.process_move(window.selected_col)
            

        window.render_board(controller.board.get_grid())
        if not controller.game_over:
            window.render_indicator(controller.current_player)
        else:
            window.render_results(controller.winner)
        window.update()

if __name__ == "__main__":
    main()
