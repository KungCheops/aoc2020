import sys
from collections import deque

class Statement():
    def __init__(self, type, args):
        self.type = type
        self.args = args

def get_input():
    with open(sys.argv[2], 'r') as f:
        for line in f:
            yield parse_line(line)
    return

def parse_line(line):
    return line.strip().replace(' ', '')

'''
while there are tokens to be read:
    read a token.
    if the token is a number, then:
        push it to the output queue.
    else if the token is a function then:
        push it onto the operator stack
    else if the token is an operator then:
        while ((there is an operator at the top of the operator stack)
              and ((the operator at the top of the operator stack has greater precedence)
                  or (the operator at the top of the operator stack has equal precedence and the token is left associative))
              and (the operator at the top of the operator stack is not a left parenthesis)):
            pop operators from the operator stack onto the output queue.
        push it onto the operator stack.
    else if the token is a left parenthesis (i.e. "("), then:
        push it onto the operator stack.
    else if the token is a right parenthesis (i.e. ")"), then:
        while the operator at the top of the operator stack is not a left parenthesis:
            pop the operator from the operator stack onto the output queue.
        /* If the stack runs out without finding a left parenthesis, then there are mismatched parentheses. */
        if there is a left parenthesis at the top of the operator stack, then:
            pop the operator from the operator stack and discard it
        if there is a function token at the top of the operator stack, then:
            pop the function from the operator stack onto the output queue.
/* After while loop, if operator stack not null, pop everything to output queue */
if there are no more tokens to read then:
    while there are still operator tokens on the stack:
        /* If the operator token on the top of the stack is a parenthesis, then there are mismatched parentheses. */
        pop the operator from the operator stack onto the output queue.
exit.
'''

debug = False

def to_postfix(input_string):
    output_queue = deque()
    operator_stack = deque()
    # while there are tokens to be read read a token:
    for char in input_string:
        # if the token is a number, then:
        if char.isnumeric():
            # push it to the output queue.
            output_queue.append(char)
        # else if the token is an operator then:
        elif char in ('+', '*'):
            # while there is an operator at the top of the operator stack
            # and the operator at the top of the operator stack is not a left parenthesis
            while len(operator_stack) > 0 and operator_stack[len(operator_stack) - 1] != '(':
                # pop operators from the operator stack onto the output queue.
                output_queue.append(operator_stack.pop())
            # push it onto the operator stack.
            operator_stack.append(char)
        # else if the token is a left parenthesis (i.e. "("), then:
        elif char == '(':
            # push it onto the operator stack.
            operator_stack.append(char)
        # else if the token is a right parenthesis (i.e. ")"), then:
        elif char == ')':
            # while the operator at the top of the operator stack is not a left parenthesis:
            while len(operator_stack) > 0 and operator_stack[len(operator_stack) - 1] != '(':
                # pop the operator from the operator stack onto the output queue.
                output_queue.append(operator_stack.pop())
                # if there is a left parenthesis at the top of the operator stack, then:
                if len(operator_stack) > 0 and operator_stack[len(operator_stack) - 1] == '(':
                    # pop the operator from the operator stack and discard it
                    operator_stack.pop()
                    break
    # /* After while loop, if operator stack not null, pop everything to output queue */
    while len(operator_stack) > 0:
        output_queue.append(operator_stack.pop())
    # while there are still operator tokens on the stack:
    while len(operator_stack) > 0:
        # pop the operator from the operator stack onto the output queue.
        output_queue.append(operator_stack.pop())
    return ''.join(output_queue)

def to_postfix_2(input_string):
    output_queue = deque()
    operator_stack = deque()
    # while there are tokens to be read read a token:
    for char in input_string:
        # if the token is a number, then:
        if char.isnumeric():
            # push it to the output queue.
            output_queue.append(char)
        # else if the token is an operator then:
        elif char in ('+', '*'):
            # while there is an operator at the top of the operator stack
            # and the operator at the top of the operator stack is not a left parenthesis
            while len(operator_stack) > 0 and operator_stack[len(operator_stack) - 1] != '(' \
                # and ((the operator at the top of the operator stack has greater precedence)
                # or (the operator at the top of the operator stack has equal precedence and the token is left associative))
                and not (operator_stack[len(operator_stack) - 1] == '*' and char == '+'):
                # pop operators from the operator stack onto the output queue.
                output_queue.append(operator_stack.pop())
            # push it onto the operator stack.
            operator_stack.append(char)
        # else if the token is a left parenthesis (i.e. "("), then:
        elif char == '(':
            # push it onto the operator stack.
            operator_stack.append(char)
        # else if the token is a right parenthesis (i.e. ")"), then:
        elif char == ')':
            # while the operator at the top of the operator stack is not a left parenthesis:
            while len(operator_stack) > 0 and operator_stack[len(operator_stack) - 1] != '(':
                # pop the operator from the operator stack onto the output queue.
                output_queue.append(operator_stack.pop())
                # if there is a left parenthesis at the top of the operator stack, then:
                if len(operator_stack) > 0 and operator_stack[len(operator_stack) - 1] == '(':
                    # pop the operator from the operator stack and discard it
                    operator_stack.pop()
                    break
    # /* After while loop, if operator stack not null, pop everything to output queue */
    while len(operator_stack) > 0:
        output_queue.append(operator_stack.pop())
    # while there are still operator tokens on the stack:
    while len(operator_stack) > 0:
        # pop the operator from the operator stack onto the output queue.
        output_queue.append(operator_stack.pop())
    return ''.join(output_queue)

def eval_postfix(postfix):
    stack = deque()
    for element in postfix:
        if element.isnumeric():
            stack.append(int(element))
        else:
            e1 = stack.pop()
            e2 = stack.pop()
            if element == '+':
                stack.append(e1 + e2)
            elif element == '*':
                stack.append(e1 * e2)
    return stack[0]

def part1():
    return sum(eval_postfix(to_postfix(line)) for line in get_input())

def part2():
    return sum(eval_postfix(to_postfix_2(line)) for line in get_input())

if __name__ == '__main__':
    if sys.argv[1] == '1':
        print(part1())
    elif sys.argv[1] == '2':
        print(part2())
