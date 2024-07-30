from problems.single_objective.continuous.rastrigin import Rastrigin


def test_rastrigin():
    theproblem = Rastrigin()
    assert theproblem.f([2.305, -4.025, 3.805, -1.505]) == round(78.37488219770594, 3)
    assert theproblem.f([-4.995, -2.230, -3.706, 2.305]) == round(83.83888661832582,3)
    assert theproblem.f([0 for i in range(10)]) == round(0.0, 3)
