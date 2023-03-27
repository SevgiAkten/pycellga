from neighborhoods.compact_21 import Compact21


def test_compact_21():
    n_rows = 5
    n_cols = 5
    position = (3, 3)

    the_neighbors_positions = Compact21(
        position, n_rows, n_cols).calculate_neighbors_positions()
    assert len(the_neighbors_positions) == 20

    position = (5, 1)
    the_neighbors_positions = Compact21(
        position, n_rows, n_cols).calculate_neighbors_positions()
    assert len(the_neighbors_positions) == 20

    position = (1, 3)
    the_neighbors_positions = Compact21(
        position, n_rows, n_cols).calculate_neighbors_positions()
    assert len(the_neighbors_positions) == 20
