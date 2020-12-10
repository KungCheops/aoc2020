import sys
from collections import defaultdict

def get_input():
    with open(sys.argv[2], 'r') as f:
        for line in f:
            yield parse_line(line)
    return

def parse_line(line):
    return int(line)

def part1():
    joltages = get_input()
    jump_lengths = defaultdict(int)
    current_joltage = 0
    for joltage in sorted(joltages):
        step = joltage - current_joltage
        jump_lengths[step] += 1
        current_joltage = joltage
    jump_lengths[3] += 1
    print(jump_lengths)
    return jump_lengths[1] * jump_lengths[3]

def part2():
    pass

if __name__ == '__main__':
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
