
"""
    The Compact25 neighborhood type is used in Cellular Genetic Algorithms to define a large local 
    neighborhood of cells. In this configuration, each cell is surrounded by its 24 immediate neighbors 
    in a grid (excluding the outermost rows and columns) plus itself, forming a compact 25-cell 
    neighborhood. This setup allows each cell to consider the influence of a substantial area around it, 
    including all cells within the grid. Compact25 is particularly useful for capturing interactions 
    over a broad local region, providing a detailed view of neighboring cells and enhancing the ability to 
    explore and exploit complex local patterns and structures in cellular genetic algorithms.
"""
class Compact25:
    def __init__(self, position, n_rows, n_cols):
        self.position = position
        self.n_rows = n_rows
        self.n_cols = n_cols

    def calculate_neighbors_positions(self) -> list:
        neighbors_positions = []
        point = self.position
        x = point[0]
        y = point[1]
        dx = [-2, -2, -2, -2, -2, -1, -1, -1, -1, -1, 0, 0,
              0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]  # Change in x
        dy = [-2, -1, 0, 1, 2, -2, -1, 0, 1, 2, -2, -1, 1,
              2, -2, -1, 0, 1, 2, -2, -1, 0, 1, 2]  # Change in y

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
