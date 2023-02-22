import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from grid import Grid 

def test_grid():
    mygrid = Grid(5, 5)
    result = mygrid.make_2d_grid()
    assert type(result) == list
    assert len(result) == 25 
    assert type(result[0]) == tuple
    assert result[0] == (1, 1)
    assert result[len(result) - 1] == (5, 5)

