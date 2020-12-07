import sys
import re
from collections import defaultdict

def get_input():
    with open(sys.argv[2], 'r') as f:
        children = defaultdict(list)
        parents = defaultdict(list)
        distances = dict()
        for line in f:
            parent_name, child_distances = parse_line(line)
            for child_name, distance in child_distances.items():
                children[parent_name].append(child_name)
                parents[child_name].append(parent_name)
                distances[(child_name, parent_name)] = distance
                distances[(parent_name, child_name)] = distance
    return children, parents, distances

def parse_line(line):
    first_part, second_part = line.strip().split('contain')
    parent_name = first_part[:-6]

    parser = re.compile('([0-9]+) ([a-z ]*) bag')
    matches = parser.finditer(second_part)
    children = dict()

    for match in matches:
        distance = int(match.group(1))
        child_name = match.group(2)
        children[child_name] = distance

    return parent_name, children

def part1():
    _, parents, _ = get_input()
    all_parents = set()
    unprocessed = set()
    unprocessed.add('shiny gold')
    while len(unprocessed) > 0:
        current_child = unprocessed.pop()
        current_parents = parents[current_child]
        for parent in current_parents:
            if not parent in all_parents:
                all_parents.add(parent)
                unprocessed.add(parent)
    return len(all_parents)

def bags_holding(bag_child, all_bag_parents):
    return 1 + sum([bags_holding(parent_bag, all_bag_parents) for parent_bag in all_bag_parents])

def part2():
    all_bag_children, _, distances = get_input()
    total_bags = bags_inside('shiny gold', all_bag_children, distances)
    return total_bags - 1

def bags_inside(bag_parent, all_bag_children, bag_numbers):
    return 1 + sum([bag_numbers[(bag_parent, child_bag)] * bags_inside(child_bag, all_bag_children, bag_numbers) for child_bag in all_bag_children[bag_parent]])

if __name__ == '__main__':
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
