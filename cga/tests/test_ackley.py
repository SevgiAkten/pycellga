from problems.single_objective.continuous.ackley import Ackley


def test_ackley():
    theproblem = Ackley()
    assert theproblem.f([15, 2.5, -25.502, -30.120]) == round(21.794472667169998, 3)
    assert theproblem.f([-13.75, -1.2, 4.20, 2.3]) == round(19.01754719776741, 3)
    assert theproblem.f([-15.2, -30.1]) == round(20.799510075569014, 3)
    assert theproblem.f([0, 0]) == round(0,3)
