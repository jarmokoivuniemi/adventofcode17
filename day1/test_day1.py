from unittest import TestCase
from nose.tools import assert_equal


def captcha1(num_string):
    num_list = make_num_list(num_string)
    return sum(digits_matching_next_digit(num_list))


def digits_matching_next_digit(num_list):
    return (num_list[i] for i in range(-1, len(num_list)) if num_list[i] == num_list[i-1])


def make_num_list(num_string):
    return [int(num) for num in num_string]


def captcha2(num_string):
    num_list = make_num_list(num_string)
    return sum(num_list[i] for i in range(len(num_list))
               if num_list[i] == num_list[sliced_index(num_list, i)])


def sliced_index(num_list, i):
    return int((len(num_list)/2 + i) % (len(num_list)))


class TestDay1(TestCase):
    def test_part1(self):
        assert_equal(0, captcha1('0'))
        assert_equal(2, captcha1('11'))
        assert_equal(3, captcha1('111'))
        assert_equal(3, captcha1('1122'))
        assert_equal(4, captcha1('1111'))
        assert_equal(9, captcha1('91212129'))
        assert_equal(1, captcha1('0110'))
        assert_equal(4, captcha1('12211'))
        assert_equal(28, captcha1('649713959682898259577777'))

    def test_part1_works(self):
        with open('puzzle.txt') as f:
            assert_equal(1228, captcha1(str(f.read()).strip()))

    def test_part2(self):
        assert_equal(4, captcha2('1111'))
        assert_equal(6, captcha2('1212'))
        assert_equal(0, captcha2('1221'))
        assert_equal(12, captcha2('123123'))
        assert_equal(4, captcha2('12131415'))

    def test_part2_works(self):
        with open('puzzle.txt') as f:
            assert_equal(1238, captcha2(str(f.read()).strip()))
