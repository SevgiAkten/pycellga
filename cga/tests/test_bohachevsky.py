from problems.single_objective.continuous.bohachevsky import Bohachevsky


def test_bohachevsky():
    theproblem = Bohachevsky()
    assert theproblem.f(-90.203, -55.305) == 14254.976198413928
    assert theproblem.f(10.780, 17.624) == 737.9695994818161
    assert theproblem.f(0, 0) == 0.0
