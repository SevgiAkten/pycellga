import pytest
from cga.problems.single_objective.continuous.levy import Levy

@pytest.fixture
def setup_levy():
    """
    Fixture to provide an instance of the Levy problem.
    """
    return Levy()

def test_levy_function(setup_levy):
    """
    Test the Levy function implementation.

    This test checks the calculation of the Levy function value for given lists of float variables.
    It uses predefined inputs and compares the outputs to the expected values.

    Parameters
    ----------
    setup_levy : fixture
        The fixture providing the Levy problem instance.
    """
    # Define sample input variables and their expected Levy function values
    test_cases = [
        ([1.0, 1.0], 0.0),  # Global minimum
        ([0.0, 0.0], 2.0),  # Arbitrary point
        ([10.0, -10.0], 202.0),  # Boundary point
        ([-5.0, 5.0], 52.0),  # Another arbitrary point
        ([1.5, 2.5], 3.75)  # Another arbitrary point
    ]

    for variables, expected_fitness in test_cases:
        fitness_value = setup_levy.f(variables)
        print(f"Variables: {variables} => Fitness: {fitness_value}, Expected: {expected_fitness}")
        assert isinstance(fitness_value, float)
        assert fitness_value == pytest.approx(expected_fitness, rel=1e-3), f"Expected {expected_fitness}, got {fitness_value}"

