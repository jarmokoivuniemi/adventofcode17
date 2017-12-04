ACCESS_POINT = 1

class SpiralMemory:
    def __init__(self, max_slot):
        self.max_slot = max_slot
        self._free_memory_slots = 1
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
#right
        self.memory[x][y+1] = 2
#up
        self.memory[x-1][y+1] = 3
#left
        self.memory[x-1][y] = 4
        self.memory[x-1][y-1] = 5
#down
        self.memory[x][y-1] = 6
        self.memory[x+1][y-1] = 7
#right
        x += 1
        self.memory[x][y] = 8
        self.memory[x][y+1] = 9

        if self.row_length > self.square_one+2:
            y += 1
            self.memory[x][y+1] = 10
#up
            self.memory[x-1][y+1] = 11
            self.memory[x-2][y+1] = 12
            self.memory[x-3][y+1] = 13
#left
            self.memory[x-3][y] = 14
            self.memory[x-3][y-1] = 15
            self.memory[x-3][y-2] = 16
            self.memory[x-3][y-3] = 17
#down
            self.memory[x-2][y-3] = 18
            self.memory[x-1][y-3] = 19
            self.memory[x][y-3] = 20
            self.memory[x+1][y-3] = 21
#right
            self.memory[x+1][y-2] = 22
            


    def _fill_memory_slot(self, i, j):
        if not self.memory[i][j]:
            self.memory[i][j] = self._free_memory_slots
            self._free_memory_slots += 1

    def _init_memory_slots(self):
        return [[0 for _ in self.row_range] for _ in self.row_range]

    def find_location(self, data):
        return next((i, j) for i in self.row_range for j in self.row_range 
                if self.memory[i][j] == data)

    @property
    def row_range(self):
        return range(self.row_length)


