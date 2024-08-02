from cga.problems.single_objective.continuous.schwefel import Schwefel


def test_schwefel():
    theproblem = Schwefel()
    assert theproblem.f([220.501, -400.025, 30.805, -105.50]
                        ) == round(1815.9104334968686, 3)
    assert theproblem.f([-400.995, -25.230, -410.706,
                        420.305]) == round(2008.8379872817275,3)
    assert round(theproblem.f([420.9687 for i in range(10)]), 2) == round(0.0, 3)
