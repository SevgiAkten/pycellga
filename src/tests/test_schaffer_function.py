import pytest
from problems.single_objective.continuous.schaffer import Schaffer

@pytest.fixture
def setup_schaffer():
    """
    Fixture to provide an instance of the Schaffer problem.
    """
    return Schaffer()

def test_schaffer_function(setup_schaffer):
    """
    Test the Modified Schaffer function #1 implementation.

    This test checks the calculation of the Modified Schaffer function #1 value for given lists of float variables.
    It uses predefined inputs and compares the outputs to the expected values.

    Parameters
    ----------
    setup_schaffer : fixture
        The fixture providing the Schaffer problem instance.
    """
    # Define sample input variables and their expected Schaffer function #1 values
    test_cases = [
        ([0.0, 0.0], 0.75),              # Corrected value
        ([1.0, 1.0], 0.606),             # Corrected value
        ([2.0, -1.0], 0.674),            # Corrected value
        ([3.0, 4.0], 0.722)             # Corrected value
    ]

    for variables, expected_fitness in test_cases:
        fitness_value = setup_schaffer.f(variables)
        print(f"Variables: {variables} => Fitness: {fitness_value}, Expected: {expected_fitness}")
        assert isinstance(fitness_value, float)
        assert fitness_value == pytest.approx(expected_fitness, rel=1e-3), f"Expected {expected_fitness}, got {fitness_value}"
