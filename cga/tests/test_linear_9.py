from cga.neighborhoods.linear_9 import Linear9


def test_linear_9():
    n_rows = 5
    n_cols = 5
    position = (3, 3)

    the_neighbors_positions = Linear9(
        position, n_rows, n_cols).calculate_neighbors_positions()
    assert len(the_neighbors_positions) == 8

    position = (5, 1)
    the_neighbors_positions = Linear9(
        position, n_rows, n_cols).calculate_neighbors_positions()
    assert len(the_neighbors_positions) == 8

    position = (1, 3)
    the_neighbors_positions = Linear9(
        position, n_rows, n_cols).calculate_neighbors_positions()
    assert len(the_neighbors_positions) == 8
