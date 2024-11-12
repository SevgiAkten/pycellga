import pytest
from problems.single_objective.discrete.binary.maxcut20_01 import Maxcut20_01

@pytest.fixture
def maxcut_instance():
    """
    Fixture for creating an instance of the Maxcut20_01 class.

    This fixture returns an instance of the Maxcut20_01 class to be used in tests.
    """
    return Maxcut20_01()

def test_maxcut20_01(maxcut_instance):
    """
    Test the MAXCUT function implementation.

    This test checks the calculation of the MAXCUT function value for a given list of binary variables.
    It uses predefined inputs and compares the outputs to expected values.
    """
    # Define sample input chromosomes (binary lists)
    sample_chromosome1 = [0, 1] * 10  # Alternating binary sequence
    sample_chromosome2 = [1] * 20  # All ones (no cut)
    sample_chromosome3 = [0] * 20  # All zeros (no cut)

    # Calculate the MAXCUT function value for the sample inputs
    fitness_value1 = maxcut_instance.f(sample_chromosome1)
    fitness_value2 = maxcut_instance.f(sample_chromosome2)
    fitness_value3 = maxcut_instance.f(sample_chromosome3)

    # Assertions to check correctness
    assert isinstance(fitness_value1, float)
    assert isinstance(fitness_value2, float)
    assert isinstance(fitness_value3, float)

    # Specific assertions based on expected behavior
    assert fitness_value1 > 0, f"Expected positive fitness, got {fitness_value1}"
    assert fitness_value2 == 0, f"Expected zero fitness for all-ones, got {fitness_value2}"
    assert fitness_value3 == 0, f"Expected zero fitness for all-zeros, got {fitness_value3}"

    print(f"Test results:\n"
          f"Sample Chromosome 1 (Alternating): Fitness = {fitness_value1}\n"
          f"Sample Chromosome 2 (All Ones): Fitness = {fitness_value2}\n"
          f"Sample Chromosome 3 (All Zeros): Fitness = {fitness_value3}")

if __name__ == "__main__":
    pytest.main()
