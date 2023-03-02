from optimizer import *


def test_optimizer():

    res = optimize()
    assert type(res) == tuple
    assert type(res[0]) == dict
    assert type(res[1]) == dict
    assert type(res[2]) == list
    assert type(res[3]) == list
