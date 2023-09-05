from problems.single_objective.discrete.binary.fms import Fms
from numpy import random


def test_fms():

    theproblem = Fms()

    random.seed(0)
    assert theproblem.f([random.randint(2)
                        for g in range(192)]) == 73.42012162437729
    random.seed(45)
    assert theproblem.f([random.randint(2)
                        for g in range(192)]) == 231.0973828479809
    random.seed(50)
    assert theproblem.f([random.randint(2)
                        for g in range(192)]) == 663.4403491286715
