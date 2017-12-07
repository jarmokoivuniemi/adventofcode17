from unittest import TestCase, skip
from nose.tools import assert_equal


def balanced_memory_banks(memory_banks):
    found_configs = []
    while found_configs.count(memory_banks) < 2:
        found_configs.append(list(balance(memory_banks)))
    return found_configs


def balance(memory_banks):
    largest_bank = memory_banks.index(max(memory_banks))
    for i in range(1, memory_banks[largest_bank]+1):
        memory_banks[(largest_bank + i) % len(memory_banks)] += 1
        memory_banks[largest_bank] -= 1
    return memory_banks


def cycles_between_duplicates(found):
    return len(found) - 1 - found.index(found[len(found) - 1])


class TestDay6(TestCase):

    def test_part1_examples(self):
        assert_equal([2, 4, 1, 2], balance([0, 2, 7, 0]))
        assert_equal([3, 1, 2, 3], balance([2, 4, 1, 2]))

        assert_equal(5, len(balanced_memory_banks([0, 2, 7, 0])))

    @skip('slow')
    def test_part1_works(self):
        with open('puzzle.txt') as f:
            memory_banks = [int(s.strip()) for s in f.read().split()]
            assert_equal(14029, len(balanced_memory_banks(memory_banks)))

    def test_part2_examples(self):
        memory_banks = [0, 2, 7, 0]
        found = balanced_memory_banks(memory_banks)
        assert_equal(4, cycles_between_duplicates(found))

    @skip('slow')
    def test_part2_works(self):
        with open('puzzle.txt') as f:
            memory_banks = [int(s.strip()) for s in f.read().split()]
            found = balanced_memory_banks(memory_banks)
            assert_equal(2765, cycles_between_duplicates(found))
