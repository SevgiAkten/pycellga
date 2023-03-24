from mutation.bit_flip_mutation import BitFlipMutation
from problems.single_objective.discrete.binary.one_max import OneMax
from individual import Individual


def test_bit_flip_mutation():
    CHSIZE = 20

    ind = Individual("Binary", CHSIZE)
    #  All of the elements of ind are zero.

    problem = OneMax()

    mut = BitFlipMutation(ind, problem)

    newind = mut.mutate()

    elementschanged = 0

    for i in range(CHSIZE):
        if newind.chromosome[i] != ind.chromosome[i]:
            elementschanged += 1

    assert elementschanged > 0

    assert newind.ch_size == CHSIZE
    assert newind.ch_size == ind.ch_size
