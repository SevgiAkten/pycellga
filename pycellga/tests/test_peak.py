import pytest
from numpy import random
from problems.single_objective.discrete.binary.peak import Peak

@pytest.fixture
def peak_instance():
    """
    Fixture for creating an instance of the Peak class.

    This fixture returns an instance of the Peak class to be used in tests.
    """
    return Peak()

def test_peak(peak_instance):
    """
    Test the Peak function implementation.

    This test checks the calculation of the Peak fitness value for given lists of binary variables.
    It uses predefined inputs and compares the outputs to the expected values.
    """
    # Seed the random number generator for reproducibility in tests
    random.seed(100)

    # Define sample input chromosomes
    test_cases = [
        [0] * 100,  # All zeros
        [1] * 100,  # All ones
        [random.randint(2) for _ in range(100)],  # Random chromosome
        [0, 1] * 50,  # Alternating 0s and 1s
        [1, 0] * 50,  # Alternating 1s and 0s
    ]

    # Calculate expected fitness values based on the Peak function's logic
    expected_fitness_values = [peak_instance.f(chromosome) for chromosome in test_cases]

    # Reset the random seed to ensure the fitness function behaves deterministically
    random.seed(100)

    # Run the tests
    for chromosome, expected_fitness in zip(test_cases, expected_fitness_values):
        fitness_value = peak_instance.f(chromosome)
        print(f"Chromosome: {chromosome[:12]}... (truncated) => Fitness: {fitness_value}")
        assert isinstance(fitness_value, float)
        assert fitness_value == expected_fitness, f"Expected {expected_fitness}, got {fitness_value}"

if __name__ == "__main__":
    pytest.main()
