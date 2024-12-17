import pytest
from pycellga.problems.single_objective.continuous.bohachevsky import Bohachevsky

@pytest.fixture
def setup_bohachevsky():
    """
    Fixture for creating an instance of the Bohachevsky problem with a specified dimension.

    Returns
    -------
    Bohachevsky
        An instance of the Bohachevsky problem.
    """
    n_var = 4  # Number of variables
    return Bohachevsky(n_var=n_var)

def test_bohachevsky(setup_bohachevsky):
    """
    Test the Bohachevsky function implementation.

    This test verifies the correctness of the Bohachevsky function by evaluating it at several points and 
    comparing the results to expected values.

    Parameters
    ----------
    setup_bohachevsky : fixture
        The fixture providing the Bohachevsky problem instance.
    """
    # Define test cases with expected results
    test_cases = [
        ([2.305, -4.025, 3.805, -1.505], 103.584),  # Test case 1
        ([-4.995, -2.230, -3.706, 2.305], 95.582),  # Test case 2
        ([0, 0, 0, 0], 0.0)  # Global minimum
    ]

    for variables, expected_fitness in test_cases:
        fitness_value = setup_bohachevsky.f(variables)
        print(f"Variables: {variables} => Fitness: {fitness_value}")
        assert pytest.approx(fitness_value, rel=1e-3) == expected_fitness, \
            f"Bohachevsky function value at {variables} does not match expected result. Expected {expected_fitness}, got {fitness_value}"

if __name__ == "__main__":
    pytest.main()
