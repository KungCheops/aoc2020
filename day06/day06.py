import sys
import string

def get_input_1():
    with open(sys.argv[2], 'r') as f:
        accumulator = set()
        for line in f:
            char_set = parse_line(line)
            if len(char_set) != 0:
                accumulator |= parse_line(line)
            else:
                yield accumulator
                accumulator = set()
        yield accumulator

def get_input_2():
    with open(sys.argv[2], 'r') as f:
        accumulator = set(string.ascii_lowercase)
        for line in f:
            char_set = parse_line(line)
            if len(char_set) != 0:
                accumulator &= parse_line(line)
            else:
                yield accumulator
                accumulator = set(string.ascii_lowercase)
        yield accumulator

def parse_line(line):
    return set(line.strip())

def part1():
    return sum(map(len, get_input_1()))

def part2():
    return sum(map(len, get_input_2()))

if __name__ == '__main__':
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
