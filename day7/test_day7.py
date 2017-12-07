from unittest import TestCase
from nose.tools import assert_equal


def parse_tower_info(s):
    tower_info = {}
    if '->' in s:
        subs = s.split('->')[1]
        tower_info['children'] = [children.strip() for children in subs.split(',')]
    tower_info['name'] = s.split()[0] 
    tower_info['weight'] = int(s[s.find('(')+1:s.find(')')])
    return tower_info


def bottom_tower(towers):
    return next(tower for key, tower in towers.items() if is_bottom_tower(tower, towers))


def is_bottom_tower(tower, towers):
    return not any(tower['name'] in t.get('children', []) for key, t in towers.items())


def balanced_weight(father, towers, result=[]):
    for children in father['children']:
        tower = towers[children]
        tower['sum'] = child_weights(tower, towers)

    unbalanced, correct_value = find_unbalanced([towers[s] for s in father['children']])
    if unbalanced:
        result.append((unbalanced, correct_value))
    else:
        unbalanced, correct_value = result[-1]
        return unbalanced['weight'] - (unbalanced['sum'] - correct_value)
    return balanced_weight(unbalanced, towers, result)
     

def child_weights(father, towers):
    result = 0
    for child in father.get('children', []):
        result += child_weights(towers[child], towers)
    return father['weight'] + result


def find_unbalanced(towers):
    sums = [s['sum'] for s in towers]
    for tower in towers:
        if sums.count(tower['sum']) < 2:
            sums.remove(tower['sum'])
            return tower, sums[0]
    return None, None


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
    def test_three_nodes(self):
        a = {'name': 'a', 'weight': 1, 'children': ['b']}
        b = {'name': 'b', 'weight': 2, 'children': ['c']}
        c = {'name': 'c', 'weight': 3}
        assert_equal(6, child_weights(a, {s['name']: s for s in [a,b,c]}))

    def test_four_nodes(self):
        a = {'name': 'a', 'weight': 1, 'children': ['b']}
        b = {'name': 'b', 'weight': 2, 'children': ['c', 'd']}
        c = {'name': 'c', 'weight': 3}
        d = {'name': 'd', 'weight': 4}
        assert_equal(10, child_weights(a, {s['name']: s for s in [a,b,c,d]}))

    def test_five_nodes(self):
        a = {'name': 'a', 'weight': 1, 'children': ['b', 'c']}
        b = {'name': 'b', 'weight': 2, 'children': ['d', 'e']}
        c = {'name': 'c', 'weight': 3}
        d = {'name': 'd', 'weight': 4}
        e = {'name': 'e', 'weight': 4}
        assert_equal(14, child_weights(a, {s['name']: s for s in [a,b,c,d,e]}))

    def test_six_nodes(self):
        a = {'name': 'a', 'weight': 1, 'children': ['b', 'c']}
        b = {'name': 'b', 'weight': 2, 'children': ['d', 'e']}
        c = {'name': 'c', 'weight': 3, 'children': ['f']}
        d = {'name': 'd', 'weight': 4}
        e = {'name': 'e', 'weight': 5}
        f = {'name': 'f', 'weight': 6}
        assert_equal(21, child_weights(a, {s['name']: s for s in [a,b,c,d,e,f]}))

    def test_parse_tower_info(self):
        expected = {'name': 'fwft', 'weight': 72, 'children': ['ktlj', 'cntj', 'xhth']}
        assert_equal(expected, parse_tower_info('fwft (72) -> ktlj, cntj, xhth'))
        assert_equal({'name': 'pbga', 'weight': 66}, parse_tower_info('pbga (66)'))

    def test_part1_examples(self):
        towers = {parse_tower_info(s)['name']: parse_tower_info(s) for s in self.example}
        assert_equal('tknk', bottom_tower(towers)['name'])

    def test_part1_works(self):
        with open('puzzle.txt') as f:
            infos = {parse_tower_info(s)['name']: parse_tower_info(s) for s in f.readlines()}
            assert_equal('azqje', bottom_tower(infos)['name'])

    def test_part2_examples(self):
        towers = {parse_tower_info(s)['name']: parse_tower_info(s) for s in self.example}
        bottom = bottom_tower(towers)
        assert_equal(60, balanced_weight(bottom, towers))

    def test_part2_works(self):
        with open('puzzle.txt') as f:
            infos = {parse_tower_info(s)['name']: parse_tower_info(s) for s in f.readlines()}
            bottom = bottom_tower(infos)
            assert_equal(646, balanced_weight(bottom, infos))
        

