from mutation.insertion_mutation import InsertionMutation
from problems.single_objective.discrete.permutation.tsp import Tsp
from individual import Individual
import random


def test_insertion_mutation():
    CHSIZE = 52

    ind = Individual("Permutation", CHSIZE)
    ind.chromosome = list(random.sample(range(1, 53), 52))

    problem = Tsp()

    mut = InsertionMutation(ind, problem)

    newind = mut.mutate()

    elementschanged = 0

    for i in range(CHSIZE):
        if newind.chromosome[i] != ind.chromosome[i]:
            elementschanged += 1

    assert elementschanged > 0

    assert newind.ch_size == CHSIZE
    assert newind.ch_size == ind.ch_size
