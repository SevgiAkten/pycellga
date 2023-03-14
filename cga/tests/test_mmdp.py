from problems.single_objective.discrete.binary.mmdp import Mmdp


def test_mmdp():
    theproblem = Mmdp()
    assert theproblem.f([1 for i in range(240)]) == 40
    assert theproblem.f([0 for i in range(240)]) == 40
    assert theproblem.f([1 for m in range(140)] +
                        [0 for n in range(100)]) == 39.360383999999996
    assert theproblem.f([1 for m in range(25)] +
                        [0 for m in range(125)] + [0 for k in range(90)]) == 39.0
