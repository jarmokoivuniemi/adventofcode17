from unittest import TestCase
from nose.tools import assert_equal

example = [
        [17, 16, 15, 14, 13],
        [18,  5,  4,  3, 12],
        [19,  6,  1,  2, 11],
        [20,  7,  8,  9, 10],
        [21, 22, 23, 24, 25]
        ]

def spiral(max_value):
    result = []
    size = int(pow(max_value, 0.5))
    for i in range(size):
        inner = []
        for j in range(size):
            inner.append(None)
        result.append(inner)

    middle = (size-1)/2
    num = int(max_value / 2 + 1)
    for i in range(size):
        for j in range(size):
            if i==middle and j==middle:
                result[i][j] = num
                num += 1

            elif i==middle and j==middle+1:
                result[i][j] = num
                num += 5

            elif i==middle-1 and j==middle+1:
                result[i][j] = num
                num += 3

            elif i==middle-1 and j==middle:
                result[i][j] = num
                num -= 1

            elif i == middle-1 and j == middle-1:
                result[i][j] = num
                num -= 1

            elif i==middle and j == middle-1:
                result[i][j] = num
                num -= 5

            elif i==middle+1 and j == middle-1:
                result[i][j] = num
                num += 1

            elif i==middle+1 and j == middle:
                result[i][j] = num
                num += 1

            elif i==middle+1 and j == middle+1:
                result[i][j] = num

    return result

class TestDay3(TestCase):

    def test_grid_size_nine(self):
        expected = [
                [5, 4, 3],
                [6, 1, 2],
                [7, 8, 9]
                ]
        assert_equal(2, expected[1][2])
        assert_equal(3, expected[0][2])
        assert_equal(4, expected[0][1])
        assert_equal(5, expected[0][0])
        assert_equal(6, expected[1][0])
        assert_equal(7, expected[2][0])
        assert_equal(8, expected[2][1])
        assert_equal(9, expected[2][2])
        #assert_equal(expected, spiral(9))
        
    def test_individual_elemets_in_spiral(self):
        assert_equal(1, spiral(9)[1][1])
        assert_equal(2, spiral(9)[1][2])
        assert_equal(3, spiral(9)[0][2])
        assert_equal(4, spiral(9)[0][1])
        assert_equal(5, spiral(9)[0][0])
        assert_equal(6, spiral(9)[1][0])
        assert_equal(7, spiral(9)[2][0])
        assert_equal(8, spiral(9)[2][1])
        assert_equal(9, spiral(9)[2][2])

    def test_25(self):
        print(spiral(25))
        assert 0
        
