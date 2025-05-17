"""
Configuration settings for the Game of Life.
"""
import argparse

# Display settings
CELL_SIZE = 20
GRID_COLOR = (40, 40, 40)
CELL_COLOR = (0, 255, 0)
BACKGROUND_COLOR = (10, 10, 10)
TEXT_COLOR = (255, 255, 255)

def parse_args():
    parser = argparse.ArgumentParser(description='Conway\'s Game of Life')
    parser.add_argument('--width', type=int, default=60)
    parser.add_argument('--height', type=int, default=30)
    parser.add_argument('--fps', type=int, default=10)
    return parser.parse_args()
