
"""
    The Linear5 neighborhood type is used in Cellular Genetic Algorithms to define a linear local 
    neighborhood of cells. In this configuration, each cell is surrounded by its 4 immediate neighbors 
    in a straight line, forming a linear 5-cell neighborhood. This setup considers cells that are directly 
    adjacent to the target cell in a one-dimensional arrangement, either horizontally or vertically. 
    Linear5 is useful for capturing interactions along a specific direction, allowing for efficient 
    exploration of linear patterns and structures in cellular genetic algorithms. This neighborhood type 
    helps in focusing on local dependencies and trends along a single axis.
"""
class Linear5:
    def __init__(self, position, n_rows, n_cols):
        self.position = position
        self.n_rows = n_rows
        self.n_cols = n_cols

    def calculate_neighbors_positions(self) -> list:
        neighbors_positions = []
        point = self.position
        x = point[0]
        y = point[1]
        dx = [0, 0, -1, 1]  # Change in x
        dy = [1, -1, 0, 0]  # Change in y

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