import sys

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

def part2():
    pass

if __name__ == '__main__':
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
