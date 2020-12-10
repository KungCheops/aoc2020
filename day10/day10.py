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

def number_of_jumps_from(items, index):
    sum = 0
    index_offset = 1
    while index + index_offset < len(items) and items[index + index_offset] <= items[index] + 3:
        sum += 1
        index_offset += 1
    return sum

precomputed = dict()

def jump_combinations(jump_list, index=0, depth=0):
    if index in precomputed:
        return precomputed[index]
    print(f'{index} {depth}    \r', end='', flush=True)
    possibilities = jump_list[index]
    if index == len(jump_list) - 1:
        precomputed[index] = 1
        return 1
    ret = sum([jump_combinations(jump_list, index + i + 1, depth + 1) for i in range(possibilities) if index + i + 1 < len(jump_list)])
    precomputed[index] = ret
    return ret

def part2():
    joltages = list(get_input())
    joltages.append(0)
    sorted_joltages = sorted(joltages)
    sorted_joltages.append(sorted_joltages[-1] + 3)
    jump_list = [number_of_jumps_from(sorted_joltages, i) for i in range(len(sorted_joltages) - 1)]
    print(jump_list)
    return jump_combinations(jump_list, 0)

if __name__ == '__main__':
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
