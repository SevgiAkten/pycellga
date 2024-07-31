
"""
    The Linear9 neighborhood type is used in Cellular Genetic Algorithms to define a linear local 
    neighborhood of cells with a larger range. In this configuration, each cell is surrounded by its 
    8 immediate neighbors in a straight line, extending in both directions, plus itself, forming a 
    linear 9-cell neighborhood. This setup considers cells that are directly adjacent to the target cell 
    in a one-dimensional arrangement, either horizontally or vertically, covering a broader span. 
    Linear9 is useful for capturing longer-range interactions along a specific direction, allowing for 
    a more comprehensive exploration of linear patterns and trends in cellular genetic algorithms. 
    This neighborhood type facilitates the analysis of dependencies and structures along a single axis 
    with a greater reach.
"""
class Linear9:
    def __init__(self, position, n_rows, n_cols):
        self.position = position
        self.n_rows = n_rows
        self.n_cols = n_cols

    def calculate_neighbors_positions(self) -> list:
        neighbors_positions = []
        point = self.position
        x = point[0]
        y = point[1]
        dx = [-2, -1, 0, 0, 1, 2, 0, 0]  # Change in x
        dy = [0, 0, -2, -1, 0, 0, 1, 2]  # Change in y

        if x == self.n_rows or y == self.n_rows:
            for i in range(len(dx)):
                npx = (x + dx[i]) % self.n_rows
                npy = (y + dy[i]) % self.n_rows
                if npx == 0:
                    npx = self.n_rows
                if npy == 0:
                    npy = self.n_rows

                neighbor_position = (npx, npy)
                neighbors_positions.append(neighbor_position)

        elif x != self.n_rows or y != self.n_rows:
            for i in range(len(dx)):
                npx = x + dx[i]
                npy = y + dy[i]
                if npx == 0:
                    npx = self.n_rows
                if npy == 0:
                    npy = self.n_rows

                neighbor_position = (npx, npy)
                neighbors_positions.append(neighbor_position)

        return neighbors_positions
