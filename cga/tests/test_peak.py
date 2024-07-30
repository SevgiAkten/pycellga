from problems.single_objective.discrete.binary.peak import Peak
from numpy import random

""" Note:
The max fitness of p-peak problem is equal to 1.0 and this is only possible when x (that represent chromosome) or p_target values be fielded opposite of 0 and 1 like this:
    x = [[1 for g in range(100)]for h in range(100)]
    p_target = [[0 for g in range(100)]for h in range(100)]
When I did this test manually, I saw that it gave expected max fitness value, 1.0.
Because p_target is fielded in Peak class, we cannot intervene it from test script. Maybe it is possibble to send p_target value as f function parameter, but I didn't need it at this stage. 
"""


def test_peak():

    theproblem = Peak()

    random.seed(45)
    assert theproblem.f([[random.randint(2) for g in range(100)]
                        for h in range(100)]) == round(0.49,3)

    random.seed(50)
    assert theproblem.f([[random.randint(2) for g in range(100)]
                         for h in range(100)]) == round(0.6, 3)
    random.seed(100)
    assert theproblem.f([[random.randint(2) for g in range(100)]
                         for h in range(100)]) == round(0.0, 3)
