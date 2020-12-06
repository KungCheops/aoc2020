import sys

def get_input():
    with open(sys.argv[2], 'r') as f:
        for line in f:
            yield parse_line(line)
    return

def parse_binary_number(number_string, one_chars):
    mult = 1
    sum = 0
    for c in reversed(number_string):
        if c in one_chars:
            sum += mult
        mult *= 2
    return sum

def parse_line(line):
    return parse_binary_number(line.strip(), ('B', 'R'))

def part1():
    return max(get_input())

def part2():
    sorted_ids = sorted(get_input())
    for i in range(len(sorted_ids)):
        if sorted_ids[i] == sorted_ids[i + 1] - 2:
            return sorted_ids[i] + 1

if __name__ == '__main__':
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
