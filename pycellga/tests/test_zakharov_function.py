import pytest
from problems.single_objective.continuous.zakharov import Zakharov


def test_zakharov_function():
    """
    Test the Zakharov function implementation.

    This test checks the calculation of the Zakharov function value
    for given lists of float variables. It uses predefined inputs and compares
    the outputs to the expected values.
    """
    # Define sample input variables and their expected Zakharov function values
    test_cases = [
        ([0.0, 0.0], 0.0),                  # Global minimum
        ([1.0, 1.0], 9.312),                  # Arbitrary point
        ([2.0, -1.0], 5.0),                # Another arbitrary point
        ([1.0, 2.0, 3.0], 2464.0)            # Another arbitrary point
    ]

    # Create an instance of the Zakharov class
    problem = Zakharov()

    for variables, expected_fitness in test_cases:
        fitness_value = problem.f(variables)
        print(f"Variables: {variables} => Fitness: {fitness_value}, Expected: {expected_fitness}")
        assert isinstance(fitness_value, float)
        assert fitness_value == pytest.approx(expected_fitness, rel=1e-3), f"Expected {expected_fitness}, got {fitness_value}"

