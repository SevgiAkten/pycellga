import pytest
from cga.problems.single_objective.continuous.matyas import Matyas

@pytest.fixture
def setup_matyas():
    """
    Fixture to provide an instance of the Matyas problem.
    """
    return Matyas()

def test_matyas_function(setup_matyas):
    """
    Test the Matyas function implementation.

    This test checks the calculation of the Matyas function value for given lists of float variables.
    It uses predefined inputs and compares the outputs to the expected values.

    Parameters
    ----------
    setup_matyas : fixture
        The fixture providing the Matyas problem instance.
    """
    # Define sample input variables and their expected Matyas function values
    test_cases = [
        ([0.0, 0.0], 0.0),  # Global minimum
        ([1.0, 1.0], 0.04),  # Simple case
        ([-1.0, -1.0], 0.04),  # Symmetric case
        ([5.0, -5.0], 25.0),  # Another arbitrary point
        ([10.0, 10.0], 4.0)  # Boundary point
    ]

    for variables, expected_fitness in test_cases:
        fitness_value = setup_matyas.f(variables)
        print(f"Variables: {variables} => Fitness: {fitness_value}, Expected: {expected_fitness}")
        assert isinstance(fitness_value, float)
        assert fitness_value == pytest.approx(expected_fitness, rel=1e-2), f"Expected {expected_fitness}, got {fitness_value}"
