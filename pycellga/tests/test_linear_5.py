from neighborhoods.linear_5 import Linear5

def test_linear_5():
    """
    Test the Linear5 class for calculating neighbor positions in a grid.

    This test verifies that the Linear5 class correctly calculates the positions
    of the 4 neighbors surrounding a given position in a grid. It ensures that:
    1. The number of neighbors is always 4, which should include the positions 
       directly adjacent in the linear neighborhood.

    The test uses three different positions within the grid to validate the functionality
    of the Linear5 neighborhood calculation.

    Notes
    -----
    The Linear5 neighborhood considers 4 neighboring cells aligned in a linear fashion
    (left, right, up, and down) in a 5x5 grid centered on a given position.

    The following assertions are made:
    - The number of calculated neighbor positions is 4 for various positions in the grid.

    Raises
    ------
    AssertionError
        If the number of calculated neighbor positions is not 4.
    """
    n_rows = 5
    n_cols = 5

    # Test for a central position in the grid
    position = (3, 3)
    the_neighbors_positions = Linear5(position, n_rows, n_cols).calculate_neighbors_positions()
    assert len(the_neighbors_positions) == 4, "The number of neighbors for a central position is not 4."

    # Test for a position near the bottom-left corner of the grid
    position = (5, 1)
    the_neighbors_positions = Linear5(position, n_rows, n_cols).calculate_neighbors_positions()
    assert len(the_neighbors_positions) == 4, "The number of neighbors for a bottom-left corner position is not 4."

    # Test for a position near the top-center of the grid
    position = (1, 3)
    the_neighbors_positions = Linear5(position, n_rows, n_cols).calculate_neighbors_positions()
    assert len(the_neighbors_positions) == 4, "The number of neighbors for a top-center position is not 4."
