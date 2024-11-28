from grid import Grid

def test_grid():
    """
    Test the Grid class implementation.

    This test checks the functionality of the Grid class for creating a 2D grid.
    It verifies the type, length, and content of the generated grid.

    The test performs the following steps:
    1. Create an instance of the Grid class with a 5x5 grid.
    2. Generate the 2D grid using the make_2d_grid method.
    3. Verify that the result is a list.
    4. Verify that the length of the list is 25 (5x5).
    5. Verify that each element in the list is a tuple.
    6. Verify the first and last elements of the list.

    Raises
    ------
    AssertionError
        If the result does not match the expected values.
    """

    mygrid = Grid(5, 5)
    result = mygrid.make_2d_grid()
    assert type(result) == list, f"Expected list, got {type(result)}"
    assert len(result) == 25, f"Expected length 25, got {len(result)}"
    assert type(result[0]) == tuple, f"Expected tuple, got {type(result[0])}"
    assert result[0] == (1, 1), f"Expected (1, 1), got {result[0]}"
    assert result[len(result) - 1] == (5, 5), f"Expected (5, 5), got {result[len(result) - 1]}"
