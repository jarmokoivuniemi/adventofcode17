from unittest import TestCase
from nose.tools import assert_equal
comparations = {
        '<': lambda x, y: x < y, 
        '>': lambda x, y: x > y,
        '>=': lambda x, y: x >= y,
        '<=': lambda x, y: x <= y,
        '==': lambda x, y: x == y,
        '!=': lambda x, y: x != y
        }

operations = {
        'inc': 1,
        'dec': -1,
        }

def init_values(instructions):
    return {s.split()[0]: 0 for s in instructions}

def execute_instructions(instructions):
    values = init_values(instructions)
    max_val = 0
    for instruction in instructions:
        value = instruction.split()[0]
        values[value] += calculate(instruction, values)
        if values[value] > max_val:
            max_val = values[value]
    return values, max_val

def calculate(instruction, values):
    _, operation, amount, _, compare_val, compare_opeartion, condition_val = instruction.split()
    if comparations[compare_opeartion](values[compare_val], int(condition_val)):
        return int(amount) * operations[operation]
    return 0

class TestDay8(TestCase):

    def test_init_input(self):
        instructions = ['b inc 5 if a > 1', 'a inc 1 if b < 5']
        assert_equal({'a': 0, 'b': 0}, init_values(instructions))

    def test_calculate_instruction(self):
        instructions = ['b inc 5 if a > 1', 'a inc 1 if b < 5']
        values = init_values(instructions)
        assert_equal(1, calculate('a inc 1 if b < 5', values))

    def test_given_instructions_that_change_value_when_execute_instructions(self):
        instructions = ['b inc 5 if a > 1', 'a inc 1 if b < 5']
        values = init_values(instructions)
        assert_equal({'a': 1, 'b': 0}, execute_instructions(instructions, values))

    def test_given_instructions_that_change_value_when_execute_instructions(self):
        instructions = ['b inc 5 if a > 1', 'a inc 1 if b < 5']
        assert_equal({'a': 1, 'b': 0}, execute_instructions(instructions)[0])

    def test_part1_examples(self):
        instructions = [
        'b inc 5 if a > 1',
        'a inc 1 if b < 5',
        'c dec -10 if a >= 1',
        'c inc -20 if c == 10',
        ]
        values, max_val = execute_instructions(instructions)
        assert_equal(1, values[max(values, key=values.get)])

    def test_it_works(self):
        with open('puzzle.txt') as f:
            instructions = [s.strip() for s in f.readlines()]
            values, max_val = execute_instructions(instructions)
            assert_equal(4066, values[max(values, key=values.get)])
            assert_equal(4829, max_val)

