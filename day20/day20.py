import sys
import numpy as np

class Tile():
    def __init__(self, id, board):
        self.id = id
        self.board = board
        # N, E, S, W
        self.edge_values = list()
        self.edge_values.append(to_number(self.board[0]))
        self.edge_values.append(to_number(self.board.T[len(self.board) - 1]))
        self.edge_values.append(to_number(self.board[len(self.board) - 1]))
        self.edge_values.append(to_number(self.board.T[0]))

    def __str__(self):
        return f'    {self.edge_values[0]: 4d}    \n' + \
               f'{self.edge_values[3]: 4d}    {self.edge_values[1]: 4d}\n' + \
               f'    {self.edge_values[2]: 4d}    '

    def __repr__(self):
        return f'<Board=<id={self.id}>,<edges={self.edge_values}>>'

def to_number(lst):
    string = ''.join(map(str, lst))
    print(string)
    number1 = int(string, 2)
    number2 = int(string[::-1], 2)
    return min(number1, number2)

def get_input():
    with open(sys.argv[2], 'r') as f:
        for line in f:
            yield parse_line(line)
    return

def parse_line(line):
    return line.strip()

def char_to_int(char):
    if char == '#':
        return 1
    elif char == '.':
        return 0

def int_to_char(number):
    if number == 1:
        return '#'
    elif number == 0:
        return '.'

def parse_tiles():
    state = 0
    tiles = []
    for line in get_input():
        if state == 0:
            number = int(line[5:-1])
            print(number)
            state = 1
            board = []
        elif state == 1:
            if line == '':
                state = 0
                tiles.append(Tile(number, np.array(board, dtype=int)))
            else:
                board.append(list(map(char_to_int, line)))
    return tiles

def part1():
    tiles = parse_tiles()
    for tile in tiles:
        print(tile.id)
        print(tile)

def part2():
    pass

if __name__ == '__main__':
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
