import sys
from collections import defaultdict, deque

def get_input():
    with open(sys.argv[2], 'r') as f:
        for line in f:
            yield parse_line(line)
    return

def parse_line(line):
    return line.strip().split(',')

def find_number(initial_list, number):
    last_spoken_at = defaultdict(deque)
    for iter, initial_number in enumerate(initial_list):
        last_spoken_at[initial_number].append(iter)
        # print(iter + 1, initial_number)
    last_spoken_number = initial_list[-1]
    for iter in range(len(initial_list), number):
        if len(last_spoken_at[last_spoken_number]) == 1:
            next_number = 0
        else:
            next_number = last_spoken_at[last_spoken_number][1] - last_spoken_at[last_spoken_number].popleft()
        last_spoken_at[next_number].append(iter)
        last_spoken_number = next_number
        # print(iter + 1, next_number)
    return last_spoken_number

def nth_number_spoken(n):
    answers = list(find_number(list(map(int, numbers)), n) for numbers in get_input())
    if len(answers) == 1:
        return answers[0]
    return answers

def part1():
    return nth_number_spoken(2020)

def part2():
    return nth_number_spoken(30000000)

if __name__ == '__main__':
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
