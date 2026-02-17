import time
import os

class Array:
    def __init__(self, size):
        self.size = size
        self.data = [0] * size

    def get(self, index):
        if 0 <= index < self.size:
            return self.data[index]
        else:
            return 0

    def set(self, index, value):
        if 0 <= index < self.size:
            self.data[index] = value

    def get_size(self):
        return self.size


class GameOfLife:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = Array(rows)

        for i in range(rows):
            self.grid.set(i, Array(cols))

    def set_cell(self, row, col, value):
        self.grid.get(row).set(col, value)

    def get_cell(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.grid.get(row).get(col)
        return 0

    def count_neighbors(self, row, col):
        count = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                count += self.get_cell(row + i, col + j)
        return count

    def next_generation(self):
        new_grid = GameOfLife(self.rows, self.cols)

        for i in range(self.rows):
            for j in range(self.cols):
                neighbors = self.count_neighbors(i, j)
                current = self.get_cell(i, j)

                if current == 1 and neighbors in [2, 3]:
                    new_grid.set_cell(i, j, 1)
                elif current == 0 and neighbors == 3:
                    new_grid.set_cell(i, j, 1)
                else:
                    new_grid.set_cell(i, j, 0)

        self.grid = new_grid.grid

    def display(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.get_cell(i, j) == 1:
                    print("■", end=" ")
                else:
                    print(".", end=" ")
            print()
        print()


# ===== PROGRAM UTAMA =====
game = GameOfLife(10, 10)

# Pola awal (glider)
game.set_cell(1, 2, 1)
game.set_cell(2, 3, 1)
game.set_cell(3, 1, 1)
game.set_cell(3, 2, 1)
game.set_cell(3, 3, 1)

for _ in range(10):
    os.system('cls' if os.name == 'nt' else 'clear')
    game.display()
    game.next_generation()
    time.sleep(0.5)
