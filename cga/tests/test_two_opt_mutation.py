from cga.mutation.two_opt_mutation import TwoOptMutation
from cga.problems.single_objective.discrete.permutation.tsp import Tsp
from cga.individual import Individual
import random


def test_two_opt_mutation():
    CHSIZE = 14

    ind = Individual("Permutation", CHSIZE)
    ind.chromosome = list(random.sample(range(1, 15), 14))

    problem = Tsp()

    mut = TwoOptMutation(ind, problem)

    newind = mut.mutate()

    elementschanged = 0

    for i in range(CHSIZE):
        if newind.chromosome[i] != ind.chromosome[i]:
            elementschanged += 1

    assert elementschanged > 0

    assert newind.ch_size == CHSIZE
    assert newind.ch_size == ind.ch_size
