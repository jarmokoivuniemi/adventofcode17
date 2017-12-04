from unittest import TestCase
from nose.tools import assert_equal, assert_true, assert_false
from itertools import combinations

def is_valid_passphrase(passphrase):
    words = passphrase.split()
    uniq_words = set(words)
    return len(words) == len(uniq_words)

def is_very_valid_passphrase(passphrase):
    words = passphrase.split()
    return all(sorted(a) != sorted(b) for a, b in combinations(words, 2))


class TestDay4(TestCase):
    def test_part1_examples(self):
        assert_true(is_valid_passphrase('aa bb cc dd ee'))
        assert_false(is_valid_passphrase('aa bb cc dd aa'))
        assert_true(is_valid_passphrase('aa bb cc dd aaa'))

    def test_part1_works(self):
        with open('puzzle.txt') as f:
            assert_equal(386, sum(1 for passphrase in f.readlines() if is_valid_passphrase(passphrase)))

    def test_part2_examples(self):
        assert_true(is_very_valid_passphrase('abcde fghij'))
        assert_false(is_very_valid_passphrase('abcde xyz ecdab'))
        assert_true(is_very_valid_passphrase('a ab abc abd abf abj'))
        assert_true(is_very_valid_passphrase('iiii oiii ooii oooi oooo'))
        assert_false(is_very_valid_passphrase('oiii ioii iioi iiio'))
        
    def test_part2_works(self):
        with open('puzzle.txt') as f:
            assert_equal(208, sum(1 for passphrase in f.readlines() if is_very_valid_passphrase(passphrase)))
