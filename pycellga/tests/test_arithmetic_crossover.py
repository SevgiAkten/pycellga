import pytest
import random
from individual import Individual, GeneType
from problems.abstract_problem import AbstractProblem
from recombination.arithmetic_crossover import ArithmeticCrossover 

class MockProblem(AbstractProblem):
    """
    A mock problem class for testing purposes.
    """
    def __init__(self):
        # Set example values for required arguments
        design_variables = 5  # Number of design variables
        bounds = [(0.0, 10.0)] * design_variables  # Bounds for each variable
        objectives = 1  # Number of objectives
        super().__init__(design_variables=design_variables, bounds=bounds, objectives=objectives)

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

def test_arithmetic_crossover(setup_parents, setup_problem):
    """
    Test the ArithmeticCrossover function implementation.

    This test checks the arithmetic crossover on a pair of parent individuals by verifying the recombination
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
    ucx = ArithmeticCrossover(setup_parents, setup_problem)
    child1, child2 = ucx.get_recombinations()

    # Log the chromosomes for debugging
    print("Parent 1 chromosome:", setup_parents[0].chromosome)
    print("Parent 2 chromosome:", setup_parents[1].chromosome)
    print("Child 1 chromosome:", child1.chromosome)
    print("Child 2 chromosome:", child2.chromosome)

    # Assertions to check correctness
    assert isinstance(child1, Individual)
    assert isinstance(child2, Individual)
    assert len(child1.chromosome) == setup_parents[0].ch_size
    assert len(child2.chromosome) == setup_parents[1].ch_size

    # Ensure the offspring chromosomes are valid
    for gene in child1.chromosome:
        assert isinstance(gene, float)

    for gene in child2.chromosome:
        assert isinstance(gene, float)

    # Ensure the offspring chromosomes are different from the parents
    assert child1.chromosome != setup_parents[0].chromosome
    assert child1.chromosome != setup_parents[1].chromosome
    assert child2.chromosome != setup_parents[0].chromosome
    assert child2.chromosome != setup_parents[1].chromosome

if __name__ == "__main__":
    pytest.main()
