import sys
sys.path.append('..')

from grid import Grid 

def test_grid():
    mygrid = Grid(5, 5)
    result = mygrid.make_2d_grid()
    assert type(result) == list
    assert len(result) == 25 
    assert type(result[0]) == tuple
    assert result[0] == (1, 1)
    assert result[len(result) - 1] == (5, 5)

