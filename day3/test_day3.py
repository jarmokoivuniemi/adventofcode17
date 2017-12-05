from unittest import TestCase
from nose.tools import assert_equal
from spiral_memory import SpiralMemory

class TestDay3(TestCase):

    def setUp(self):
        self.memory = SpiralMemory(25)

    def test_big_spiral(self):
        memory = SpiralMemory(pow(199, 2))
        assert_equal(31, memory.calcualte_distance(1024))

    def test_part1_works(self):
        memory = SpiralMemory(pow(700, 2))
        assert_equal(430, memory.calcualte_distance(312051))

    def test_part2_works(self):
        memory = SpiralMemory(pow(199, 2), hack=True, puzzle=312051)
        assert_equal(312453, memory.puzzle)
        
