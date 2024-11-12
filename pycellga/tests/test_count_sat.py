import pytest
from problems.single_objective.discrete.binary.count_sat import CountSat

@pytest.fixture
def setup_count_sat():
    """
    Fixture to provide an instance of the CountSat problem.
    """
    return CountSat()

def test_count_sat(setup_count_sat):
    """
    Test the CountSat function implementation.

    This test verifies the calculation of the CountSat function value for specific binary input values.

    The CountSat function evaluates the satisfaction of a set of binary clauses. This test ensures the 
    function computes the correct results for specific test inputs, including cases where all variables 
    are set to 1 and other configurations.

    Parameters
    ----------
    setup_count_sat : fixture
        The fixture providing the CountSat problem instance.
    """
    # Define test cases and expected values
    test_cases = [
        ([1] * 20, 1.0),  # All variables set to 1, expected to be fully satisfied
        ([1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0], 0.9),  # Arbitrary binary input
        ([0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0], 0.95),  # Another arbitrary input
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0.87)  # Mixed 1s and 0s
    ]

    for variables, expected_fitness in test_cases:
        fitness_value = setup_count_sat.f(variables)
        print(f"Variables: {variables} => Fitness: {fitness_value}, Expected: {expected_fitness}")
        assert isinstance(fitness_value, float)
        assert fitness_value == pytest.approx(expected_fitness, rel=1e-2), f"Expected {expected_fitness}, got {fitness_value}"
