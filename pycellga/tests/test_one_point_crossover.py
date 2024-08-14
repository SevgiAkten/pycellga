from recombination.one_point_crossover import OnePointCrossover
from individual import Individual, GeneType
from problems.single_objective.discrete.binary.one_max import OneMax

def test_one_point_crossover():
    """
    Test the OnePointCrossover class for generating offspring from two parents.

    This test verifies that the OnePointCrossover class correctly performs one-point crossover
    between two parent individuals. It ensures that:
    1. The offspring generated have the same chromosome size as the parents.
    2. The chromosomes of the offspring contain only valid binary values (0 or 1).

    The test performs the following checks:
    - Both offspring have the same chromosome size.
    - Each chromosome in the offspring is composed of binary values (0 or 1).

    Raises
    ------
    AssertionError
        If any of the conditions for the crossover operation are not met.
    """
    CHSIZE = 10

    # Create two parent individuals with binary chromosomes of the specified size
    indv1 = Individual(gen_type=GeneType.BINARY, ch_size=CHSIZE)
    indv2 = Individual(gen_type=GeneType.BINARY, ch_size=CHSIZE)

    # Randomize the chromosomes of the parents
    indv1.randomize()
    indv2.randomize()

    parents = [indv1, indv2]

    # Initialize the OnePointCrossover with the parent individuals and problem
    ucx = OnePointCrossover(parents, OneMax())

    # Perform the crossover to get two offspring
    child1, child2 = ucx.get_recombinations()

    # Check that the chromosome size of both offspring matches the parents
    assert child1.ch_size == child2.ch_size, "Offspring chromosome sizes do not match."
    assert child1.ch_size == CHSIZE, "Offspring chromosome size does not match expected size."

    # Ensure all genes in the offspring are binary (0 or 1)
    for i in range(CHSIZE):
        assert child1.chromosome[i] in [0, 1], "Invalid gene value in child1's chromosome."
        assert child2.chromosome[i] in [0, 1], "Invalid gene value in child2's chromosome."
