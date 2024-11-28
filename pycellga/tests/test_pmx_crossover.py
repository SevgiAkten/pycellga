from problems.single_objective.discrete.permutation.tsp import Tsp
from recombination.pmx_crossover import PMXCrossover
from individual import Individual, GeneType
import random

def test_pmx_crossover():
    """
    Test the PMXCrossover class for generating offspring from two permutation parents.

    This test verifies that the PMXCrossover class correctly performs partially matched crossover
    (PMX) between two parent individuals. It ensures that:
    1. The offspring generated have the same chromosome size as the parents.

    The test performs the following checks:
    - Both offspring have the same chromosome size as the parents.

    Raises
    ------
    AssertionError
        If any of the conditions for the crossover operation are not met.
    """
    CHSIZE = 14

    # Create two parent individuals with permutation chromosomes of the specified size
    indv1 = Individual(gen_type=GeneType.PERMUTATION, ch_size=CHSIZE)
    indv2 = Individual(gen_type=GeneType.PERMUTATION, ch_size=CHSIZE)

    # Randomly initialize the chromosomes of the parents with unique permutations
    p1 = list(random.sample(range(1, CHSIZE + 1), CHSIZE))
    p2 = list(random.sample(range(1, CHSIZE + 1), CHSIZE))

    indv1.chromosome = p1
    indv2.chromosome = p2
    parents = [indv1, indv2]

    # Initialize the PMXCrossover with the parent individuals and problem
    theproblem = Tsp()
    ucx = PMXCrossover(parents, theproblem)

    # Perform the crossover to get two offspring
    child1, child2 = ucx.get_recombinations()

    # Check that the chromosome size of both offspring matches the parents
    assert child1.ch_size == child2.ch_size, "Offspring chromosome sizes do not match."
    assert child1.ch_size == CHSIZE, "Offspring chromosome size does not match expected size."
