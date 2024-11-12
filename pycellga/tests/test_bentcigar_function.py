import pytest
from problems.single_objective.continuous.bentcigar import Bentcigar

@pytest.fixture
def setup_bentcigar():
    """
    Fixture for creating an instance of the Bentcigar problem with a specified dimension.

    Returns
    -------
    Bentcigar
        An instance of the Bentcigar problem.
    """
    dimension = 10 
    return Bentcigar(dimension=dimension)

def test_bentcigar_function(setup_bentcigar):
    """
    Test the Bentcigar function implementation.

    This test checks the calculation of the Bentcigar function value for given lists of float variables.
    It uses predefined inputs and compares the outputs to the expected values.

    Parameters
    ----------
    setup_bentcigar : fixture
        The fixture providing the Bentcigar problem instance.
    """
    # Define sample input variables and their expected Bentcigar function values
    test_cases = [
        ([0.0] * 10, 0.0),  # All zeros
        ([1.0] + [0.0] * 9, 1.0),  # One non-zero value at the first position
        ([0.0] + [1.0] * 9, 9000000.0),  # Non-zero values from the second position
        ([0.5] * 10, 0.25 + 9 * 1000000.0 * 0.25),  # All 0.5 values
        ([-1.0] * 10, 1.0 + 9 * 1000000.0 * 1.0)  # All -1.0 values
    ]

    for variables, expected_fitness in test_cases:
        fitness_value = setup_bentcigar.f(variables)
        print(f"Variables: {variables[:5]}... (truncated) => Fitness: {fitness_value}")
        assert isinstance(fitness_value, float)
        assert fitness_value == pytest.approx(expected_fitness, rel=1e-3), f"Expected {expected_fitness}, got {fitness_value}"

if __name__ == "__main__":
    pytest.main()
