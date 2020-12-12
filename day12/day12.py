import sys
import numpy as np

debug = False

class Action():
    pass

dir_values = {'N': np.array([0,-1]), 'E': np.array([1, 0]), 'S': np.array([0, 1]), 'W': np.array([-1, 0])}
class MoveAction(Action):
    def __init__(self, dir, value):
        self.move = dir_values[dir]
        self.dir = dir
        self.value = value

    def __str__(self):
        return f'{self.dir}{self.value}'

    def __repr__(self):
        return self.__str__()

class TurnAction(Action):
    def __init__(self, direction, angle):
        self.dir = direction
        self.value = angle
        theta = np.radians(angle)
        c, s = np.cos(theta), np.sin(theta)
        if direction == 'L':
            self.matrix = np.array(((c, -s), (s, c)), dtype=int)
        elif direction == 'R':
            self.matrix = np.array(((c, s), (-s, c)), dtype=int)

    def __str__(self):
        return f'{self.dir}{self.value}'

    def __repr__(self):
        return self.__str__()

class ForwardAction(Action):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'F{self.value}'

    def __repr__(self):
        return self.__str__()

class Ship():
    def __init__(self, dir=(1,0), pos=(0,0)):
        self.dir = np.array(dir)
        self.pos = np.array(pos)

    def take_action(self, action):
        if isinstance(action, MoveAction):
            self.pos += action.move * action.value
        elif isinstance(action, TurnAction):
            self.dir = np.matmul(self.dir, action.matrix)
        elif isinstance(action, ForwardAction):
            self.pos += self.dir * action.value

    def __str__(self):
        return f'<ship>: dir={self.dir} pos={self.pos}'

    def __repr__(self):
        return self.__str__()

class Waypoint():
    def __init__(self, pos=(10,-1)):
        self.pos = np.array(pos)

    def take_action(self, action):
        if isinstance(action, MoveAction):
            self.pos += action.move * action.value
        elif isinstance(action, TurnAction):
            self.pos = np.matmul(self.pos, action.matrix)

    def __str__(self):
        return f'<waypoint>: pos={self.pos}'

    def __repr__(self):
        return self.__str__()

def get_input():
    with open(sys.argv[2], 'r') as f:
        for line in f:
            yield parse_line(line)
    return

def parse_line(line):
    line = line.strip()
    dir = line[0]
    value = int(line[1:])
    if dir in ('N', 'S', 'E', 'W'):
        return MoveAction(dir, value)
    elif dir in ('L', 'R'):
        return TurnAction(dir, value)
    elif dir == 'F':
        return ForwardAction(value)
    raise ParseError(f'Not a valid action: {line}')

def part1():
    all_actions = get_input()
    ship = Ship()
    if debug:
        print(ship)
    for action in all_actions:
        ship.take_action(action)
        if debug:
            print(action)
            print(ship)
    return sum(map(abs, ship.pos))

def part2():
    all_actions = get_input()
    ship = Ship()
    waypoint = Waypoint()
    if debug:
        print(ship)
        print(waypoint)
    for action in all_actions:
        if isinstance(action, ForwardAction):
            ship.pos += waypoint.pos * action.value
        else:
            waypoint.take_action(action)
        if debug:
            print(action)
            print(ship)
            print(waypoint)
    return sum(map(abs, ship.pos))

if __name__ == '__main__':
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
