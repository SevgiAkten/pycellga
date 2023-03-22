from problems.single_objective.discrete.permutation.tsp import Tsp
from numpy import random
import tsplib95


def test_tsp():

    theproblem = Tsp()

    random.seed(0)
    assert theproblem.f(
        list(random.randint(1, 53, size=(52)))) == 32276.58323426501
    random.seed(50)
    assert theproblem.f(
        list(random.randint(1, 53, size=(52)))) == 29596.82092858752
    random.seed(100)
    assert theproblem.f(
        list(random.randint(1, 53, size=(52)))) == 25025.128223962678

    # Optimal tour
    with open("berlin52.opt.tour.txt") as o:
        best_route = tsplib95.read(o)
    assert theproblem.f(best_route.tours[0]) == 7544.365901904087
