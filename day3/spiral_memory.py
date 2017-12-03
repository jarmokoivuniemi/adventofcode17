ACCESS_POINT = 1

class SpiralMemory:
    def __init__(self, max_slot):
        self.max_slot = max_slot
        self._free_memory_slots = max_slot
        self.row_length = int(pow(self.max_slot, 0.5))
        self.square_one = int((self.row_length-1)/2)
        self.memory = self._init_memory_slots()
        self.fill_memory_slots()

    def calcualte_distance(self, data):
        x_goal, y_goal = self.find_location(ACCESS_POINT)
        x, y = self.find_location(data)
        return abs(abs((x_goal - x)) + abs((y_goal - y)))

    def fill_memory_slots(self):
        for spiral_round in range(self.square_one, -1, -1):
            self._spiral_left(spiral_round)
            self._spiral_up(spiral_round)
            self._spiral_right(spiral_round)
            self._spiral_down(spiral_round)

    def _spiral_left(self, spiral_round):
        for j in range(self.row_length-1, -1, -1):
            self._fill_memory_slot(self.square_one + spiral_round, j)

    def _spiral_up(self, spiral_round):
        for i in range(self.row_length-1, -1, -1):
            self._fill_memory_slot(i, self.square_one - spiral_round)

    def _spiral_right(self, spiral_round):
        for j in self.row_range:
            self._fill_memory_slot(self.square_one - spiral_round, j)

    def _spiral_down(self, spiral_round):
        for i in self.row_range:
            self._fill_memory_slot(i, self.square_one + spiral_round)

    def _init_memory_slots(self):
        return [[None for _ in self.row_range] for _ in self.row_range]

    def _fill_memory_slot(self, i, j):
        if not self.memory[i][j]:
            self.memory[i][j] = self._free_memory_slots
            self._free_memory_slots -= 1

    def find_location(self, data):
        return next((i, j) for i in self.row_range for j in self.row_range 
                if self.memory[i][j] == data)

    @property
    def row_range(self):
        return range(self.row_length)


