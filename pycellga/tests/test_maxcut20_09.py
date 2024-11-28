import pytest
from problems.single_objective.discrete.binary.maxcut20_09 import Maxcut20_09
import numpy as np

@pytest.fixture
def maxcut_instance():
    """Fixture for creating an instance of the Maxcut20_09 class."""
    return Maxcut20_09()

def test_maxcut20_09(maxcut_instance):
    """
    Test the MAXCUT function implementation.
    """
    # Define sample input chromosomes (binary lists)
    sample_chromosome1 = [0, 1] * 10
    sample_chromosome2 = [1] * 20
    sample_chromosome3 = [0] * 20

    # Calculate the MAXCUT function value for the sample inputs
    fitness_value1 = maxcut_instance.f(sample_chromosome1)
    fitness_value2 = maxcut_instance.f(sample_chromosome2)
    fitness_value3 = maxcut_instance.f(sample_chromosome3)

    # Assertions to check correctness
    assert isinstance(fitness_value1, float)
    assert isinstance(fitness_value2, float)
    assert isinstance(fitness_value3, float)
    assert fitness_value1 > 0, f"Expected positive fitness, got {fitness_value1}"
    assert fitness_value2 == 0, f"Expected fitness of 0, got {fitness_value2}"
    assert fitness_value3 == 0, f"Expected fitness of 0, got {fitness_value3}"

def test_maxcut20_09_evaluate(maxcut_instance):
    """
    Test the evaluate function for compatibility with pymoo.
    """
    # Define sample input as numpy array (for pymoo compatibility)
    sample_input = np.array([[0, 1] * 10])

    # Dictionary to store the output of evaluate function
    out = {}

    # Evaluate the function using pymoo-compatible evaluate method
    maxcut_instance.evaluate(sample_input[0], out)

    # Assertions to check that output is as expected
    assert "F" in out, "Expected 'F' in output dictionary"
    assert isinstance(out["F"], float), f"Expected a float, got {type(out['F'])}"
    assert out["F"] > 0, f"Expected positive fitness value, got {out['F']}"
