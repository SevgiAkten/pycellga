import sys 
sys.path.append('..')

from Problems.Combinatorial.OneMax import OneMax

def test_onemax():
    theproblem = OneMax()
    assert theproblem.f([1, 1, 1, 1, 1]) == 5
    assert theproblem.f([1, 1, 1, 1, 1, 1]) == 6
    assert theproblem.f([0 for i in range(10)]) == 0
