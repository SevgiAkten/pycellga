from neighborhoods.linear_5 import Linear5


def test_linear_5():
    n_rows = 5
    n_cols = 5
    position = (3, 3)

    the_neighbors_positions = Linear5(
        position, n_rows, n_cols).calculate_neighbors_positions()
    assert len(the_neighbors_positions) == 4

    position = (5, 1)
    the_neighbors_positions = Linear5(
        position, n_rows, n_cols).calculate_neighbors_positions()
    assert len(the_neighbors_positions) == 4

    position = (1, 3)
    the_neighbors_positions = Linear5(
        position, n_rows, n_cols).calculate_neighbors_positions()
    assert len(the_neighbors_positions) == 4
