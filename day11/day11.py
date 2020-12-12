import sys
import time
import numpy as np

class ConwayBoard():
    def __init__(self, board):
        self.board = np.array(board, dtype=int)
        self.occupied_neighbors = np.empty_like(self.board)
        self.dimensions = self.board.shape

    def __str__(self):
        return str(self.board)

    def compute_neighbors(self):
        for i, line in enumerate(self.board):
            for j, element in enumerate(line):
                self.occupied_neighbors[i][j] = self.get_occupied_neighbors(i, j)

    def get_occupied_neighbors(self, x, y):
        counter = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i >= 0 and i < self.dimensions[0] and j >= 0 and j < self.dimensions[1] and (i - x != 0 or j - y != 0) and self.board[i][j] == 2:
                    counter += 1
        return counter

    def get_occupied_neighbors_far(self, x, y):
        pass

    def update_board(self):
        self.compute_neighbors()
        changed = False
        for i, line in enumerate(self.board):
            for j, element in enumerate(line):
                if element == 1 and self.occupied_neighbors[i][j] == 0:
                    self.board[i][j] = 2
                    changed = True
                elif element == 2 and self.occupied_neighbors[i][j] >= 4:
                    self.board[i][j] = 1
                    changed = True
        return changed

def get_input():
    with open(sys.argv[2], 'r') as f:
        for line in f:
            yield parse_line(line)
    return

def char_to_int(char):
    if char == 'L':
        return 1
    elif char == '.':
        return 0
    elif char == '#':
        return 2

def parse_line(line):
    return list(map(char_to_int, line.strip()))

def part1():
    conway_board = ConwayBoard(list(get_input()))
    counter = 0
    while conway_board.update_board():
        print(f'{counter}  ', end='\r')
        counter += 1
    return sum([sum([1 for elem in line if elem == 2]) for line in conway_board.board])

def part2():
    pass

if __name__ == '__main__':
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
