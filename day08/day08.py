import sys

class Op():
    def __init__(self, name, *args):
        self.name = name
        self.args = args

    def __str__(self):
        return f'op:{self.name} {self.args}'

    def __repr__(self):
        return self.__str__()

class Computer():
    def __init__(self, memory):
        self.memory = memory
        self.instruction_counter = 0
        self.accumulator = 0

    def execute_instruction(self):
        current_instruction = self.memory[self.instruction_counter]
        if current_instruction.name == 'acc':
            self.accumulator += current_instruction.args[0]
        elif current_instruction.name == 'jmp':
            self.instruction_counter += current_instruction.args[0] - 1
        elif current_instruction.name == 'nop':
            pass
        else:
            assert False, "Unknown instruction: %s" % current_instruction.name
        self.instruction_counter += 1

    def __str__(self):
        return f'Computer, ic={self.instruction_counter}, acc={self.accumulator}'

    def __repr__(self):
        return self.__str__()

def get_input():
    with open(sys.argv[2], 'r') as f:
        for line in f:
            yield parse_line(line)
    return

def parse_line(line):
    op_name, *operands = line.strip().split(' ')
    operands = map(int, operands)
    return Op(op_name, *operands)

# returns false if it loops and true if it terminates
def run_until_termination(computer):
    instructions_run = set()
    while True:
        if computer.instruction_counter in instructions_run:
            return False
        elif computer.instruction_counter >= len(computer.memory):
            return True
        instructions_run.add(computer.instruction_counter)
        computer.execute_instruction()
    assert False, 'something went wrong'

def part1():
    memory = list(get_input())
    comp = Computer(memory)
    run_until_termination(comp)
    return comp.accumulator

def part2():
    memory = list(get_input())
    for i, operation in enumerate(memory):
        if operation.name == 'jmp':
            operation.name = 'nop'
        elif operation.name == 'nop':
            operation.name = 'jmp'
        else:
            continue
        comp = Computer(memory)
        terminated = run_until_termination(comp)
        if terminated:
            return comp.accumulator
        if operation.name == 'jmp':
            operation.name = 'nop'
        elif operation.name == 'nop':
            operation.name = 'jmp'
    return False

if __name__ == '__main__':
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
