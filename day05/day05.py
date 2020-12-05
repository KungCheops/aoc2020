import sys

def get_input():
    with open(sys.argv[2], 'r') as f:
        for line in f:
            yield parse_line(line)
    return

def parse_binary_number(number_string, one_char, zero_char):
    mult = 1
    sum = 0
    for c in reversed(number_string):
        if c == one_char:
            sum += mult
        mult *= 2
    return sum

def parse_line(line):
    line = line.strip()
    row_string = line[:7]
    col_string = line[7:]
    row_num = parse_binary_number(row_string, 'B', 'F')
    col_num = parse_binary_number(col_string, 'R', 'L')
    return row_num, col_num

def get_seat_id(row_num, col_num):
    return row_num * 8 + col_num

def part1():
    return max([get_seat_id(row_num, col_num) for row_num, col_num in get_input()])

def part2():
    sorted_ids = sorted([get_seat_id(row_num, col_num) for row_num, col_num in get_input()])
    for i in range(len(sorted_ids)):
        if sorted_ids[i] == sorted_ids[i + 1] - 2:
            return sorted_ids[i] + 1

if __name__ == '__main__':
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
