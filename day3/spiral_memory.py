class SpiralMemory:
    def __init__(self, max_slot):
        self.max_slot = max_slot
        self._free_memory_slots = max_slot
        self.row_length = int(pow(self.max_slot, 0.5))
        self.square_one = int((self.row_length-1)/2)
        self.spiral_memory()

    def calcualte_distance(self, data):
        x_goal, y_goal = self.find_location(1)
        x, y = self.find_location(data)
        return abs(abs((x_goal - x)) + abs((y_goal - y)))

    def spiral_memory(self):
        self.memory = self._init_memory_slots()
        for roundnum in range(self.square_one, -1, -1):
            self._spiral_left(roundnum)
            self._spiral_up(roundnum)
            self._spiral_right(roundnum)
            self._spiral_down(roundnum)

    def _spiral_left(self, roundnum):
        i = self.square_one + roundnum
        for j in range(self.row_length-1, -1, -1):
            if not self.memory[i][j]:
                self.memory[i][j] = self._free_memory_slots
                self._free_memory_slots -= 1

    def _spiral_up(self, roundnum):
        j = self.square_one - roundnum
        for i in range(self.row_length-1, -1, -1):
            if not self.memory[i][j]:
                self.memory[i][j] = self._free_memory_slots
                self._free_memory_slots -= 1

    def _spiral_right(self, roundnum):
        i = self.square_one - roundnum - self.row_length
        for j in range(self.row_length):
            if not self.memory[i][j]:
                self.memory[i][j] = self._free_memory_slots
                self._free_memory_slots -= 1 

    def _spiral_down(self, roundnum):
        j = self.square_one + roundnum
        for i in range(self.row_length-1):
            if not self.memory[i][j]:
                self.memory[i][j] = self._free_memory_slots
                self._free_memory_slots -= 1

    def _init_memory_slots(self):
        return [[None for _ in range(self.row_length)] for _ in range(self.row_length)]

    def find_location(self, data):
        for i in range(self.row_length):
            for j in range(self.row_length):
                if self.memory[i][j] == data:
                    return (i, j)


