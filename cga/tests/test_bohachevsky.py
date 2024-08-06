from cga.problems.single_objective.continuous.bohachevsky import Bohachevsky

def test_bohachevsky():
    """
    Test the Bohachevsky function implementation.

    This test verifies the correctness of the Bohachevsky function by evaluating it at several points and 
    comparing the results to expected values.

    The Bohachevsky function is used as a benchmark for optimization algorithms. It has multiple local minima 
    and is designed to test the performance of optimization algorithms.

    The test performs the following checks:
    1. Evaluates the Bohachevsky function at specific points.
    2. Compares the computed values to the expected rounded results.

    Parameters
    ----------
    None

    Raises
    ------
    AssertionError
        If any of the computed values do not match the expected rounded values.
    """
    # Initialize the Bohachevsky problem instance
    theproblem = Bohachevsky()

    # Test cases with expected rounded results
    assert round(theproblem.f([2.305, -4.025, 3.805, -1.505]), 3) == 103.584, \
        "Bohachevsky function value at [2.305, -4.025, 3.805, -1.505] does not match expected result."

    assert round(theproblem.f([-4.995, -2.230, -3.706, 2.305]), 3) == 95.582, \
        "Bohachevsky function value at [-4.995, -2.230, -3.706, 2.305] does not match expected result."

    assert round(theproblem.f([0 for _ in range(10)]), 3) == 0.0, \
        "Bohachevsky function value at [0, 0, ..., 0] does not match expected result."

if __name__ == "__main__":
    test_bohachevsky()
