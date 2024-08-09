from neighborhoods.compact_9 import Compact9

def test_compact_9():
    """
    Test the Compact9 class for calculating neighbor positions in a grid.

    This test verifies that the Compact9 class correctly calculates the positions
    of the 8 neighbors surrounding a given position in a grid. It ensures that:
    1. The number of neighbors is always 8 for positions not on the boundary of the grid.
    2. Positions on the boundary of the grid still correctly return 8 neighbors.

    The test uses three different positions within the grid to validate the functionality
    of the Compact9 neighborhood calculation.

    Notes
    -----
    The Compact9 neighborhood considers all 8 surrounding cells in a 3x3 grid centered
    on a given position. The grid is assumed to be toroidal, meaning that positions on the
    edges wrap around to the opposite edge.

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
    the_neighbors_positions = Compact9(position, n_rows, n_cols).calculate_neighbors_positions()
    assert len(the_neighbors_positions) == 8, "The number of neighbors for a central position is not 8."

    # Test for a position near the bottom-left corner of the grid
    position = (5, 1)
    the_neighbors_positions = Compact9(position, n_rows, n_cols).calculate_neighbors_positions()
    assert len(the_neighbors_positions) == 8, "The number of neighbors for a bottom-left corner position is not 8."

    # Test for a position near the top-center of the grid
    position = (1, 3)
    the_neighbors_positions = Compact9(position, n_rows, n_cols).calculate_neighbors_positions()
    assert len(the_neighbors_positions) == 8, "The number of neighbors for a top-center position is not 8."
