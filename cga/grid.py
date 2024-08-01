class Grid:
    """
    A class to represent a 2D grid.

    Attributes
    ----------
    n_rows : int
        Number of rows in the grid.
    n_cols : int
        Number of columns in the grid.
    """

    def __init__(self, n_rows: int, n_cols: int):
        """
        Initialize the Grid with the number of rows and columns.

        Parameters
        ----------
        n_rows : int
            Number of rows in the grid.
        n_cols : int
            Number of columns in the grid.
        """
        self.n_rows = n_rows
        self.n_cols = n_cols

    def make_2d_grid(self) -> list:
        """
        Create a 2D grid where each cell is represented by a tuple (row, column).

        Returns
        -------
        list
            A list of tuples where each tuple represents a grid cell.
            Each tuple is of the form (row, column), with rows and columns starting from 1.
        """
        grid = []
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                point = (i + 1, j + 1)
                grid.append(point)
        return grid
