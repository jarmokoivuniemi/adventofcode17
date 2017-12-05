from unittest import TestCase
from nose.tools import assert_equal

def steps_to_exit(steps):
    exit = len(steps)
    current_pos = 0
    step_map = {i: number for i, number in enumerate(steps)}
    num_steps = 0
    while current_pos < exit:
        current_pos += next_position(current_pos, step_map)
        num_steps +=1
    return num_steps

def next_position(current_pos, steps):
    pos = steps[current_pos]
    steps[current_pos] += 1
    return pos

class TestDay5(TestCase):

    def test_part1_example(self):
        steps = [0, 3, 0, 1, -3]
        assert_equal(5, steps_to_exit(steps))
    
    def test_part1_works(self):
        with open('puzzle.txt') as f:
            steps = [int(n.strip()) for n in f.readlines()]
            assert_equal(373543, steps_to_exit(steps))
        
