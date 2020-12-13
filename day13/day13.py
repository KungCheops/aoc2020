import sys
import itertools
import numpy as np

def get_input():
    with open(sys.argv[2], 'r') as f:
        for line in f:
            yield parse_line(line)
    return

def parse_line(line):
    return line

def part1():
    line1, line2 = get_input()
    earliest_departure = int(line1.strip())
    bus_ids = list(map(int, (bus_time for bus_time in line2.strip().split(',') if bus_time.isnumeric())))

    shortest_wait_time = float('inf')
    earliest_bus_id = -1
    for bus_id in bus_ids:
        wait_time = bus_id - (earliest_departure % bus_id)
        # print(bus_id, wait_time)
        if wait_time < shortest_wait_time:
            shortest_wait_time = wait_time
            earliest_bus_id = bus_id
    return shortest_wait_time * earliest_bus_id

def possible_wait_times(bus_id, offset):
    i = 0
    while True:
        ret = i * bus_id - offset
        while ret < offset:
            i += 1
            ret = i * bus_id - offset
        yield ret
        i += 1

def part2():
    _, line2 = get_input()
    bus_ids = list()
    offsets = list()
    for i, bus_id in enumerate(line2.strip().split(',')):
        if bus_id.isnumeric():
            bus_ids.append(int(bus_id))
            offsets.append(i)

    multiple = bus_ids[0]
    counter = 0
    for i in range(1, len(bus_ids)):
        while True:
            if (counter + offsets[i]) % bus_ids[i] == 0:
                break
            counter += multiple
        multiple *= bus_ids[i]
    return counter

if __name__ == '__main__':
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
