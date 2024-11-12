import pytest
from problems.single_objective.continuous.pow import Pow

@pytest.fixture
def setup_pow():
    """
    Fixture to provide an instance of the Pow problem.
    """
    return Pow()

def test_pow_function(setup_pow):
    """
    Test the Pow function implementation.

    This test checks the calculation of the Pow function value for given lists of float variables.
    It uses predefined inputs and compares the outputs to the expected values.

    Parameters
    ----------
    setup_pow : fixture
        The fixture providing the Pow problem instance.
    """
    # Define sample input variables and their expected Pow function values
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
        assert isinstance(fitness_value, float)
        assert fitness_value == pytest.approx(expected_fitness, rel=1e-2), f"Expected {expected_fitness}, got {fitness_value}"

if __name__ == "__main__":
    pytest.main()
