import pytest
from cga.problems.single_objective.continuous.rothellipsoid import Rothellipsoid

@pytest.fixture
def setup_rothellipsoid():
    """
    Fixture to provide an instance of the Rotated Hyper-Ellipsoid problem.
    """
    return Rothellipsoid()

def test_rothellipsoid_function(setup_rothellipsoid):
    """
    Test the Rotated Hyper-Ellipsoid function implementation.

    This test checks the calculation of the Rotated Hyper-Ellipsoid function value for given lists of float variables.
    It uses predefined inputs and compares the outputs to the expected values.

    Parameters
    ----------
    setup_rothellipsoid : fixture
        The fixture providing the Rotated Hyper-Ellipsoid problem instance.
    """
    # Define sample input variables and their expected Rotated Hyper-Ellipsoid function values
    test_cases = [
        ([0.0, 0.0, 0.0], 0.0),       # Global minimum
        ([1.0, 1.0, 1.0], 9.0),       # Arbitrary point
        ([2.0, 2.0, 2.0], 36.0),      # Another arbitrary point
        ([5.0, -5.0, 0.0], 125.0)     # Another arbitrary point
    ]

    for variables, expected_fitness in test_cases:
        fitness_value = setup_rothellipsoid.f(variables)
        print(f"Variables: {variables} => Fitness: {fitness_value}, Expected: {expected_fitness}")
        assert isinstance(fitness_value, float)
        assert fitness_value == pytest.approx(expected_fitness, rel=1e-3), f"Expected {expected_fitness}, got {fitness_value}"
