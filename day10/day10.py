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

class JumpList():
    def __init__(self, items, jump_length):
        self.items = sorted(items)
        self.size = len(self.items)
        self.jump_length = jump_length
        self.jumps_from_cache = [-1] * self.size
        self.combinations_cache = [-1] * self.size

    def number_of_jumps_from(self, index):
        if self.jumps_from_cache[index] > -1:
            return self.jumps_from_cache[index]
        sum = 0
        index_offset = 1
        while index + index_offset < self.size and self.items[index + index_offset] <= self.items[index] + 3:
            sum += 1
            index_offset += 1
        self.jumps_from_cache[index] = sum
        return sum

    def total_combinations(self, index=0):
        if self.combinations_cache[index] > -1:
            return self.combinations_cache[index]
        if index == self.size - 1:
            self.combinations_cache[index] = 1
            return 1
        possible_jumps = self.number_of_jumps_from(index)
        ret = sum([self.total_combinations(index + i + 1) for i in range(possible_jumps) if index + i + 1 < self.size])
        self.combinations_cache[index] = ret
        return ret

def part2():
    joltages = list(get_input())
    joltages.append(0)
    jump_list = JumpList(joltages, 3)
    tot_combs = jump_list.total_combinations()
    return tot_combs

if __name__ == '__main__':
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
