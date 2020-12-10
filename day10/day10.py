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

def possibilities_from(items, index):
    sum = 0
    index_offset = 1
    while index + index_offset < len(items) and items[index + index_offset] <= items[index] + 3:
        sum += 1
        index_offset += 1
    return sum

def part2():
    joltages = list(get_input())
    joltages.append(0)
    sorted_joltages = sorted(joltages)
    sorted_joltages.append(sorted_joltages[-1] + 3)
    print(sorted_joltages)
    for i in range(len(sorted_joltages)):
        print(possibilities_from(sorted_joltages, i))
    return

if __name__ == '__main__':
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
