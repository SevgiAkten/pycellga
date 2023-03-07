from problems.single_objective.continuous.rosenbrock import Rosenbrock


def test_rosenbrock():
    theproblem = Rosenbrock()
    assert theproblem.f([2.305, -4.025, 3.805, -1.505]) == 49665.553494187516
    assert theproblem.f([-4.995, -2.230, -3.706, 2.305]) == 94539.42650987211
    assert theproblem.f([1 for i in range(10)]) == 0
