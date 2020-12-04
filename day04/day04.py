import sys

debug = False

def get_input():
    with open(sys.argv[2], 'r') as f:
        entries = dict()
        for line in f:
            parsed_line = list(parse_line(line))
            if parsed_line != []:
                for key, value in parsed_line:
                    entries[key] = value
            else:
                yield entries
                entries = dict()
        yield entries

def parse_line(line):
    for token in line.split():
        yield token.split(':')

def part1():
    counter = 0
    for entry in get_input():
        if not 'byr' in entry:
            continue
        if not 'iyr' in entry:
            continue
        if not 'eyr' in entry:
            continue
        if not 'hgt' in entry:
            continue
        if not 'hcl' in entry:
            continue
        if not 'ecl' in entry:
            continue
        if not 'pid' in entry:
            continue
        counter += 1
    return counter

eye_colors = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])

def part2():
    counter = 0
    for entry in get_input():
        if not 'byr' in entry:
            if debug:
                print('no birth year')
            continue
        else:
            birth_year = entry['byr']
            if not birth_year.isnumeric():
                if debug:
                    print(f'invalid birth year: {birth_year}')
                continue
            number = int(birth_year)
            if number < 1920 or number > 2002:
                if debug:
                    print(f'invalid birth year: {birth_year}')
                continue
        if not 'iyr' in entry:
            if debug:
                print('no issue year')
            continue
        else:
            issue_year= entry['iyr']
            if not issue_year.isnumeric():
                if debug:
                    print(f'invalid issue year: {issue_year}')
                continue
            number = int(issue_year)
            if number < 2010 or number > 2020:
                if debug:
                    print(f'invalid issue year: {issue_year}')
                continue
        if not 'eyr' in entry:
            if debug:
                print('no expiration year')
            continue
        else:
            expiration_year = entry['eyr']
            if not expiration_year.isnumeric():
                if debug:
                    print(f'invalid expiration year: {birth_year}')
                continue
            number = int(expiration_year)
            if number < 2020 or number > 2030:
                if debug:
                    print(f'invalid expiration year: {birth_year}')
                continue
        if not 'hgt' in entry:
            if debug:
                print('no height')
            continue
        else:
            height = entry['hgt']
            if not height[:-2].isnumeric():
                if debug:
                    print(f'invalid height: {height}')
                continue
            height_value = int(height[:-2]) # ignore last two characters
            if height.endswith('cm'):
                if height_value < 150 or height_value > 193:
                    if debug:
                        print(f'invalid height: {height}')
                    continue
            elif height.endswith('in'):
                if height_value < 59 or height_value > 76:
                    if debug:
                        print(f'invalid height: {height}')
                    continue
            else:
                if debug:
                    print(f'invalid height: {height}')
                continue
        if not 'hcl' in entry:
            if debug:
                print('no hair color')
            continue
        else:
            hair_color = entry['hcl']
            if hair_color[0] != '#':
                if debug:
                    print(f'invalid hair color: {hair_color}')
                continue
            if not hair_color[1:].isalnum():
                if debug:
                    print(f'invalid hair color: {hair_color}')
                continue
        if not 'ecl' in entry:
            if debug:
                print('no eye color')
            continue
        else:
            eye_color = entry['ecl']
            if not eye_color in eye_colors:
                if debug:
                    print(f'invalid eye color: {eye_color}')
                continue
        if not 'pid' in entry:
            if debug:
                print('no passport id')
            continue
        else:
            passport_id = entry['pid']
            if not len(passport_id) == 9:
                if debug:
                    print(f'invalid passport id: {passport_id}')
                continue
            if not passport_id.isnumeric():
                if debug:
                    print(f'invalid passport id: {passport_id}')
                continue
        counter += 1
    return counter

if __name__ == '__main__':
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
