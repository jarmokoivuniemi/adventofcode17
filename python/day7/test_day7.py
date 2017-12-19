from unittest import TestCase
from nose.tools import assert_equal
from tower_balancer import TowerBalancer


def parse_tower_info(s):
    tower_info = {}
    if '->' in s:
        subs = s.split('->')[1]
        tower_info['children'] = [children.strip() for children in subs.split(',')]
    tower_info['name'] = s.split()[0]
    tower_info['weight'] = int(s[s.find('(')+1:s.find(')')])
    return tower_info


class TestDay7(TestCase):
    example = [
            'pbga (66)',
            'xhth (57)',
            'ebii (61)',
            'havc (66)',
            'ktlj (57)',
            'fwft (72) -> ktlj, cntj, xhth',
            'qoyq (66)',
            'padx (45) -> pbga, havc, qoyq',
            'tknk (41) -> ugml, padx, fwft',
            'jptl (61)',
            'ugml (68) -> gyxo, ebii, jptl',
            'gyxo (61)',
            'cntj (57)',
        ]

    def puzzle_towers(self):
        with open('puzzle.txt') as f:
            return {parse_tower_info(s)['name']: parse_tower_info(s) for s in f.readlines()}

    def example_towers(self):
        return {parse_tower_info(s)['name']: parse_tower_info(s) for s in self.example}

    def test_parse_tower_info_with_children(self):
        expected = {'name': 'fwft', 'weight': 72, 'children': ['ktlj', 'cntj', 'xhth']}
        assert_equal(expected, parse_tower_info('fwft (72) -> ktlj, cntj, xhth'))

    def test_parse_tower_info_without_children(self):
        assert_equal({'name': 'pbga', 'weight': 66}, parse_tower_info('pbga (66)'))

    def test_sum_weights_for_node_with_two_children_each_with_their_own_children(self):
        a = {'name': 'a', 'weight': 1, 'children': ['b', 'c']}
        b = {'name': 'b', 'weight': 2, 'children': ['d', 'e']}
        c = {'name': 'c', 'weight': 3, 'children': ['f']}
        d = {'name': 'd', 'weight': 4}
        e = {'name': 'e', 'weight': 5}
        f = {'name': 'f', 'weight': 6}
        balancer = TowerBalancer({s['name']: s for s in [a, b, c, d, e, f]})
        assert_equal(21, balancer._child_weights(a))

    def test_part1_examples(self):
        balancer = TowerBalancer(self.example_towers())
        assert_equal('tknk', balancer.bottom_tower()['name'])

    def test_part1_works(self):
        balancer = TowerBalancer(self.puzzle_towers())
        assert_equal('azqje', balancer.bottom_tower()['name'])

    def test_part2_examples(self):
        balancer = TowerBalancer(self.example_towers())
        bottom = balancer.bottom_tower()
        assert_equal(60, balancer.weight_for_unbalanceed(bottom))

    def test_part2_works(self):
        balancer = TowerBalancer(self.puzzle_towers())
        bottom = balancer.bottom_tower()
        assert_equal(646, balancer.weight_for_unbalanceed(bottom))
