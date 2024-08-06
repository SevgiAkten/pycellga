from cga.problems.single_objective.continuous.rosenbrock import Rosenbrock

def test_rosenbrock():
    """
    Test the Rosenbrock function implementation.

    This test verifies the calculation of the Rosenbrock function value for a given list of continuous variables.
    It compares the function output with known expected values.

    Notes
    -----
    The Rosenbrock function, also known as the Rosenbrock's valley or Rosenbrock's banana function,
    is a common test problem for optimization algorithms. The global minimum is at (1, ..., 1), where the function value is 0.

    Assertions
    ----------
    - The function should return the correct values for predefined inputs.
    - The function should return 0 for an input list of all ones.

    Examples
    --------
    >>> test_rosenbrock()
    """
    theproblem = Rosenbrock()

    # Test cases with known values
    assert theproblem.f([2.305, -4.025, 3.805, -1.505]) == round(49665.553494187516, 3)
    assert theproblem.f([-4.995, -2.230, -3.706, 2.305]) == round(94539.42650987211, 3)
    assert theproblem.f([1 for _ in range(10)]) == round(0, 3)
