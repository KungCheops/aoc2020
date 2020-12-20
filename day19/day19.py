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
    print(f'matching string={string}, rule={rule}')
    if isinstance(rule, str):
        if rule.isalpha():
            return (string[0] == rule, string[1:], rule)
        elif rule.isnumeric():
            match_, rest, rule2 = match(string, rules, rules[rule])
            return match_, rest, (rule, rule2)
    elif isinstance(rule, tuple):
        left_rule, right_rule = rule
        left_match, rest, new_rule = match(string, rules, left_rule)
        print(left_match, rest, new_rule)
        if left_match:
            return left_match, rest, new_rule
        else:
            print('trying options 2')
            right_match, rest, new_rule = match(string, rules, right_rule)
            if right_match:
                return right_match, rest, new_rule
        return False, string, rule
    elif isinstance(rule, list):
        rules_used = []
        for rule_elem in rule:
            #if len(string) == 0:
            #    return (False, string)
            match_, string, rule2 = match(string, rules, rule_elem)
            rules_used.append(rule2)
            if not match_:
                return (False, string, rules_used)
        return (len(string) == 0, string, rules_used)

def count_matches(input):
    state = 0
    rules = dict()
    count = 0
    for line in input:
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
            print(line)
            match_, rest, rule = match(line, rules)
            if match_ and len(rest) == 0:
                print(line, rule)
                count += 1
    return count

def part1():
    return count_matches(get_input())

def part2():
    input = list(get_input())
    for i, line in enumerate(input):
        if line.startswith('8:'):
            input[i] = '8: 42 | 42 8'
        elif line.startswith('11:'):
            input[i] = '11: 42 31 | 42 11 31'
    return count_matches(input)

if __name__ == '__main__':
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
