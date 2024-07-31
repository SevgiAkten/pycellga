
"""
    The Compact13 neighborhood type is used in Cellular Genetic Algorithms to define a local 
    neighborhood of cells with a slightly larger range. In this configuration, each cell is surrounded 
    by its 12 immediate neighbors in a grid (excluding the corners) plus itself, forming a compact 
    13-cell neighborhood. This setup allows each cell to consider the influence of a broader area 
    around it, including diagonal and edge-adjacent cells. Compact13 is useful for capturing interactions 
    over a larger local region compared to Compact9, providing a more extensive view of neighboring cells 
    and enabling better exploration of local patterns and structures in cellular genetic algorithms.
"""

class Compact13:
    def __init__(self, position, n_rows, n_cols):
        self.position = position
        self.n_rows = n_rows
        self.n_cols = n_cols

    def calculate_neighbors_positions(self) -> list:
        neighbors_positions = []
        point = self.position
        x = point[0]
        y = point[1]
        dx = [-2, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 2]  # Change in x
        dy = [0, -1, 0, 1, -2, -1, 1, 2, -1, 0, 1, 0]  # Change in y

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
