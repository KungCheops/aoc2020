import sys

def get_input1():
    with open(sys.argv[2], 'r') as f:
        for i, line in enumerate(f):
            yield parse_line1(line, i)
    return

def parse_line1(line, line_no):
    char = line[(line_no * 3) % (len(line) - 1)]
    if char == '#':
        return 1
    if char == '.':
        return 0

def part1():
    counter = 0
    for num in get_input1():
        counter += num
    return counter

def part2():
    pass

if __name__ == '__main__':
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
