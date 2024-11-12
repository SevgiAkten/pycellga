import pytest
from problems.single_objective.continuous.schaffer2 import Schaffer2

@pytest.fixture
def setup_schaffer2():
    """
    Fixture to provide an instance of the Schaffer2 problem.
    """
    return Schaffer2(design_variables=2)

def test_schaffer2_function(setup_schaffer2):
    """
    Test the Modified Schaffer function #2 implementation.

    This test checks the calculation of the Modified Schaffer function #2 value
    for given lists of float variables. It uses predefined inputs and compares
    the outputs to the expected values.

    Parameters
    ----------
    setup_schaffer2 : fixture
        The fixture providing the Schaffer2 problem instance.
    """
    # Define sample input variables and their expected Schaffer function #2 values
    test_cases = [
        ([0.0, 0.0], 0.0),                # Global minimum
        ([1.0, 1.0], 0.002),              # Arbitrary point
        ([2.0, -1.0], 0.025),             # Another arbitrary point 
        ([3.0, 4.0], 0.435)               # Another arbitrary point 
    ]

    for variables, expected_fitness in test_cases:
        fitness_value = setup_schaffer2.f(variables)
        print(f"Variables: {variables} => Fitness: {fitness_value}, Expected: {expected_fitness}")
        assert isinstance(fitness_value, float)
        assert fitness_value == pytest.approx(expected_fitness, rel=1e-3), f"Expected {expected_fitness}, got {fitness_value}"
