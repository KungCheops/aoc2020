import sys

class Computer():
    def __init__(self):
        self.memory = dict()
        self.and_mask = 0xfffffffff
        self.or_mask = 0x000000000

    def update_masks(self, mask):
        and_mask_string = mask.replace('X', '1')
        self.and_mask = int(and_mask_string, 2)
        or_mask_string = mask.replace('X', '0')
        self.or_mask = int(or_mask_string, 2)

    def write_to_memory(self, position, data):
        self.memory[position] = (data & self.and_mask) | self.or_mask

    def get_memory_sum(self):
        return sum(self.memory.values())

def get_input():
    with open(sys.argv[2], 'r') as f:
        for line in f:
            yield parse_line(line)
    return

def parse_line(line):
    return line.strip().split(' = ')

def part1():
    computer = Computer()
    for instruction in get_input():
        if instruction[0] == 'mask':
            computer.update_masks(instruction[1])
        elif instruction[0].startswith('mem'):
            computer.write_to_memory(int(instruction[0][4:-1]), int(instruction[1]))
    return computer.get_memory_sum()

def part2():
    pass

if __name__ == '__main__':
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
