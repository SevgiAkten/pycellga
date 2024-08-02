import numpy as np
import pytest
from cga.mutation.bit_flip_mutation import BitFlipMutation
from cga.problems.single_objective.discrete.binary.one_max import OneMax
from cga.individual import Individual

def test_bit_flip_mutation():
    np.random.seed(0)  # Set seed for reproducibility
    CHSIZE = 20

    # Create an individual with all zeros
    ind = Individual("Binary", CHSIZE)
    ind.chromosome = [0] * CHSIZE
    ind.ch_size = CHSIZE

    # Initialize the OneMax problem
    problem = OneMax()

    # Perform the mutation
    mut = BitFlipMutation(ind, problem)
    newind = mut.mutate()

    # Check how many elements have changed
    elementschanged = sum(1 for i in range(CHSIZE) if newind.chromosome[i] != ind.chromosome[i])

    # Assertions to check correctness
    assert elementschanged > 0
    assert newind.ch_size == CHSIZE
    assert newind.ch_size == ind.ch_size
    assert newind.fitness_value == problem.f(newind.chromosome)

if __name__ == "__main__":
    pytest.main()
