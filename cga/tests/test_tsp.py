from problems.single_objective.discrete.permutation.tsp import Tsp

import random


def test_tsp():

    theproblem = Tsp()

    random.seed(0)
    assert theproblem.f(
        list(random.sample(range(1, 15), 14))) == 6094.6
    random.seed(50)
    assert theproblem.f(
        list(random.sample(range(1, 15), 14))) == 6879.0
    random.seed(100)
    assert theproblem.f(
        list(random.sample(range(1, 15), 14))) == 8222.0
