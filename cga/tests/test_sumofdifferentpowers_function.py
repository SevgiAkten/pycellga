import pytest
from cga.problems.single_objective.continuous.sumofdifferentpowers import Sumofdifferentpowers  

@pytest.fixture
def setup_sumofdifferentpowers():
    """
    Fixture to create an instance of the Sumofdifferentpowers problem.
    """
    return Sumofdifferentpowers()

def test_sumofdifferentpowers_function(setup_sumofdifferentpowers):
    """
    Test the Sum of Different Powers function implementation.
    
    This test checks the calculation of the Sum of Different Powers function value
    for given lists of float variables. It uses predefined inputs and compares
    the outputs to the expected values.
    
    Parameters
    ----------
    setup_sumofdifferentpowers : fixture
        The fixture providing the Sumofdifferentpowers problem instance.
    """
    # Define sample input variables and their expected function values
    test_cases = [
        ([0.0, 0.0], 0.0),                # Global minimum
        ([1.0, 1.0], 2.0),                # Simple test case
        ([1.0, 2.0, 3.0], 32.0),           # Test case with three variables
        ([2.0, -1.0, 0.0], 3.0)           # Test case with positive and negative values
    ]
    
    for variables, expected_fitness in test_cases:
        fitness_value = setup_sumofdifferentpowers.f(variables)
        print(f"Variables: {variables} => Fitness: {fitness_value}, Expected: {expected_fitness}")
        assert isinstance(fitness_value, float)
        assert fitness_value == pytest.approx(expected_fitness, rel=1e-3), f"Expected {expected_fitness}, got {fitness_value}"
