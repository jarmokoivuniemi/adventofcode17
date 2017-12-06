from unittest import TestCase
from nose.tools import assert_equal

def detect_infinite_loop(blocks, times=2):
    found_configs = []
    cycles = 0
    while found_configs.count(blocks) < times:
        blocks = balance(list(blocks))
        found_configs.append(blocks)
        cycles += 1

    return cycles


def balance(blocks):
    block_size = len(blocks)
    largest_bank = blocks.index(max(blocks)) 
    slots_to_distribute = blocks[largest_bank]
    blocks[largest_bank] = 0
    for i in range(1, slots_to_distribute+1):
        blocks[(block_size + largest_bank + i) % block_size] += 1

    return blocks

class TestDay6(TestCase):

    def test_part1_examples(self):
        assert_equal([2, 4, 1, 2], balance([0, 2, 7, 0]))
        assert_equal([3, 1, 2, 3], balance([2, 4, 1, 2]))

        assert_equal(5, detect_infinite_loop([0, 2, 7, 0]))

    def test_part1_works(self):
        with open('puzzle.txt') as f:
            blocks = [int(s.strip()) for s in f.read().split()]
            assert_equal(14029, detect_infinite_loop(blocks))

    def test_part2_examples(self):
        assert_equal(5+4, detect_infinite_loop([0, 2, 7, 0], times=3))

    def test_part2_works(self):
        with open('puzzle.txt') as f:
            blocks = [int(s.strip()) for s in f.read().split()]
            assert_equal(14029 + 2765, detect_infinite_loop(blocks, times=3))
