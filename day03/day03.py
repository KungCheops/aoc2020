import sys

def get_input(x_step, y_step):
    with open(sys.argv[2], 'r') as f:
        for i, line in enumerate(f):
            if i % y_step == 0:
                yield parse_line(line, i // y_step, x_step)
    return

def parse_line(line, line_no, step_length):
    char = line[(line_no * step_length) % (len(line) - 1)]
    if char == '#':
        return 1
    if char == '.':
        return 0

def count_crashes(x_step, y_step):
    counter = 0
    for num in get_input(x_step, y_step):
        counter += num
    return counter

def part1():
    return count_crashes(3, 1)

def part2():
    perms = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    multiple = 1
    for x_step, y_step in perms:
        multiple *= count_crashes(x_step, y_step)
    return multiple

if __name__ == '__main__':
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
