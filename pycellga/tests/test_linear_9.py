from neighborhoods.linear_9 import Linear9

def test_linear_9():
    """
    Test the Linear9 class for calculating neighbor positions in a grid.

    This test verifies that the Linear9 class correctly calculates the positions
    of the 8 neighbors surrounding a given position in a grid. It ensures that:
    1. The number of neighbors is always 8, which should include the positions 
       surrounding the given position in the linear neighborhood.

    The test uses three different positions within the grid to validate the functionality
    of the Linear9 neighborhood calculation.

    Notes
    -----
    The Linear9 neighborhood considers 8 neighboring cells aligned in a linear fashion
    (left, right, up, down, and the diagonals) in a 5x5 grid centered on a given position.

    The following assertions are made:
    - The number of calculated neighbor positions is 8 for various positions in the grid.

    Raises
    ------
    AssertionError
        If the number of calculated neighbor positions is not 8.
    """
    n_rows = 5
    n_cols = 5

    # Test for a central position in the grid
    position = (3, 3)
    the_neighbors_positions = Linear9(position, n_rows, n_cols).calculate_neighbors_positions()
    assert len(the_neighbors_positions) == 8, "The number of neighbors for a central position is not 8."

    # Test for a position near the bottom-left corner of the grid
    position = (5, 1)
    the_neighbors_positions = Linear9(position, n_rows, n_cols).calculate_neighbors_positions()
    assert len(the_neighbors_positions) == 8, "The number of neighbors for a bottom-left corner position is not 8."

    # Test for a position near the top-center of the grid
    position = (1, 3)
    the_neighbors_positions = Linear9(position, n_rows, n_cols).calculate_neighbors_positions()
    assert len(the_neighbors_positions) == 8, "The number of neighbors for a top-center position is not 8."
