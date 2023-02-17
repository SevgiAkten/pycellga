class Grid:
    def __init__(self, n_rows, n_cols):
        self.n_rows = n_rows
        self.n_cols = n_cols

    def make_2d_grid(self):
        grid = []
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                point = (i + 1, j + 1)
                grid.append(point)
        return grid
