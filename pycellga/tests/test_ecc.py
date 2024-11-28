import pytest
from problems.single_objective.discrete.binary.ecc import Ecc

@pytest.fixture
def ecc_instance():
    """
    Fixture to create an instance of the Ecc class.
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
    sample_chromosome2 = [1] * 144    # All ones
    sample_chromosome3 = [0] * 144    # All zeros

    # Calculate the ECC function value for the sample inputs
    fitness_value1 = ecc_instance.f(sample_chromosome1)
    fitness_value2 = ecc_instance.f(sample_chromosome2)
    fitness_value3 = ecc_instance.f(sample_chromosome3)

    # Assertions to check correctness
    assert isinstance(fitness_value1, float)
    assert isinstance(fitness_value2, float)
    assert isinstance(fitness_value3, float)

    # Verify that fitness values are within expected range and types
    assert fitness_value1 >= 0.0
    assert fitness_value2 >= 0.0
    assert fitness_value3 == 0.0  # Expect 0 for all-zero chromosome as there's no Hamming distance

    print(f"Fitness values: {fitness_value1}, {fitness_value2}, {fitness_value3}")

if __name__ == "__main__":
    pytest.main()
