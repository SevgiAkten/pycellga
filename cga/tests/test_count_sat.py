from problems.single_objective.discrete.binary.count_sat import CountSat


def test_count_sat():
    theproblem = CountSat()
    # update values as normalized values
    # assert theproblem.f([1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1,
    #                     0, 1, 0, 0, 1, 0, 1, 0, 0]) == 6176
    # assert theproblem.f([0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1,
    #                     0, 1, 0, 0, 1, 0, 0, 0, 0]) == 6545
    # assert theproblem.f([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    #                     0, 0, 0, 0, 0, 0, 0, 0, 0]) == 5950
    assert theproblem.f([1 for i in range(20)]) == 1
