ACCESS_POINT = 1
UP, RIGHT, DOWN, LEFT = 0, 90, 180, 270
DIRECTIONS = {UP: (-1, 0), RIGHT: (0, 1), DOWN: (1, 0), LEFT: (0, -1)}

class SpiralMemory:
    def __init__(self, max_slot):
        self.direction = RIGHT
        self.max_slot = max_slot
        self.row_length = int(pow(self.max_slot, 0.5))
        self.square_one = int((self.row_length-1)/2)
        self.memory = self._init_memory_slots()
        self.fill_memory_slots()

    def calcualte_distance(self, data):
        x_goal, y_goal = self.find_location(ACCESS_POINT)
        x, y = self.find_location(data)
        return abs(abs((x_goal - x)) + abs((y_goal - y)))

    def fill_memory_slots(self):
        x, y = self.square_one, self.square_one
        self.memory[x][y] = 1
        slots_to_fill = 1
        slot_value = 2
        for _ in range(self.row_length-1):
            for _ in range(slots_to_fill):
                x, y = self._next_slot(x, y)
                self.memory[x][y] = slot_value
                slot_value +=1
            self.direction = self._turn()
            for _ in range(slots_to_fill):
                x, y = self._next_slot(x, y)
                self.memory[x][y] = slot_value
                slot_value += 1
            self.direction = self._turn()
            slots_to_fill += 1
        for _ in range(slots_to_fill):
            x, y = self._next_slot(x, y)
            self.memory[x][y] = slot_value
            slot_value += 1
            if slot_value == self.max_slot+1:
                break

    def _next_slot(self, x, y):
        x += DIRECTIONS[self.direction][0]
        y += DIRECTIONS[self.direction][1]
        return x, y

    def _turn(self):
        return (self.direction + 270) % 360

    def _init_memory_slots(self):
        return [[0 for _ in self.row_range] for _ in self.row_range]

    def find_location(self, data):
        return next((i, j) for i in self.row_range for j in self.row_range 
                if self.memory[i][j] == data)

    @property
    def row_range(self):
        return range(self.row_length)


