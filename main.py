from ui.game_window import GameWindow
from game.game_controller import GameController
import random
from ai.aiconfig import AIConfig
from ai.planning_agent import PlanningAgent
import argparse
import threading
from testing.tests import TestTool


# -- Parsing command line arguments https://docs.python.org/3/library/argparse.html
def parse_arguments():
    """Parse command-line arguments for player control."""
    parser = argparse.ArgumentParser(
        description="Connect 4"
    )
    parser.add_argument('--player1', action='store_true')
    parser.add_argument('--player2', action='store_true')
    parser.add_argument('--depth', type=int, default=5)
    parser.add_argument('--fps', type=int, default=30)
    parser.add_argument('--test', action='store_true')
    
    args = parser.parse_args()
    
    return AIConfig(args.player1, args.player2), args.depth, args.fps, args.test


def main(ai_config, ai_depth, fps, testing = False):
    window = GameWindow(fps)
    controller = GameController()
    ai_agent = PlanningAgent()
    ai_thinking = False
    ai_thread = threading.Thread(target=ai_agent.get_move, args=([controller, ai_depth]))
    
    # -- Pygame Game Loop https://www.pygame.org/docs/
    while window.running:
        window.handle_events()
        if not controller.game_over:
            if ai_config.is_ai(controller.current_player):
                if not ai_thinking: # Start AI Thread
                    ai_thinking=True
                    ai_thread.start()
                if ai_agent.move is not None: # Triggers after AI makes decision
                    ai_thinking = False
                    controller.process_move(ai_agent.move)
                    ai_agent.reset()
                    ai_thread = threading.Thread(target=ai_agent.get_move, args=([controller, ai_depth]))
            else:
                if window.selected_col is not None and controller.board.is_valid_move(window.selected_col):
                    controller.process_move(window.selected_col)

        window.render_board(controller.board.get_grid())
        if not controller.game_over:
            if not ai_config.is_ai(controller.current_player):
                window.render_indicator(controller.current_player)
        else:
            window.render_results(controller.winner)
            if testing: window.running = False
        window.update()

if __name__ == "__main__":
    ai_config, ai_depth, fps, testing = parse_arguments()
    if testing:
        ai_config = AIConfig(True,True)
        for i in range(1,ai_depth+1):
            TestTool.reset()
            TestTool.set_depth(i)
            TestTool.start_timer()
            main(ai_config, i, fps, testing)
            TestTool.end_timer()
            TestTool.save_results()
        TestTool.plot_results()
    else:
        main(ai_config, ai_depth, fps)
