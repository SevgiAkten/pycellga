from cga.problems.single_objective.discrete.binary.one_max import OneMax


def test_one_max():
    theproblem = OneMax()
    assert theproblem.f([1, 1, 1, 1, 1]) == 5
    assert theproblem.f([1, 1, 1, 1, 1, 1]) == 6
    assert theproblem.f([0 for i in range(10)]) == 0
