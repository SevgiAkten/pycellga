from cga.problems.single_objective.discrete.binary.one_max import OneMax
from cga.recombination.uniform_crossover import UniformCrossover
from cga.individual import Individual


def test_uniform_crossover():

    CHSIZE = 10

    indv1 = Individual(gen_type="Binary", ch_size=CHSIZE)
    indv2 = Individual(gen_type="Binary", ch_size=CHSIZE)

    indv1.randomize()
    indv2.randomize()

    parents = [indv1, indv2]

    theproblem = OneMax()

    ucx = UniformCrossover(parents, theproblem)
    child1, child2 = ucx.get_recombinations()

    assert child1.ch_size == child2.ch_size
    assert child1.ch_size == CHSIZE

    for i in range(CHSIZE):
        assert child1.chromosome[i] == 1 or child1.chromosome[i] == 0

    for i in range(CHSIZE):
        assert child2.chromosome[i] == 1 or child2.chromosome[i] == 0
