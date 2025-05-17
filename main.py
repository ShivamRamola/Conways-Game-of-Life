"""
Main entry point for Conway's Game of Life.
"""
from game_logic import GameBoard
from gui import GameGUI
from io_operations import save_pattern, load_pattern
from config import parse_args

def main():
    # Initialize game
    args = parse_args()
    game = GameBoard(args.width, args.height)
    gui = GameGUI(args.width, args.height)
    
    running = True
    paused = True

    while running:
        # Handle events
        action = gui.handle_events()
        if action == "QUIT":
            running = False
        elif action == "TOGGLE_PAUSE":
            paused = not paused
        elif action == "STEP" and paused:
            game.next_generation()
        elif action == "RANDOM":
            game.randomize()
        elif action == "CLEAR":
            game.clear()
        elif action == "SAVE":
            save_pattern(game.board)
        elif action == "LOAD":
            game.board = load_pattern(game.width, game.height)

        # Handle mouse input
        mouse_action = gui.get_mouse_cell()
        if mouse_action:
            x, y, state = mouse_action
            game.set_cell(x, y, state)

        # Update game state
        if not paused:
            game.next_generation()

        # Draw everything
        gui.draw(game.board, game.generation)
        gui.tick(args.fps)

    gui.quit()

if __name__ == "__main__":
    main()
