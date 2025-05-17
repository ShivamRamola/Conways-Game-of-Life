"""
Contains the core game logic for Conway's Game of Life.
"""

class GameBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0]*width for _ in range(height)]
        self.generation = 0

    def count_neighbors(self, x, y):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                     (0, -1),          (0, 1),
                     (1, -1), (1, 0),  (1, 1)]
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                count += self.board[ny][nx]
        return count

    def next_generation(self):
        new_board = [[0]*self.width for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                neighbors = self.count_neighbors(x, y)
                if self.board[y][x] == 1:
                    if neighbors in [2, 3]:
                        new_board[y][x] = 1
                else:
                    if neighbors == 3:
                        new_board[y][x] = 1
        self.board = new_board
        self.generation += 1

    def set_cell(self, x, y, state):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.board[y][x] = state

    def clear(self):
        self.board = [[0]*self.width for _ in range(self.height)]
        self.generation = 0

    def randomize(self):
        import random
        self.board = [[random.choice([0, 1]) for _ in range(self.width)] 
                     for _ in range(self.height)]
