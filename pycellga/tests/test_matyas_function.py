import pytest
from problems.single_objective.continuous.matyas import Matyas

@pytest.fixture
def setup_matyas():
    """
    Fixture to provide an instance of the Matyas problem.

    Returns
    -------
    Matyas
        An instance of the Matyas optimization problem.
    """
    return Matyas()

def test_matyas_function(setup_matyas):
    """
    Test the Matyas function implementation.

    This test checks the calculation of the Matyas function value for given lists of float variables.
    It uses predefined inputs and compares the outputs to the expected values, verifying the function's accuracy.

    Parameters
    ----------
    setup_matyas : Matyas
        An instance of the Matyas function problem for testing.

    Test Cases
    ----------
    - [0.0, 0.0]: Expected result is 0.0, representing the global minimum.
    - [1.0, 1.0]: Simple case with positive values, expected result is 0.04.
    - [-1.0, -1.0]: Symmetric case with negative values, expected result is 0.04.
    - [5.0, -5.0]: Mixed positive and negative values, expected result is 25.0.
    - [10.0, 10.0]: Boundary point with maximum values, expected result is 4.0.

    Raises
    ------
    AssertionError
        If the actual fitness value does not match the expected fitness value.
    """
    test_cases = [
        ([0.0, 0.0], 0.0),
        ([1.0, 1.0], 0.04),
        ([-1.0, -1.0], 0.04),
        ([5.0, -5.0], 25.0),
        ([10.0, 10.0], 4.0)
    ]

    for variables, expected_fitness in test_cases:
        fitness_value = setup_matyas.f(variables)
        print(f"Variables: {variables} => Fitness: {fitness_value}, Expected: {expected_fitness}")
        assert isinstance(fitness_value, float)
        assert fitness_value == pytest.approx(expected_fitness, rel=1e-2), f"Expected {expected_fitness}, got {fitness_value}"

if __name__ == "__main__":
    pytest.main()
