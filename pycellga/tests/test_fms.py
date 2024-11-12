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

    This test checks the calculation of the Fms function value for a given list of float variables.
    It uses a predefined input and compares the output to ensure it's in the correct format.

    Parameters
    ----------
    fms_instance : Fms
        An instance of the Fms class.

    Notes
    -----
    The test generates a sample input chromosome of length 6 within the valid bounds and checks:
    - If the function output is a float.
    - If the fitness value is non-negative, as it represents a sum of squares of differences.

    Assertions
    ----------
    - The fitness value should be a float.
    - The fitness value should be non-negative.
    """
    # Define a sample input chromosome within bounds [-6.4, 6.35] for each variable
    sample_chromosome = np.random.uniform(-6.4, 6.35, size=6)

    # Calculate the FMS function value for the sample input
    fitness_value = fms_instance.f(sample_chromosome)

    # Assertions to check correctness
    assert isinstance(fitness_value, float), "Fitness value should be a float."
    assert fitness_value >= 0, "Fitness value should be non-negative."
    print(f"Sample chromosome: {sample_chromosome}, Fitness: {fitness_value}")

if __name__ == "__main__":
    pytest.main()
