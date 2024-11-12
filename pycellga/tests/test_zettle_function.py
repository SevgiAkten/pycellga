import pytest
from problems.single_objective.continuous.zettle import Zettle

@pytest.fixture
def setup_zettle():
    """
    Fixture to provide an instance of the Zettle problem.
    """
    return Zettle()

def test_zettle_function(setup_zettle):
    """
    Test the Zettle function implementation.

    This test checks the calculation of the Zettle function value for given lists of float variables.
    It uses predefined inputs and compares the outputs to the expected values.

    Parameters
    ----------
    setup_zettle : fixture
        The fixture providing the Zettle problem instance.
    """
    # Define sample input variables and their expected Zettle function values
    test_cases = [
        ([0.0, 0.0], 0.0),                # Global minimum
        ([1.0, 1.0], 0.25),               # Arbitrary point
        ([2.0, -1.0], 1.5),               # Corrected expected value
        ([3.0, -2.0], 49.75)              # Another arbitrary point
    ]

    for variables, expected_fitness in test_cases:
        fitness_value = setup_zettle.f(variables)
        print(f"Variables: {variables} => Fitness: {fitness_value}, Expected: {expected_fitness}")
        assert isinstance(fitness_value, float)
        assert fitness_value == pytest.approx(expected_fitness, rel=1e-6), f"Expected {expected_fitness}, got {fitness_value}"
