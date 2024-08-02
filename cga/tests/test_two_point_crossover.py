import numpy as np
from cga.problems.single_objective.discrete.binary.one_max import OneMax
from cga.recombination.two_point_crossover import TwoPointCrossover
from cga.individual import Individual

def test_two_point_crossover():
    """
    Test the TwoPointCrossover class implementation.

    This test verifies the functionality of the two-point crossover on a pair of parent individuals.
    """
    CHSIZE = 10

    indv1 = Individual(gen_type="Binary", ch_size=CHSIZE)
    indv2 = Individual(gen_type="Binary", ch_size=CHSIZE)

    indv1.randomize()
    indv2.randomize()

    parents = [indv1, indv2]

    theproblem = OneMax()

    ucx = TwoPointCrossover(parents, theproblem)
    child1, child2 = ucx.get_recombinations()

    assert child1.ch_size == child2.ch_size
    assert child1.ch_size == CHSIZE

    for i in range(CHSIZE):
        assert child1.chromosome[i] == 1 or child1.chromosome[i] == 0

    for i in range(CHSIZE):
        assert child2.chromosome[i] == 1 or child2.chromosome[i] == 0

if __name__ == "__main__":
    test_two_point_crossover()
