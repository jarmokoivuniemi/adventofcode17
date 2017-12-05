from unittest import TestCase
from nose.tools import assert_equal

def steps_to_exit(offsets, next_position):
    current_pos, steps = 0, 0
    offset_map = {i: number for i, number in enumerate(offsets)}
    while current_pos < len(offsets):
        current_pos += next_position(current_pos, offset_map)
        steps +=1
    return steps


def part1(current_pos, offset_map):
    pos = offset_map[current_pos]
    offset_map[current_pos] += 1
    return pos


def part2(current_pos, offset_map):
    pos = offset_map[current_pos]
    offset_map[current_pos] += -1 if pos >=3 else 1
    return pos

class TestDay5(TestCase):

    def test_part1_example(self):
        offsets = [0, 3, 0, 1, -3]
        assert_equal(5, steps_to_exit(offsets, part1))
    
    def test_part1_works(self):
        with open('puzzle.txt') as f:
            offsets = [int(n.strip()) for n in f.readlines()]
            assert_equal(373543, steps_to_exit(offsets, part1))

    def test_part2_example(self):
        offsets = [0, 3, 0, 1, -3]
        assert_equal(10, steps_to_exit(offsets, part2))
        
    def test_part2_works(self):
        with open('puzzle.txt') as f:
            offsets = [int(n.strip()) for n in f.readlines()]
            assert_equal(27502966, steps_to_exit(offsets, part2))
