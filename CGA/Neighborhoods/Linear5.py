class Linear5:
    def __init__(self, position, n_rows, n_cols):
        self.position = position
        self.n_rows = n_rows
        self.n_cols = n_cols

    def calculateNeighborsPositions(self):
        neighbors_positions = []
        point = self.position
        x = point[0]
        y = point[1]

        if x == self.n_rows or y == self.n_cols:
            pass
        # burası yazılacak
        else:
            n_right = (x, y + 1)
            n_left = (x, y - 1)
            n_above = (x - 1, y)
            n_belove = (x + 1, y)
            pass

        neighbors_positions.append()

        return neighbors_positions


deneme = Linear5((3, 3), 5).calculateNeighborsPositions()
print(deneme)
