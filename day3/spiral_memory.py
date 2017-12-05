#Don't look at me
ACCESS_POINT = 1
UP, RIGHT, DOWN, LEFT = 0, 90, 180, 270
DIRECTIONS = {UP: (-1, 0), RIGHT: (0, 1), DOWN: (1, 0), LEFT: (0, -1)}
SIDES_BEFORE_TURN = 2

class SpiralMemory:
    def __init__(self, max_slot, hack=False, puzzle=0):
        self.puzzle = puzzle #i give up
        self.found = False
        self.part2_hack = hack
        self.direction = RIGHT
        self.max_slot = max_slot
        self.row_length = int(pow(self.max_slot, 0.5))
        self.square_one = int((self.row_length-1)/2)
        self.memory = self._init_memory_slots()
        self.make_spiral_memory()

    def calcualte_distance(self, data):
        x_goal, y_goal = self.find_location(ACCESS_POINT)
        x, y = self.find_location(data)
        return abs(abs((x_goal - x)) + abs((y_goal - y)))

    def make_spiral_memory(self):
        x, y = self.square_one, self.square_one
        self.memory[x][y] = 1
        slots_to_fill = 1
        slot_value = 2
        while not self.found:
            for _ in range(SIDES_BEFORE_TURN):
                for _ in range(slots_to_fill):
                    x, y = self._next_slot(x, y)
                    self.memory[x][y] = self._slot_value(x, y, slot_value)
                    slot_value +=1
                self._turn()
            slots_to_fill += 1

    def _next_slot(self, x, y):
        x += DIRECTIONS[self.direction][0]
        y += DIRECTIONS[self.direction][1]
        return x, y

    def _turn(self):
        self.direction = (self.direction + 270) % 360

    def _init_memory_slots(self):
        return [[0 for _ in self.row_range] for _ in self.row_range]

    def find_location(self, data):
        return next((x, y) for x in self.row_range for y in self.row_range 
                if self.memory[x][y] == data)

    @property
    def row_range(self):
        return range(self.row_length)

    def _slot_value(self, x, y, slot_value):
        result = slot_value if not self.part2_hack else sum(self._surrounding_elems(x, y)) 
        if result > self.puzzle and not self.found:
            self.puzzle = result
            self.found = True
        return result

    def _surrounding_elems(self, x, y):
        return [self.memory[a][b] for a in self._range(x) for b in self._range(y) if (a, b) != (x, y)]

    def _range(self, x):
        if x == self.row_length-1:
            return range(x-1, x+1)
        return range(x-1, x+2) if x > 0 else range(x, x+2)



