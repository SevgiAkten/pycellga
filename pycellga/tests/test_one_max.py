from problems.single_objective.discrete.binary.one_max import OneMax

def test_one_max():
    """
    Test the OneMax function implementation.

    This test verifies the calculation of the OneMax function value for specific binary input values.

    The OneMax function evaluates the number of 1s in a binary list. This test ensures that the function 
    computes the correct number of 1s for various test inputs.

    Examples
    --------
    >>> test_one_max()
    """

    theproblem = OneMax()

    # Test case 1: All variables set to 1
    # Expected output is 5 because there are 5 ones in the input list.
    assert theproblem.f([1, 1, 1, 1, 1]) == 5

    # Test case 2: All variables set to 1 in a list of size 6
    # Expected output is 6 because there are 6 ones in the input list.
    assert theproblem.f([1, 1, 1, 1, 1, 1]) == 6

    # Test case 3: All variables set to 0
    # Expected output is 0 because there are no ones in the input list.
    assert theproblem.f([0 for _ in range(10)]) == 0
