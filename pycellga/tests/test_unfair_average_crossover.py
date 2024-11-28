import pytest
import random
from individual import Individual, GeneType
from problems.abstract_problem import AbstractProblem
from recombination.unfair_avarage_crossover import UnfairAvarageCrossover

class MockProblem(AbstractProblem):
    """
    A mock problem class for testing purposes.
    """
    def __init__(self):
        super().__init__(design_variables=5, bounds=[(0, 10)] * 5, objectives=1)

    def f(self, x: list) -> float:
        """
        A mock fitness function that simply sums the chromosome values.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The sum of the list values.
        """
        return sum(x)

@pytest.fixture
def setup_parents():
    """
    Fixture for creating a pair of parent Individual instances.

    Returns
    -------
    list
        A list containing two parent individuals with predefined chromosomes and size.
    """
    ind1 = Individual(GeneType.REAL, 5)
    ind2 = Individual(GeneType.REAL, 5)
    ind1.chromosome = [1.0, 2.0, 3.0, 4.0, 5.0]
    ind2.chromosome = [5.0, 4.0, 3.0, 2.0, 1.0]
    ind1.ch_size = 5
    ind2.ch_size = 5
    return [ind1, ind2]

@pytest.fixture
def setup_problem():
    """
    Fixture for creating a mock problem instance.

    Returns
    -------
    MockProblem
        An instance of the mock problem.
    """
    return MockProblem()

def test_unfair_average_crossover(setup_parents, setup_problem):
    """
    Test the UnfairAvarageCrossover function implementation.

    This test checks the unfair average crossover on a pair of parent individuals by verifying the recombination
    operation and the integrity of the offspring chromosomes.

    Parameters
    ----------
    setup_parents : fixture
        The fixture providing the parent individuals.
    setup_problem : fixture
        The fixture providing the mock problem instance.
    """
    # Set seed for reproducibility
    random.seed(0)

    # Perform the crossover
    crossover = UnfairAvarageCrossover(setup_parents, setup_problem)
    offsprings = crossover.get_recombinations()
    child1, child2 = offsprings[0], offsprings[1]

    # Log the chromosomes for debugging
    print("Parent 1 chromosome:", setup_parents[0].chromosome)
    print("Parent 2 chromosome:", setup_parents[1].chromosome)
    print("Child 1 chromosome:", child1.chromosome)
    print("Child 2 chromosome:", child2.chromosome)

    # Assertions to check correctness
    assert isinstance(child1, Individual), "Child 1 is not an Individual instance."
    assert isinstance(child2, Individual), "Child 2 is not an Individual instance."
    assert len(child1.chromosome) == setup_parents[0].ch_size, "Child 1 chromosome length mismatch."
    assert len(child2.chromosome) == setup_parents[1].ch_size, "Child 2 chromosome length mismatch."

    # Ensure the offspring chromosomes are valid floats
    for gene in child1.chromosome:
        assert isinstance(gene, float), "Child 1 chromosome gene is not a float."

    for gene in child2.chromosome:
        assert isinstance(gene, float), "Child 2 chromosome gene is not a float."

    # Ensure the offspring chromosomes are different from the parents
    assert child1.chromosome != setup_parents[0].chromosome, "Child 1 chromosome matches Parent 1."
    assert child1.chromosome != setup_parents[1].chromosome, "Child 1 chromosome matches Parent 2."
    assert child2.chromosome != setup_parents[0].chromosome, "Child 2 chromosome matches Parent 1."
    assert child2.chromosome != setup_parents[1].chromosome, "Child 2 chromosome matches Parent 2."

    # Ensure the offspring chromosomes are different from each other
    assert child1.chromosome != child2.chromosome, "Child 1 and Child 2 should not have the same chromosome."

if __name__ == "__main__":
    pytest.main()
