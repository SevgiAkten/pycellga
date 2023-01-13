class Grid:
    def __init__(self, n_rows, n_cols):
        self.n_rows = n_rows
        self.n_cols = n_cols

    def make2DGrid(n_rows, n_cols):
        grid = []
        for i in range(n_rows - 1):
            for j in range(n_cols - 1):
                point = (i + 1, j + 1)
                grid.append(point)
        return grid
