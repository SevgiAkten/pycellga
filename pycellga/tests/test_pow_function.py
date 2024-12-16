import pytest
from problems.single_objective.continuous.pow import Pow

@pytest.fixture
def setup_pow():
    """
    Fixture to provide an instance of the Pow problem.

    Returns
    -------
    Pow
        An instance of the Pow optimization problem.
    """
    return Pow(n_var=5)

def test_pow_function(setup_pow):
    """
    Test the Pow function implementation.

    This test checks the calculation of the Pow function value for given lists of float variables.
    It uses predefined inputs and compares the outputs to the expected values.

    Parameters
    ----------
    setup_pow : Pow
        An instance of the Pow function problem for testing.

    Test Cases
    ----------
    - [5.0, 7.0, 9.0, 3.0, 2.0]: Expected result is 0.0, representing the global minimum.
    - [0.0, 0.0, 0.0, 0.0, 0.0]: All variables set to zero, expected result is 168.0.
    - [10.0, 10.0, 10.0, 10.0, 10.0]: All variables set to upper bounds, expected result is 148.0.
    - [-5.0, -5.0, -5.0, -5.0, -5.0]: All variables set to lower bounds, expected result is 553.0.
    - [6.0, 8.0, 10.0, 4.0, 3.0]: Near the global minimum, expected result is 5.0.
    """
    test_cases = [
        ([5.0, 7.0, 9.0, 3.0, 2.0], 0.0),         # Global minimum
        ([0.0, 0.0, 0.0, 0.0, 0.0], 168.0),       # All zeros
        ([10.0, 10.0, 10.0, 10.0, 10.0], 148.0),  # Point near boundaries
        ([-5.0, -5.0, -5.0, -5.0, -5.0], 553.0),  # Negative boundary
        ([6.0, 8.0, 10.0, 4.0, 3.0], 5.0)         # Near global minimum
    ]

    for variables, expected_fitness in test_cases:
        fitness_value = setup_pow.f(variables)
        print(f"Variables: {variables} => Fitness: {fitness_value}, Expected: {expected_fitness}")
        assert isinstance(fitness_value, float), "Fitness value should be a float."
        assert fitness_value == pytest.approx(expected_fitness, rel=1e-2), f"Expected {expected_fitness}, got {fitness_value}"

if __name__ == "__main__":
    pytest.main()
