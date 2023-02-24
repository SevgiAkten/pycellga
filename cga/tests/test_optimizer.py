from optimizer import *
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


def test_optimizer():

    res = optimize()
    assert type(res) == tuple
    assert type(res[0]) == dict
    assert type(res[1]) == dict
    assert type(res[2]) == list
    assert type(res[3]) == list
