from unittest import TestCase
from nose.tools import assert_equal
from spiral_memory import SpiralMemory

class TestDay3(TestCase):

    def setUp(self):
        self.memory = SpiralMemory(9)

    def test_size_49(self):
        memory = SpiralMemory(49)
        assert_equal(1, memory.memory[3][3])
        assert_equal(2, memory.memory[3][4])
        assert_equal(3, memory.memory[2][4])
        assert_equal(4, memory.memory[2][3])
        assert_equal(5, memory.memory[2][2])
        assert_equal(6, memory.memory[3][2])
        assert_equal(7, memory.memory[4][2])
        assert_equal(8, memory.memory[4][3])
        assert_equal(9, memory.memory[4][4])
        assert_equal(10, memory.memory[4][5])
        assert_equal(11, memory.memory[3][5])
        assert_equal(12, memory.memory[2][5])
        assert_equal(13, memory.memory[1][5])
        assert_equal(14, memory.memory[1][4])
        assert_equal(15, memory.memory[1][3])
        assert_equal(16, memory.memory[1][2])
        assert_equal(17, memory.memory[1][1])
        assert_equal(18, memory.memory[2][1])
        assert_equal(19, memory.memory[3][1])
        assert_equal(20, memory.memory[4][1])
        assert_equal(21, memory.memory[5][1])
        assert_equal(22, memory.memory[5][2])

    def test_spiral_of_size25(self):
        memory = SpiralMemory(25)
        expected = [
                [17, 16, 15, 14, 13],
                [18,  5,  4,  3, 12],
                [19,  6,  1,  2, 11],
                [20,  7,  8,  9, 10],
                [21, 22, 23, 24, 25]
                ]
        #assert_equal(expected, memory.memory)
        assert_equal(1, memory.memory[2][2])
        assert_equal(2, memory.memory[2][3])
        assert_equal(3, memory.memory[1][3])
        assert_equal(4, memory.memory[1][2])
        assert_equal(5, memory.memory[1][1])
        assert_equal(6, memory.memory[2][1])
        assert_equal(7, memory.memory[3][1])
        assert_equal(8, memory.memory[3][2])
        assert_equal(9, memory.memory[3][3])
        assert_equal(10, memory.memory[3][4])
        assert_equal(11, memory.memory[2][4])
        assert_equal(12, memory.memory[1][4])
        assert_equal(13, memory.memory[0][4])
        assert_equal(14, memory.memory[0][3])
        assert_equal(15, memory.memory[0][2])
        assert_equal(16, memory.memory[0][1])
        assert_equal(17, memory.memory[0][0])
        assert_equal(18, memory.memory[1][0])
        assert_equal(19, memory.memory[2][0])
        assert_equal(20, memory.memory[3][0])
        assert_equal(21, memory.memory[4][0])
        assert_equal(22, memory.memory[4][1])
        #assert_equal(23, memory.memory[4][2])
        #assert_equal(24, memory.memory[4][3])
        #assert_equal(25, memory.memory[4][4])


    def test_size_nine(self):
        memory = SpiralMemory(9)
        e = [
            [5, 4, 3],
            [6, 1, 2],
            [7, 8, 9]
            ]
        assert_equal(1, memory.memory[1][1])
        assert_equal(2, memory.memory[1][2])
        assert_equal(3, memory.memory[0][2])
        assert_equal(4, memory.memory[0][1])
        assert_equal(5, memory.memory[0][0])
        assert_equal(6, memory.memory[1][0])
        assert_equal(7, memory.memory[2][0])
        assert_equal(8, memory.memory[2][1])
        assert_equal(9, memory.memory[2][2])

    def est_find_data_square(self):
        assert_equal((2, 2), self.memory.find_location(1))
        assert_equal((2, 3), self.memory.find_location(2))

    def est_calculate_distance(self):
        assert_equal(0, self.memory.calcualte_distance(1))
        assert_equal(3, self.memory.calcualte_distance(12))
        assert_equal(2, self.memory.calcualte_distance(23))

    def est_big_spiral(self):
        memory = SpiralMemory(pow(199, 2))
        assert_equal(31, memory.calcualte_distance(1024))

    def est_part1_works(self):
        memory = SpiralMemory(pow(587, 2))
        assert_equal(430, memory.calcualte_distance(312051))

