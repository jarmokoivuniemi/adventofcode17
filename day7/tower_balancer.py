class TowerBalancer:
    def __init__(self, towers):
        self.towers = towers

    def bottom_tower(self):
        return next(tower for key, tower in self.towers.items() if self._is_bottom_tower(tower))

    def _is_bottom_tower(self, tower):
        return not any(self._is_child_of_other_towers(tower))

    def _is_child_of_other_towers(self, tower):
        return (tower['name'] in t.get('children', []) for key, t in self.towers.items())

    def weight_for_unbalanceed(self, father, result=[]):
        self._sum_weights_for_father_nodes(father)

        unbalanced, correct_value = self._find_unbalanced([self.towers[s] for s in father['children']])
        if unbalanced:
            result.append((unbalanced, correct_value))
            return self.weight_for_unbalanceed(unbalanced, result)
        else:
            unbalanced, correct_value = result[-1]
            return unbalanced['weight'] - (unbalanced['sum'] - correct_value)

    def _sum_weights_for_father_nodes(self, father):
        for children in father['children']:
            tower = self.towers[children]
            tower['sum'] = self._child_weights(tower)

    def _child_weights(self, father):
        result = 0
        for child in father.get('children', []):
            result += self._child_weights(self.towers[child])
        return father['weight'] + result

    def _find_unbalanced(self, towers):
        sums = [s['sum'] for s in towers]
        for tower in towers:
            if sums.count(tower['sum']) < 2:
                sums.remove(tower['sum'])
                return tower, sums[0]
        return None, None
