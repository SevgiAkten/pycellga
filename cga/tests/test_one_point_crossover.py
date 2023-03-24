from problems.single_objective.discrete.binary.one_max import OneMax
from recombination.one_point_crossover import OnePointCrossover
from individual import Individual


def test_one_point_crossover():

    CHSIZE = 10

    indv1 = Individual(gen_type="Binary", ch_size=CHSIZE)
    indv2 = Individual(gen_type="Binary", ch_size=CHSIZE)

    indv1.randomize()
    indv2.randomize()

    parents = [indv1, indv2]

    theproblem = OneMax()

    ucx = OnePointCrossover(parents, theproblem)
    child1, child2 = ucx.get_recombinations()

    assert child1.ch_size == child2.ch_size
    assert child1.ch_size == CHSIZE

    for i in range(CHSIZE):
        assert child1.chromosome[i] == 1 or child1.chromosome[i] == 0

    for i in range(CHSIZE):
        assert child2.chromosome[i] == 1 or child2.chromosome[i] == 0
