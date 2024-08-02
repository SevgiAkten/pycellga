from cga.neighborhoods.compact_25 import Compact25


def test_compact_25():
    n_rows = 5
    n_cols = 5
    position = (3, 3)

    the_neighbors_positions = Compact25(
        position, n_rows, n_cols).calculate_neighbors_positions()
    assert len(the_neighbors_positions) == 24

    position = (5, 1)
    the_neighbors_positions = Compact25(
        position, n_rows, n_cols).calculate_neighbors_positions()
    assert len(the_neighbors_positions) == 24

    position = (1, 3)
    the_neighbors_positions = Compact25(
        position, n_rows, n_cols).calculate_neighbors_positions()
    assert len(the_neighbors_positions) == 24
