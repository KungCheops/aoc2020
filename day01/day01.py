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
    sorted_input = sorted(get_input())
    for i in range(len(sorted_input)):
        for j in range (i + 1, len(sorted_input)):
            for k in range (j + 1, len(sorted_input)):
                if sorted_input[i] + sorted_input[j] + sorted_input[k] == 2020:
                    return sorted_input[i] * sorted_input[j] * sorted_input[k]

if __name__ == '__main__':
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
