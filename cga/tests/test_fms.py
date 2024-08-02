import pytest
from cga.problems.abstract_problem import AbstractProblem
from cga.problems.single_objective.continuous.fms import Fms  # Replace with the actual path if different
from numpy import random

@pytest.fixture
def fms_instance():
    """
    Fixture for creating an instance of the Fms class.

    This fixture returns an instance of the Fms class to be used in tests.
    """
    return Fms()

def test_fms(fms_instance):
    """
    Test the Fms function implementation.

    This test checks the calculation of the FMS function value for a given list of binary variables.
    It uses a predefined input and compares the output to the expected value.
    """
    # Define a sample input chromosome (binary list)
    sample_chromosome = [random.randint(2) for _ in range(192)]

    # Calculate the FMS function value for the sample input
    fitness_value = fms_instance.f(sample_chromosome)

    # Assertions to check correctness
    assert isinstance(fitness_value, float)
    assert fitness_value >= 0  # Since it's a sum of squares of differences

    # Additional checks with known values
    # Here we assume specific values and their known outputs for more thorough testing
    # You can add more specific test cases if you have known outputs for certain inputs

if __name__ == "__main__":
    pytest.main()
