from neighborhoods.compact_13 import Compact13


def test_compact_13():
    n_rows = 5
    n_cols = 5
    position = (3, 3)

    the_neighbors_positions = Compact13(
        position, n_rows, n_cols).calculate_neighbors_positions()
    assert len(the_neighbors_positions) == 12

    position = (5, 1)
    the_neighbors_positions = Compact13(
        position, n_rows, n_cols).calculate_neighbors_positions()
    assert len(the_neighbors_positions) == 12

    position = (1, 3)
    the_neighbors_positions = Compact13(
        position, n_rows, n_cols).calculate_neighbors_positions()
    assert len(the_neighbors_positions) == 12
