from problems.single_objective.continuous.sphere import Sphere


def test_sphere():
    theproblem = Sphere()
    assert theproblem.f([2.305, -4.025, 3.805, -1.505]) == 38.2567
    assert theproblem.f([-4.995, -2.230, -3.706, 2.305]) == 48.970386000000005
    assert theproblem.f([0 for i in range(10)]) == 0
