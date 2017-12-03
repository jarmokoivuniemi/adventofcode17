from unittest import TestCase
from nose.tools import assert_equal
from spiral_memory import SpiralMemory

class TestDay3(TestCase):

    def setUp(self):
        self.memory = SpiralMemory(25)

    def test_spiral_of_size25(self):
        expected = [
                [17, 16, 15, 14, 13],
                [18,  5,  4,  3, 12],
                [19,  6,  1,  2, 11],
                [20,  7,  8,  9, 10],
                [21, 22, 23, 24, 25]
                ]

        assert_equal(expected, self.memory.memory)

    def test_find_data_square(self):
        assert_equal((2, 2), self.memory.find_location(1))
        assert_equal((2, 3), self.memory.find_location(2))

    def test_calculate_distance(self):
        assert_equal(0, self.memory.calcualte_distance(1))
        assert_equal(3, self.memory.calcualte_distance(12))
        assert_equal(2, self.memory.calcualte_distance(23))

    def test_big_spiral(self):
        memory = SpiralMemory(pow(199, 2))
        assert_equal(31, memory.calcualte_distance(1024))

    def test_part1_works(self):
        memory = SpiralMemory(pow(587, 2))
        assert_equal(430, memory.calcualte_distance(312051))
