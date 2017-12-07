from unittest import TestCase
from nose.tools import assert_equal


def parse_tower_info(s):
    tower_info = {}
    if '->' in s:
        subs = s.split('->')[1]
        tower_info['sub'] = [sub.replace(',','') for sub in subs.split()]
    tower_info['name'] = s.split()[0] 
    tower_info['weight'] = int(s[s.find('(')+1:s.find(')')])
    return tower_info


def bottom_tower(tower_infos):
    return next(tower for tower in tower_infos if is_bottom_tower(tower, tower_infos))


def is_bottom_tower(tower, tower_infos):
    return has_subs(tower) and not is_sub(tower, tower_infos)

def has_subs(tower):
    return 'sub' in tower.keys()


def is_sub(tower, tower_infos):
    return any(tower['name'] in t.get('sub', []) for t in tower_infos)


def calculate_balanced_weight(tower_infos):
    discs = []
    for tower in tower_infos:
        if has_subs(tower) and not is_bottom_tower(tower, tower_infos):
            discs.append({'name': tower['name'], 'weight': tower['weight'], 'sums': sum(get_weights(tower['name'], tower_infos))})
    unbalanced = None
    correct_balance = 0
    for disc in discs:
        if [d['sums'] for d in discs].count(disc['sums']) == 1:
            unbalanced = disc
        else:
            correct_balance = disc['sums']
    print(unbalanced)
    print(correct_balance)
    return abs(unbalanced['sums'] - correct_balance - unbalanced['weight'])
            


def get_weights(tower_name, tower_infos):
    main_tower = find_tower(tower_name, tower_infos)
    sub_towers = [tower for tower in tower_infos if tower['name'] in main_tower.get('sub', [])]
    return [main_tower['weight']] + [t['weight'] for t in sub_towers]


def find_tower(tower_name, tower_infos):
    return next(tower for tower in tower_infos if tower['name'] == tower_name)


class TestDay7(TestCase):

    def test_parse_tower_info(self):
        expected = {'name': 'fwft', 'weight': 72, 'sub': ['ktlj', 'cntj', 'xhth']}
        assert_equal(expected, parse_tower_info('fwft (72) -> ktlj, cntj, xhth'))
        assert_equal({'name': 'pbga', 'weight': 66}, parse_tower_info('pbga (66)'))

    def test_part1_examples(self):
        inputs = [
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
        tower_infos = [parse_tower_info(s) for s in inputs]
        assert_equal('tknk', bottom_tower(tower_infos)['name'])

    def test_part1_works(self):
        with open('puzzle.txt') as f:
            infos = [parse_tower_info(s) for s in f.readlines()]
            assert_equal('azqje', bottom_tower(infos)['name'])

    def test_part2_examples(self):
        inputs = [
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
        tower_infos = [parse_tower_info(s) for s in inputs]
        assert_equal([68, 61, 61, 61], get_weights('ugml', tower_infos))
        assert_equal(60, calculate_balanced_weight(tower_infos))

    def test_part2_works(self):
        with open('puzzle.txt') as f:
            infos = [parse_tower_info(s) for s in f.readlines()]
            assert_equal(60, calculate_balanced_weight(infos))
        

