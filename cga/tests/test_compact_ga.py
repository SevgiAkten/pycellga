from compact_ga import Compact_GA
from problems.single_objective.discrete.binary.one_max import OneMax


def test_compact_ga():
    # Compact GA parameters:
    pop_size = 100
    ch_size = 50
    n_gen = 200

    ind = Compact_GA(pop_size=pop_size, ch_size=ch_size, n_gen=n_gen).run()
    theproblem = OneMax()

    assert ind.ch_size == ch_size
    assert ind.fitness_value == theproblem.f(ind.chromosome)
