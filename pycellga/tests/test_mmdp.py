import pytest
from problems.single_objective.discrete.binary.mmdp import Mmdp

@pytest.fixture
def mmdp_instance():
    """
    Fixture for creating an instance of the Mmdp class.

    This fixture returns an instance of the Mmdp class to be used in tests.
    """
    return Mmdp()

def test_mmdp(mmdp_instance):
    """
    Test the Mmdp function implementation.

    This test checks the calculation of the MMDP fitness value for given lists of binary variables.
    It uses predefined inputs and compares the outputs to the expected values.
    """
    # Define sample input chromosomes and their expected fitness values
    test_cases = [
        ([0] * 240, 1.0),  # All zeros: 1.0 for each subproblem, total 40, normalized 40/40=1.0
        ([1] * 240, 1.0),  # All ones: 1.0 for each subproblem, total 40, normalized 40/40=1.0
        ([1, 0] * 120, 0.641),  # Alternating 1s and 0s, normalized as per problem definition
        ([1, 0, 1, 0, 1, 0] * 40, 0.641),  # Alternating pattern within each subproblem
        ([1] * 6 + [0] * 6 + [1] * 6 + [0] * 222, 1.0),  # Mix of all ones and all zeros
        ([0, 1, 1, 1, 1, 1] * 40, 0.0)  # Five ones and one zero in each subproblem
    ]

    for chromosome, expected_fitness in test_cases:
        fitness_value = mmdp_instance.f(chromosome)
        print(f"Chromosome: {chromosome[:12]}... (truncated) => Fitness: {fitness_value}")
        assert isinstance(fitness_value, float)
        assert fitness_value == expected_fitness, f"Expected {expected_fitness}, got {fitness_value}"

if __name__ == "__main__":
    pytest.main()
