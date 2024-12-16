import pytest
from problems.single_objective.continuous.fms import Fms
import numpy as np

@pytest.fixture
def fms_instance():
    """
    Fixture for creating an instance of the Fms class.

    This fixture returns an instance of the Fms class to be used in tests.

    Returns
    -------
    Fms
        An instance of the Fms class.
    """
    return Fms()

def test_fms(fms_instance):
    """
    Test the Fms function implementation.

    This test checks the calculation of the Fms function value for given lists of float variables.
    It uses multiple predefined inputs to validate the function's output.

    Parameters
    ----------
    fms_instance : Fms
        An instance of the Fms class.

    Assertions
    ----------
    - The fitness value should be a float.
    - The fitness value should be non-negative.
    """
    # Define sample input chromosomes and their expected properties
    test_cases = [
        np.array([1.0, 2.0, -1.5, 0.5, 2.5, -0.75]),  # Valid input within bounds
        np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0]),  # All zeros
        np.array([-6.4, 6.35, -6.4, 6.35, -6.4, 6.35]),  # Boundary values
        np.random.uniform(-6.4, 6.35, size=6)  # Random input within bounds
    ]

    for sample_chromosome in test_cases:
        fitness_value = fms_instance.f(sample_chromosome)
        # Assertions
        assert isinstance(fitness_value, float), "Fitness value should be a float."
        assert fitness_value >= 0, "Fitness value should be non-negative."
        print(f"Sample chromosome: {sample_chromosome}, Fitness: {fitness_value}")

if __name__ == "__main__":
    pytest.main()
