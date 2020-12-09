import sys

class Preamble():
    def __init__(self, capacity):
        self.capacity = capacity
        self.__pointer = 0
        self.__unsorted_list = [0] * self.capacity
        self.__sorted_list = sorted(self.__unsorted_list)

    def full(self):
        return self.capacity < self.__pointer

    def add(self, item):
        self.__sorted_list[self.__sorted_list.index(self.__unsorted_list[self.__pointer % self.capacity])] = item
        self.__sorted_list = sorted(self.__sorted_list)
        self.__unsorted_list[self.__pointer % self.capacity] = item
        self.__pointer += 1

    def __str__(self):
        return str(self.__sorted_list)

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return min(self.__pointer, self.capacity)

    def contains_sum(self, value):
        min_index = 0
        max_index = self.capacity - 1

        while min_index < max_index:
            if self.__sorted_list[min_index] + self.__sorted_list[max_index] == value:
                return True
            elif self.__sorted_list[min_index] + self.__sorted_list[max_index] < value:
                min_index += 1
            elif self.__sorted_list[min_index] + self.__sorted_list[max_index] > value:
                max_index -= 1

        return False

def get_input():
    with open(sys.argv[2], 'r') as f:
        for line in f:
            yield parse_line(line)
    return

def parse_line(line):
    return int(line)

def part1():
    preamble = Preamble(25)
    for i in get_input():
        if preamble.full():
            if not preamble.contains_sum(i):
                return i
        preamble.add(i)
    if preamble.full():
        if not preamble.contains_sum(i):
            return i
    raise ValueError('No number found.')

def part2():
    bad_number = part1()
    input_list = list(get_input())
    for index, number in enumerate(input_list):
        sum = number
        index_2 = index
        smallest = number
        largest = number
        while sum <= bad_number:
            if sum == bad_number:
                return smallest + largest
            else:
                index_2 += 1
                sum += input_list[index_2]
                if input_list[index_2] < smallest:
                    smallest = input_list[index_2]
                elif input_list[index_2] > largest:
                    largest = input_list[index_2]
    raise ValueError('No contiguous sum found.')

if __name__ == '__main__':
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
