from problems.single_objective.continuous.rastrigin import Rastrigin


def test_rastrigin():
    theproblem = Rastrigin()
    assert theproblem.f([2.305, -4.025, 3.805, -1.505]) == 78.37488219770594
    assert theproblem.f([-4.995, -2.230, -3.706, 2.305]) == 83.83888661832582
    assert theproblem.f([0 for i in range(10)]) == 0.0
