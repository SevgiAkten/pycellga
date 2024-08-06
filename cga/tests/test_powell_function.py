import pytest
from cga.problems.single_objective.continuous.powell import Powell

@pytest.fixture
def setup_powell():
    """
    Fixture to provide an instance of the Powell problem.
    """
    return Powell()

def test_powell_function(setup_powell):
    """
    Test the Powell function implementation.

    This test checks the calculation of the Powell function value for given lists of float variables.
    It uses predefined inputs and compares the outputs to the expected values.

    Parameters
    ----------
    setup_powell : fixture
        The fixture providing the Powell problem instance.
    """
    # Define sample input variables and their expected Powell function values
    test_cases = [
        ([0.0, 0.0, 0.0, 0.0], 0.0),  # Global minimum
        ([1.0, 2.0, 3.0, 4.0], 1512.0),  # Arbitrary point
        ([1.0, 2.0, 3.0, 4.0, 1.0, 2.0, 3.0, 4.0], 3024.0),  # Extra dimension
        ([5.0, -4.0, 0.0, 0.0, 2.0, -3.0, 4.0, -5.0], 47571.0)  # Another arbitrary point
    ]

    for variables, expected_fitness in test_cases:
        fitness_value = setup_powell.f(variables)
        print(f"Variables: {variables} => Fitness: {fitness_value}, Expected: {expected_fitness}")
        assert isinstance(fitness_value, float)
        assert fitness_value == pytest.approx(expected_fitness, rel=1e-1), f"Expected {expected_fitness}, got {fitness_value}"
