import pytest
from problems.single_objective.continuous.threehumps import Threehumps

@pytest.fixture
def setup_threehumps():
    """Fixture to provide the Threehumps problem instance."""
    return Threehumps()

def test_threehumps_function(setup_threehumps):
    """
    Test the Three Hump Camel function implementation.

    This test checks the calculation of the Three Hump Camel function value
    for given lists of float variables. It uses predefined inputs and compares
    the outputs to the expected values.

    Parameters
    ----------
    setup_threehumps : fixture
        The fixture providing the Threehumps problem instance.
    """
    # Define sample input variables and their expected Three Hump Camel function values
    test_cases = [
        ([0.0, 0.0], 0.0),                  # Global minimum
        ([1.0, 1.0], 3.116667),             # Arbitrary point
        ([2.0, -1.0], 0.866667),                 # Another arbitrary point
        ([3.0, -2.0], 52.45)            # Another arbitrary point
    ]

    for variables, expected_fitness in test_cases:
        fitness_value = setup_threehumps.f(variables)
        print(f"Variables: {variables} => Fitness: {fitness_value}, Expected: {expected_fitness}")
        assert isinstance(fitness_value, float)
        assert fitness_value == pytest.approx(expected_fitness, rel=1e-6), f"Expected {expected_fitness}, got {fitness_value}"
