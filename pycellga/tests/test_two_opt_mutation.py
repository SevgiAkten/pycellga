from mutation.two_opt_mutation import TwoOptMutation
from problems.single_objective.discrete.permutation.tsp import Tsp
from individual import Individual, GeneType
import random

def test_two_opt_mutation():
    """
    Test the TwoOptMutation class for the Individual class on the TSP problem.

    This test verifies that the TwoOptMutation correctly mutates the chromosome of
    an Individual by applying the 2-opt mutation technique. It ensures that:
    1. The chromosome is mutated by swapping two edges in the permutation.
    2. The chromosome size remains unchanged.

    The function initializes the chromosome with a random permutation of integers
    from 1 to CHSIZE and applies the two-opt mutation.

    Notes
    -----
    The test assumes that the TwoOptMutation class correctly implements the 2-opt mutation
    and that the TSP problem correctly evaluates the fitness of an individual.

    The following assertions are made:
    - At least one element in the chromosome is changed.
    - The size of the mutated individual’s chromosome matches the original size.

    Raises
    ------
    AssertionError
        If any of the conditions for correctness are not met.
    """
    CHSIZE = 14

    # Create an individual with a random permutation of integers from 1 to CHSIZE
    ind = Individual(GeneType.PERMUTATION, CHSIZE)
    ind.chromosome = list(random.sample(range(1, CHSIZE + 1), CHSIZE))

    # Initialize the TSP problem
    problem = Tsp()

    # Perform the mutation
    mut = TwoOptMutation(ind, problem)
    newind = mut.mutate()

    # Count how many elements have changed
    elementschanged = 0
    for i in range(CHSIZE):
        if newind.chromosome[i] != ind.chromosome[i]:
            elementschanged += 1

    # Assertions to check correctness
    assert elementschanged > 0, "No elements were changed during mutation."
    assert newind.ch_size == CHSIZE, "The chromosome size of the mutated individual is incorrect."
    assert newind.ch_size == ind.ch_size, "The chromosome size of the mutated individual does not match the original size."
