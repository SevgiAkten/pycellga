from cga.problems.single_objective.continuous.rastrigin import Rastrigin

def test_rastrigin():
    """
    Test the Rastrigin function implementation.

    This test verifies the calculation of the Rastrigin function value for a given list of continuous variables.
    It compares the function output with known expected values.

    Notes
    -----
    The Rastrigin function is a well-known benchmark function used in optimization problems.
    It has a global minimum value of 0, which is achieved when all variables are 0.

    Assertions
    ----------
    - The function should return the correct values for predefined inputs.
    - The function should return 0 for an input list of all zeros.

    Examples
    --------
    >>> test_rastrigin()
    """
    theproblem = Rastrigin()

    # Test cases with known values
    assert theproblem.f([2.305, -4.025, 3.805, -1.505]) == round(78.37488219770594, 3)
    assert theproblem.f([-4.995, -2.230, -3.706, 2.305]) == round(83.83888661832582, 3)
    assert theproblem.f([0 for _ in range(10)]) == round(0.0, 3)
