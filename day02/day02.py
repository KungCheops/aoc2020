import sys

def get_input():
    with open(sys.argv[2], 'r') as f:
        for line in f:
            number, token, value = line.split()
            low, high = map(int, number.split('-'))
            token = token[0]
            yield low, high, token, value
    return

def part1():
    counter = 0
    for low, high, token, value in get_input():
        number_of_tokens = len([c for c in value if c == token])
        if number_of_tokens >= low and number_of_tokens <= high:
            counter += 1
    return counter

def part2():
    counter = 0
    for low, high, token, value in get_input():
        success = (value[low - 1] == token and value[high - 1] != token) or (value[low - 1] != token and value[high - 1] == token)
        if success:
            counter += 1
    return counter

if __name__ == '__main__':
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
