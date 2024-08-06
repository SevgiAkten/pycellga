import pytest
from cga.problems.single_objective.discrete.binary.ecc import Ecc

@pytest.fixture
def ecc_instance():
    """
    Fixture for creating an instance of the Ecc class.

    This fixture returns an instance of the Ecc class to be used in tests.
    """
    return Ecc()

def test_ecc(ecc_instance):
    """
    Test the ECC function implementation.

    This test checks the calculation of the ECC function value for a given list of binary variables.
    It uses predefined inputs and compares the outputs to expected values.
    """
    # Define sample input chromosomes (binary lists)
    sample_chromosome1 = [0, 1] * 72  # Example binary sequence
    sample_chromosome2 = [1] * 144  # All ones
    sample_chromosome3 = [0] * 144  # All zeros

    # Calculate the ECC function value for the sample inputs
    fitness_value1 = ecc_instance.f(sample_chromosome1)
    fitness_value2 = ecc_instance.f(sample_chromosome2)
    fitness_value3 = ecc_instance.f(sample_chromosome3)

    # Assertions to check correctness
    assert isinstance(fitness_value1, float)
    assert isinstance(fitness_value2, float)
    assert isinstance(fitness_value3, float)

    assert fitness_value1 > 0
    assert fitness_value2 > 0
    assert fitness_value3 > 0

    # Additional checks with known values
    # Here we assume specific values and their known outputs for more thorough testing
    # You can add more specific test cases if you have known outputs for certain inputs

if __name__ == "__main__":
    pytest.main()
