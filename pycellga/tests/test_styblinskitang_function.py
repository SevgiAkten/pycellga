import pytest
from problems.single_objective.continuous.styblinskitang import StyblinskiTang

@pytest.fixture
def setup_styblinski_tang():
    """
    Fixture to provide an instance of the StyblinskiTang problem.
    """
    return StyblinskiTang(design_variables=2)

def test_styblinskitang_function(setup_styblinski_tang):
    """
    Test the Styblinski-Tang function implementation.

    This test checks the calculation of the Styblinski-Tang function value
    for given lists of float variables. It uses predefined inputs and compares
    the outputs to the expected values.

    Parameters
    ----------
    setup_styblinski_tang : fixture
        The fixture providing the StyblinskiTang problem instance.
    """
    # Define sample input variables and their expected Styblinski-Tang function values
    test_cases = [
        ([-2.903534, -2.903534], -78.332),  # Global minimum
        ([0.0, 0.0], 0.0),                 # Simple case
        ([1.0, 1.0], -10.0),               # Arbitrary point
        ([2.0, -1.0], -29.0)               # Another arbitrary point
    ]

    for variables, expected_fitness in test_cases:
        fitness_value = setup_styblinski_tang.f(variables)
        print(f"Variables: {variables} => Fitness: {fitness_value}, Expected: {expected_fitness}")
        assert isinstance(fitness_value, float)
        assert fitness_value == pytest.approx(expected_fitness, rel=1e-3), f"Expected {expected_fitness}, got {fitness_value}"
