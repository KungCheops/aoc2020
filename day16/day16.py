import sys

class Ticket():
    def __init__(self, fields):
        self.fields = list(fields)

    def __str__(self):
        return str(self.fields)

    def __repr__(self):
        return str(self.fields)

class TicketField():
    def __init__(self, tf_string):
        name, ranges = tf_string.split(':')
        self.name = name
        ranges = ranges.split(' or ')
        ranges = map(lambda x: map(int, x.split('-')), ranges)
        ranges = [range(a, b + 1) for a, b in ranges]
        self.ranges = ranges

    def is_in_range(self, value):
        return any((value in range_ for range_ in self.ranges))

    def __str__(self):
        return f'{self.name}: {self.ranges}'

    def __repr__(self):
        return self.__str__()

def parse_file():
    ticket_fields = list()
    my_ticket = None
    nearby_tickets = []
    input_part = 0
    for line in get_input():
        if input_part == 0:
            if line == '':
                input_part = 1
            else:
                ticket_fields.append(TicketField(line))
        elif input_part == 1:
            if line == '':
                input_part = 2
            elif line[0].isnumeric():
                my_ticket = Ticket(map(int, line.split(',')))
        elif input_part == 2:
            if line[0].isnumeric():
                nearby_tickets.append(Ticket(map(int, line.split(','))))
    return my_ticket, nearby_tickets, ticket_fields

def get_input():
    with open(sys.argv[2], 'r') as f:
        for line in f:
            yield parse_line(line)
    return

def parse_line(line):
    return line.strip()

def part1():
    my_ticket, nearby_tickets, ticket_fields = parse_file()
    invalid_values = list()

    for ticket in nearby_tickets:
        for value in ticket.fields:
            is_valid = False
            for ticket_field in ticket_fields:
                if ticket_field.is_in_range(value):
                    is_valid = True
                    break
            if not is_valid:
                invalid_values.append(value)
    return sum(invalid_values)

def part2():
    pass

if __name__ == '__main__':
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
