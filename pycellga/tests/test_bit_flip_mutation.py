import numpy as np
import pytest
from mutation.bit_flip_mutation import BitFlipMutation
from problems.single_objective.discrete.binary.one_max import OneMax
from individual import Individual, GeneType

def test_bit_flip_mutation():
    """
    Test the BitFlipMutation class for the Individual class on the OneMax problem.

    This test verifies that the BitFlipMutation correctly mutates the chromosome of
    an Individual by flipping some bits and ensures that the mutation is applied
    correctly. The test checks that:
    1. The chromosome is mutated.
    2. The chromosome size remains unchanged.
    3. The fitness value of the mutated individual is computed correctly.

    The function uses a fixed random seed to ensure reproducibility of the results.

    Notes
    -----
    The test assumes that the BitFlipMutation class correctly implements bit flipping
    mutation and that the OneMax problem correctly evaluates the fitness of an individual.
    
    The following assertions are made:
    - At least one bit in the chromosome is changed.
    - The size of the mutated individual’s chromosome matches the original size.
    - The fitness value of the mutated individual is calculated correctly.

    Raises
    ------
    AssertionError
        If any of the conditions for correctness are not met.

    """
    np.random.seed(0)  # Set seed for reproducibility
    CHSIZE = 20

    # Create an individual with all zeros
    ind = Individual(GeneType.BINARY, CHSIZE)
    ind.chromosome = [0] * CHSIZE
    ind.ch_size = CHSIZE

    # Initialize the OneMax problem
    problem = OneMax()

    # Perform the mutation
    mut = BitFlipMutation(ind, problem)
    newind = mut.mutate()

    # Count how many elements have changed
    elementschanged = sum(1 for i in range(CHSIZE) if newind.chromosome[i] != ind.chromosome[i])

    # Assertions to check correctness
    assert elementschanged > 0, "No bits were flipped during mutation."
    assert newind.ch_size == CHSIZE, "The chromosome size of the mutated individual is incorrect."
    assert newind.ch_size == ind.ch_size, "The chromosome size of the mutated individual does not match the original size."
    assert newind.fitness_value == problem.f(newind.chromosome), "The fitness value of the mutated individual is incorrect."

if __name__ == "__main__":
    pytest.main()
