import pytest
from problems.single_objective.continuous.rosenbrock import Rosenbrock

@pytest.fixture
def setup_rosenbrock():
    """
    Fixture to provide an instance of the Rosenbrock problem.
    """
    return Rosenbrock(n_var=4)  # Ensure compatibility with the new AbstractProblem structure

def test_rosenbrock(setup_rosenbrock):
    """
    Test the Rosenbrock function implementation.

    This test verifies the calculation of the Rosenbrock function value for given lists of continuous variables.
    It compares the function output with known expected values.

    Parameters
    ----------
    setup_rosenbrock : fixture
        The fixture providing the Rosenbrock problem instance.

    Assertions
    ----------
    - The function should return the correct values for predefined inputs.
    - The function should return 0 for an input list of all ones.
    """
    # Define test cases with known values
    test_cases = [
        ([2.305, -4.025, 3.805, -1.505], 49665.553),
        ([-4.995, -2.230, -3.706, 2.305], 94539.427),
        ([1.0, 1.0, 1.0, 1.0], 0.0)  # Global minimum
    ]

    for variables, expected_fitness in test_cases:
        fitness_value = setup_rosenbrock.f(variables)
        print(f"Variables: {variables} => Fitness: {fitness_value}, Expected: {expected_fitness}")
        assert isinstance(fitness_value, float)
        assert fitness_value == pytest.approx(expected_fitness, rel=1e-3), \
            f"Expected {expected_fitness}, got {fitness_value}"

if __name__ == "__main__":
    pytest.main()
