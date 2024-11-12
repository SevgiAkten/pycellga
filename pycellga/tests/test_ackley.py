from problems.single_objective.continuous.ackley import Ackley
import numpy as np

def test_ackley():
    """
    Test the Ackley function implementation.

    This test verifies the correctness of the Ackley function by evaluating it at several points and 
    comparing the results to expected values.

    The Ackley function is commonly used as a benchmark for optimization algorithms. It is a continuous 
    function with multiple local minima and a single global minimum.

    The test performs the following checks:
    1. Evaluates the Ackley function at a set of given points.
    2. Compares the computed values to expected results.

    Raises
    ------
    AssertionError
        If any of the computed values do not match the expected values.
    """
    # Initialize the Ackley problem instance with appropriate dimensions
    theproblem = Ackley(dimension=4)  # Set dimension to match the length of test inputs

    # Test cases with expected results
    assert np.isclose(theproblem.f([15, 2.5, -25.502, -30.120]), 21.493, atol=1e-3), \
        "Ackley function value at [15, 2.5, -25.502, -30.120] does not match expected result."

    assert np.isclose(theproblem.f([-13.75, -1.2, 4.20, 2.3]), 16.998, atol=1e-3), \
        "Ackley function value at [-13.75, -1.2, 4.20, 2.3] does not match expected result."

    # Initialize another instance of Ackley with dimension 2 for the next test case
    theproblem_2d = Ackley(dimension=2)
    assert np.isclose(theproblem_2d.f([-15.2, -30.1]), 20.8, atol=1e-1), \
        "Ackley function value at [-15.2, -30.1] does not match expected result."

    assert np.isclose(theproblem_2d.f([0, 0]), 0.0, atol=1e-6), \
        "Ackley function value at [0, 0] does not match expected result."

if __name__ == "__main__":
    test_ackley()
