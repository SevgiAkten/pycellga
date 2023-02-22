import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from problems.combinatorial.one_max import OneMax

def test_one_max():
    theproblem = OneMax()
    assert theproblem.f([1, 1, 1, 1, 1]) == 5
    assert theproblem.f([1, 1, 1, 1, 1, 1]) == 6
    assert theproblem.f([0 for i in range(10)]) == 0
