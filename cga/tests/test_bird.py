from problems.single_objective.continuous.bird import Bird


def test_bird():
    theproblem = Bird()
    assert theproblem.f(1.504, 2.130) == 21.16076264956393
    assert theproblem.f(4.124, -2.702) == -26.253821134407204
    assert theproblem.f(4.70104, 3.15294) == -106.7785949110127
    assert theproblem.f(-1.58214, -3.13024) == -106.77859490782035
