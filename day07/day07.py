import sys
import re

class Node():
    def __init__(self, name):
        self.name = name
        self.children = dict()
        self.parents = dict()

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return "<Node %s>" % self.name

    def add_child(self, child_name, distance=0):
        self.children[child_name] = distance

    def get_children(self):
        return self.children

    def add_parent(self, parent_name, distance=0):
        self.parents[parent] = distance

    def get_parents(self):
        return self.parents

def get_input():
    with open(sys.argv[2], 'r') as f:
        node_set = set()
        for line in f:
            yield parse_line(line)
    return

def parse_line(line):
    first_part, second_part = line.strip().split('contain')
    first_node_name = first_part[:-6]
    first_node = Node(first_node_name)

    parser = re.compile('([0-9]+) ([a-z ]*) bags')
    matches = parser.finditer(second_part)

    for match in matches:
        number = int(match.group(1))
        name = match.group(2)
        first_node.add_child(name, number)

    return first_node

def part1():
    nodes = get_input()
    for node in nodes:
        print(node)
        for child, distance in node.get_children().items():
            print('    ' + child + ' ' + str(distance))

def part2():
    pass

if __name__ == '__main__':
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
