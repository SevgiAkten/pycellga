from problems.single_objective.continuous.ackley import Ackley


def test_ackley():
    theproblem = Ackley()
    assert theproblem.f(15, 2.5) == 19.38995256329671
    assert theproblem.f(-10, -1) == 15.171841011518415
    assert theproblem.f(0, 0) == 0.0
