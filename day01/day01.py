import sys

def get_input():
    with open(sys.argv[2], 'r') as f:
        for line in f:
            yield int(line)
    return

def part1():
    prev = set()
    for val in get_input():
        if 2020 - val in prev:
            return val * (2020 - val)
        else:
            prev.add(val)

def part2():
    input_list = list(get_input())
    input_set = set(get_input())
    for i in range(len(input_list) - 2):
        for j in range (i + 1, len(input_list) - 1):
                if 2020 - (input_list[i] + input_list[j]) in input_set:
                    return input_list[i] * input_list[j] * (2020 - (input_list[i] + input_list[j]))

if __name__ == '__main__':
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
