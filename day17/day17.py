import sys
from collections import defaultdict

class ConwayBoard3D():
    def __init__(self, initial_board):
        self.board = defaultdict(int)
        self.min_x = self.max_x = self.min_y = self.max_y = self.min_z = self.max_z = 0
        self._active_cubes = 0
        for j, row in enumerate(initial_board):
            for i, element in enumerate(row):
                self.board[(i, j, 0)] = element
                self.update_bounds(i, j, 0)
                if element == 1:
                    self._active_cubes += 1
        self.next_board = defaultdict(int, self.board)

    def step(self):
        for z in range(self.min_z - 1, self.max_z + 2):
            for y in range(self.min_y - 1, self.max_y + 2):
                for x in range(self.min_x - 1, self.max_x + 2):
                    if self.active(x, y, z) and not (self.active_neighbors(x, y, z) in (2, 3)):
                        self.deactivate(x, y, z)
                    elif not self.active(x, y, z) and self.active_neighbors(x, y, z) == 3:
                        self.activate(x, y, z)
                        self.update_bounds(x, y, z)
        self.board = defaultdict(int, self.next_board)

    def update_bounds(self, x, y, z):
        if x < self.min_x:
            self.min_x = x
        if x > self.max_x:
            self.max_x = x
        if y < self.min_y:
            self.min_y = y
        if y > self.max_y:
            self.max_y = y
        if z < self.min_z:
            self.min_z = z
        if z > self.max_z:
            self.max_z = z

    def active(self, x, y, z):
        return self.board[(x, y, z)] == 1

    def activate(self, x, y, z):
        self.next_board[(x, y, z)] = 1
        self._active_cubes += 1

    def deactivate(self, x, y, z):
        self.next_board[(x, y, z)] = 0
        self._active_cubes -= 1

    def active_neighbors(self, x, y, z):
        active_neighbors = 0
        for k in range(z - 1, z + 2):
            for j in range(y - 1, y + 2):
                for i in range(x - 1, x + 2):
                    if i != x or j != y or k != z:
                        if self.active(i, j, k):
                            active_neighbors += 1
        return active_neighbors

    def __str__(self):
        string_list = list()
        for z in range(self.min_z, self.max_z + 1):
            string_list.append(f'z={z}')
            for y in range(self.min_y, self.max_y + 1):
                sub_string_list = list()
                for x in range(self.min_x, self.max_x + 1):
                    sub_string_list.append(int_to_char(self.board[(x, y, z)]))
                string_list.append(''.join(sub_string_list))
            string_list.append('\n')
        return '\n'.join(string_list)

    def __repr__(self):
        return self.__str__()

    def active_cubes(self):
        return self._active_cubes

class ConwayBoard4D():
    def __init__(self, initial_board):
        self.board = defaultdict(int)
        self.min_x = self.max_x = self.min_y = self.max_y = self.min_z = self.max_z = self.min_w = self.max_w = 0
        self._active_cubes = 0
        for j, row in enumerate(initial_board):
            for i, element in enumerate(row):
                self.board[(i, j, 0, 0)] = element
                self.update_bounds(i, j, 0, 0)
                if element == 1:
                    self._active_cubes += 1
        self.next_board = defaultdict(int, self.board)

    def step(self):
        for w in range(self.min_w - 1, self.max_w + 2):
            for z in range(self.min_z - 1, self.max_z + 2):
                for y in range(self.min_y - 1, self.max_y + 2):
                    for x in range(self.min_x - 1, self.max_x + 2):
                        if self.active(x, y, z, w) and not (self.active_neighbors(x, y, z, w) in (2, 3)):
                            self.deactivate(x, y, z, w)
                        elif not self.active(x, y, z, w) and self.active_neighbors(x, y, z, w) == 3:
                            self.activate(x, y, z, w)
                            self.update_bounds(x, y, z, w)
        self.board = defaultdict(int, self.next_board)

    def update_bounds(self, x, y, z, w):
        if x < self.min_x:
            self.min_x = x
        if x > self.max_x:
            self.max_x = x
        if y < self.min_y:
            self.min_y = y
        if y > self.max_y:
            self.max_y = y
        if z < self.min_z:
            self.min_z = z
        if z > self.max_z:
            self.max_z = z
        if w < self.min_w:
            self.min_w = w
        if w > self.max_w:
            self.max_w = w

    def active(self, x, y, z, w):
        return self.board[(x, y, z, w)] == 1

    def activate(self, x, y, z, w):
        self.next_board[(x, y, z, w)] = 1
        self._active_cubes += 1

    def deactivate(self, x, y, z, w):
        self.next_board[(x, y, z, w)] = 0
        self._active_cubes -= 1

    def active_neighbors(self, x, y, z, w):
        active_neighbors = 0
        for l in range(w - 1, w + 2):
            for k in range(z - 1, z + 2):
                for j in range(y - 1, y + 2):
                    for i in range(x - 1, x + 2):
                        if i != x or j != y or k != z or l != w:
                            if self.active(i, j, k, l):
                                active_neighbors += 1
        return active_neighbors

    def __str__(self):
        string_list = list()
        for w in range(self.min_w, self.max_w + 1):
            for z in range(self.min_z, self.max_z + 1):
                string_list.append(f'z={z}, w={w}')
                for y in range(self.min_y, self.max_y + 1):
                    sub_string_list = list()
                    for x in range(self.min_x, self.max_x + 1):
                        sub_string_list.append(int_to_char(self.board[(x, y, z, w)]))
                    string_list.append(''.join(sub_string_list))
                string_list.append('\n')
        return '\n'.join(string_list)

    def __repr__(self):
        return self.__str__()

    def active_cubes(self):
        return self._active_cubes

def get_input():
    with open(sys.argv[2], 'r') as f:
        for line in f:
            yield parse_line(line)
    return

def int_to_char(num):
    if num == 0:
        return '.'
    if num == 1:
        return '#'
    return '@'

def char_to_int(char):
    if char == '.':
        return 0
    if char == '#':
        return 1
    return -1

def parse_line(line):
    return map(char_to_int, line.strip())

debug = False

def part1():
    cBoard = ConwayBoard3D(get_input())
    if debug:
        print('Step 0')
        print(cBoard)
    for i in range(6):
        cBoard.step()
        if debug:
            print(f'Step {i + 1}')
            print(cBoard)
    return cBoard.active_cubes()

def part2():
    cBoard = ConwayBoard4D(get_input())
    if debug:
        print('Step 0')
        print(cBoard)
    for i in range(6):
        cBoard.step()
        if debug:
            print(f'Step {i + 1}')
            print(cBoard)
    return cBoard.active_cubes()

if __name__ == '__main__':
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
