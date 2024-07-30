from problems.single_objective.continuous.rosenbrock import Rosenbrock


def test_rosenbrock():
    theproblem = Rosenbrock()
    assert theproblem.f([2.305, -4.025, 3.805, -1.505]) == round(49665.553494187516, 3)
    assert theproblem.f([-4.995, -2.230, -3.706, 2.305]) == round(94539.42650987211, 3)
    assert theproblem.f([1 for i in range(10)]) == round(0, 3)
