import pytest
import random
from individual import Individual, GeneType
from problems.abstract_problem import AbstractProblem
from mutation.float_uniform_mutation import FloatUniformMutation 

class MockProblem(AbstractProblem):
    """
    A mock problem class for testing purposes.
    """
    def __init__(self):
        # Define design variables, bounds, and objectives according to the test requirements
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
def setup_individual():
    """
    Fixture for creating a sample Individual instance.

    Returns
    -------
    Individual
        An individual instance with a predefined chromosome and size.
    """
    ind = Individual(GeneType.REAL, 5)
    ind.chromosome = [1.0, 2.0, 3.0, 4.0, 5.0]
    ind.ch_size = 5
    return ind

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

def test_float_uniform_mutation(setup_individual, setup_problem):
    """
    Test the FloatUniformMutation function implementation.

    This test checks the uniform mutation on an individual's chromosome by verifying the mutation
    operation and the integrity of the chromosome.

    Parameters
    ----------
    setup_individual : fixture
        The fixture providing the sample individual.
    setup_problem : fixture
        The fixture providing the mock problem instance.
    """
    # Set seed for reproducibility
    random.seed(0)

    # Perform the mutation
    mut = FloatUniformMutation(setup_individual, setup_problem)
    new_individual = mut.mutate()

    # Log the chromosomes for debugging
    print("Original chromosome:", setup_individual.chromosome)
    print("Mutated chromosome:", new_individual.chromosome)

    # Assertions to check correctness
    assert isinstance(new_individual, Individual), "Mutated individual is not an Individual instance"
    assert len(new_individual.chromosome) == setup_individual.ch_size, "Chromosome length mismatch"
    assert new_individual.chromosome != setup_individual.chromosome, "Mutation did not occur"

    # Additional checks to verify the mutation logic
    original_ch = setup_individual.chromosome
    mutated_ch = new_individual.chromosome

    # Ensure each gene has been mutated within the range [-1, +1] relative to original value
    for orig, mut in zip(original_ch, mutated_ch):
        assert abs(mut - orig) <= 1.0, f"Gene mutated outside of expected range: {mut} vs {orig}"

    # Check that each mutated gene is a float
    for gene in mutated_ch:
        assert isinstance(gene, float), f"Gene {gene} is not a float"

if __name__ == "__main__":
    pytest.main()
