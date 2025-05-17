"""
GUI implementation using Pygame.
"""
import pygame
from config import CELL_SIZE, GRID_COLOR, CELL_COLOR, BACKGROUND_COLOR, TEXT_COLOR

class GameGUI:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen_width = width * CELL_SIZE
        self.screen_height = height * CELL_SIZE
        
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Conway's Game of Life")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 24)

    def handle_events(self):
        """Handle pygame events and return user actions."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return "TOGGLE_PAUSE"
                elif event.key == pygame.K_n:
                    return "STEP"
                elif event.key == pygame.K_r:
                    return "RANDOM"
                elif event.key == pygame.K_c:
                    return "CLEAR"
                elif event.key == pygame.K_s:
                    return "SAVE"
                elif event.key == pygame.K_l:
                    return "LOAD"
        return None

    def get_mouse_cell(self):
        """Get the cell coordinates from mouse position."""
        if pygame.mouse.get_pressed()[0] or pygame.mouse.get_pressed()[2]:  # Left or right click
            pos = pygame.mouse.get_pos()
            x, y = pos[0] // CELL_SIZE, pos[1] // CELL_SIZE
            return (x, y, 1 if pygame.mouse.get_pressed()[0] else 0)
        return None

    def draw(self, board, generation):
        """Draw the game board and UI."""
        self.screen.fill(BACKGROUND_COLOR)

        # Draw grid and cells
        for y in range(self.height):
            for x in range(self.width):
                rect = (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, GRID_COLOR, rect, 1)
                if board[y][x] == 1:
                    pygame.draw.rect(self.screen, CELL_COLOR, 
                                   (x*CELL_SIZE+1, y*CELL_SIZE+1, 
                                    CELL_SIZE-2, CELL_SIZE-2))

        # Display generation count
        gen_text = self.font.render(f"Generation: {generation}", True, TEXT_COLOR)
        self.screen.blit(gen_text, (10, 10))

        pygame.display.flip()

    def tick(self, fps):
        """Control the game speed."""
        self.clock.tick(fps)

    def quit(self):
        """Clean up pygame."""
        pygame.quit()
