from problems.single_objective.discrete.permutation.tsp import Tsp
import random
import tsplib95


def test_tsp():

    theproblem = Tsp()

    random.seed(0)
    assert theproblem.f(
        list(random.sample(range(1, 53), 52))) == 29495.465603578683
    random.seed(50)
    assert theproblem.f(
        list(random.sample(range(1, 53), 52))) == 30518.155190953657
    random.seed(100)
    assert theproblem.f(
        list(random.sample(range(1, 53), 52))) == 31545.914565031067

    # Optimal tour
    with open("berlin52.opt.tour.txt") as o:
        best_route = tsplib95.read(o)
    assert theproblem.f(best_route.tours[0]) == 7544.365901904087
