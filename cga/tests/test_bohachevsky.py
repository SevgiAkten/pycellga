from cga.problems.single_objective.continuous.bohachevsky import Bohachevsky


def test_bohachevsky():
    theproblem = Bohachevsky()
    assert theproblem.f([2.305, -4.025, 3.805, -1.505]) == round(103.5844151636286, 3)
    assert theproblem.f([-4.995, -2.230, -3.706, 2.305]) == round(95.58203266386136,3)
    assert theproblem.f([0 for i in range(10)]) == round(0.0, 3)
