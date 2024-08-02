class Compact9:
    """
    Compact9 calculates the positions of the 8 neighbors in a 2D grid for a given position,
    considering wrapping at the grid edges.

    Parameters
    ----------
    position : tuple
        The (x, y) position of the point whose neighbors are to be calculated.
    n_rows : int
        The number of rows in the grid.
    n_cols : int
        The number of columns in the grid.
    """

    def __init__(self, position, n_rows, n_cols):
        """
        Initialize the Compact9 object.

        Parameters
        ----------
        position : tuple
            The (x, y) position of the point whose neighbors are to be calculated.
        n_rows : int
            The number of rows in the grid.
        n_cols : int
            The number of columns in the grid.
        """
        self.position = position
        self.n_rows = n_rows
        self.n_cols = n_cols

    def calculate_neighbors_positions(self) -> list:
        """
        Calculate the positions of the 8 neighbors for the given position in the grid.

        The neighbors are determined by considering wrapping at the grid edges.

        Returns
        -------
        list
            A list of tuples representing the positions of the 8 neighbors.
        """
        neighbors_positions = []
        point = self.position
        x = point[0]
        y = point[1]

        # Change in x and y for the 8 neighbors
        dx = [-1, -1, -1, 0, 1, 1, 1, 0]
        dy = [-1, 0, 1, -1, -1, 0, 1, 1]

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
