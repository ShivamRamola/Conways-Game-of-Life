"""
Contains file I/O operations for saving and loading game states.
"""

def save_pattern(board, filename="pattern.txt"):
    """Save the current board state to a file."""
    with open(filename, "w") as file:
        for row in board:
            file.write("".join(map(str, row)) + "\n")

def load_pattern(width, height, filename="pattern.txt"):
    """Load a board state from a file."""
    import os
    if not os.path.exists(filename):
        print(f"File '{filename}' not found.")
        return [[0] * width for _ in range(height)]

    with open(filename, "r") as file:
        return [list(map(int, line.strip())) for line in file]
