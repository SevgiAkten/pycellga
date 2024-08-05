import pytest
from cga.problems.single_objective.continuous.holzman import Holzman

@pytest.fixture
def setup_holzman():
    """
    Fixture for creating an instance of the Holzman problem.

    Returns
    -------
    Holzman
        An instance of the Holzman problem.
    """
    return Holzman()

def test_holzman_function(setup_holzman):
    """
    Test the Holzman function implementation.

    This test checks the calculation of the Holzman function value for given lists of float variables.
    It uses predefined inputs and compares the outputs to the expected values.

    Parameters
    ----------
    setup_holzman : fixture
        The fixture providing the Holzman problem instance.
    """
    # Define sample input variables and their expected Holzman function values
    test_cases = [
        ([0.0, 0.0, 0.0], 0.0),  # Global minimum
        ([1.0, 1.0, 1.0], 6.0),  # Points at which i=0 will dominate
        ([1.0, 2.0, 3.0], 276.0),  # Arbitrary point
        ([-1.0, -2.0, -3.0], 276.0),  # Symmetry check
        ([1.5, -2.5, 3.5], 533.375)  # Another arbitrary point
    ]

    for variables, expected_fitness in test_cases:
        fitness_value = setup_holzman.f(variables)
        print(f"Variables: {variables} => Fitness: {fitness_value}")
        assert isinstance(fitness_value, float)
        assert fitness_value == pytest.approx(expected_fitness, rel=1e-3), f"Expected {expected_fitness}, got {fitness_value}"

if __name__ == "__main__":
    pytest.main()
