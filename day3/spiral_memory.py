class SpiralMemory:
    def __init__(self, max_slot):
        self.memory = self.spiral(max_slot)

    def calcualte_distance(self, data):
        x_goal, y_goal = self.find_location(1)
        x, y = self.find_location(data)
        return abs(abs((x_goal - x)) + abs((y_goal - y)))


    def spiral(self, max_value):
        result = []
        size = int(pow(max_value, 0.5))
        for i in range(size):
            inner = []
            for j in range(size):
                inner.append(None)
            result.append(inner)

        middle = int((size-1)/2)
        num = max_value

        for roundnum in range(middle, -1, -1):
            i = middle + roundnum
            for j in range(size-1, -1, -1):
                if not result[i][j]:
                    result[i][j] = num
                    num -= 1

            j = middle - roundnum
            for i in range(size-1, -1, -1):
                if not result[i][j]:
                    result[i][j] = num
                    num -= 1

            i = middle - roundnum-size
            for j in range(size):
                if not result[i][j]:
                    result[i][j] = num
                    num -= 1 

            j = middle + roundnum + 0
            for i in range(size-1):
                if not result[i][j]:
                    result[i][j] = num
                    num -= 1

        return result

    def find_location(self, data):
        for i in range(len(self.memory)):
            for j in range(len(self.memory)):
                if self.memory[i][j] == data:
                    return (i, j)


