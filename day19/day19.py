import sys
import re

def get_input():
    with open(sys.argv[2], 'r') as f:
        for line in f:
            yield parse_line(line)
    return

def parse_line(line, ):
    return line.replace('"', '').strip()

def match(string, rules, rule='0'):
    # print(f'matching string={string}, rule={rule}')
    if len(string) == 0:
        return True
    if isinstance(rule, str):
        if rule.isalpha():
            return (string[0] == rule, string[1:])
        elif rule.isnumeric():
            return match(string, rules, rules[rule])
    elif isinstance(rule, tuple):
        left_rule, right_rule = rule
        left_match, rest = match(string, rules, left_rule)
        if left_match:
            return left_match, rest
        right_match, rest = match(string, rules, right_rule)
        if right_match:
            return right_match, rest
        return False, string
    elif isinstance(rule, list):
        for rule_elem in rule:
            match_, string = match(string, rules, rule_elem)
            if not match_:
                return (False, string)
        return (True, string)

def part1():
    state = 0
    rules = dict()
    count = 0
    for line in get_input():
        if state == 0:
            if line == '':
                state = 1
                continue
            else:
                rule_number, rule = line.split(': ')
                rule_number = rule_number
                if '|' in rule:
                    left_rule, right_rule = rule.split(' | ')
                    rules[rule_number] = (left_rule.split(' '), right_rule.split(' '))
                elif rule.isalpha():
                    rules[rule_number] = rule
                else:
                    rules[rule_number] = rule.split(' ')
        if state == 1:
            match_, rest = match(line, rules)
            if match_ and len(rest) == 0:
                count += 1
    return count

def part2():
    pass

if __name__ == '__main__':
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
