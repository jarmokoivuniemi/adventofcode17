from unittest import TestCase
from nose.tools import assert_equal
from itertools import combinations


def difference_checksum(spreadsheet):
    return sum(difference(make_num_list(numbers)) for numbers in spreadsheet)


def difference(num_list):
    return max(num_list) - min(num_list)


def make_num_list(num_string):
    return [int(n) for n in num_string.split()]


class TestDay2Part1(TestCase):

    def test_difference(self):
        assert_equal(8, difference(make_num_list('5 1 9 5')))

    def test_it_wors(self):
        with open('puzzle.txt') as f:
            puzzle = [n.strip() for n in f.readlines() if n.strip()]
            assert_equal(53460, difference_checksum(puzzle))


def division_checksum(spreadsheet):
    return sum(divide_evenly_divisible(make_num_list(numbers)) for numbers in spreadsheet)


def divide_evenly_divisible(num_list):
    return next(divide(a, b) for a, b in combinations(num_list, 2) if are_divisible(a, b))


def are_divisible(a, b):
    return max(a, b) % min(a, b) == 0


def divide(a, b):
    return int(max(a, b) / min(a, b))


class TestDay2Part2(TestCase):

    def test_even_division(self):
        assert_equal(4, divide_evenly_divisible(make_num_list('5 9 2 8')))
        assert_equal(3, divide_evenly_divisible(make_num_list('9 4 7 3')))
        assert_equal(2, divide_evenly_divisible(make_num_list('3 8 6 5')))

    def test_it_wors(self):
        with open('puzzle.txt') as f:
            puzzle = [n.strip() for n in f.readlines() if n.strip()]
            assert_equal(282, division_checksum(puzzle))
