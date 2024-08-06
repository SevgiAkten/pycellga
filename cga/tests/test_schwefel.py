from cga.problems.single_objective.continuous.schwefel import Schwefel

def test_schwefel():
    """
    Test the Schwefel function implementation.

    This test verifies the functionality of the Schwefel function on a set of predefined input values.
    
    The Schwefel function is used as a benchmark in optimization problems, and this test ensures
    that the function computes the expected results for given inputs.

    It performs assertions to check:
    - The correctness of the function's output for specific input values.
    - The proper rounding of the function's output to three decimal places.

    Notes
    -----
    The Schwefel function is typically used to evaluate optimization algorithms, and the expected values
    for the test cases are specific to the known behavior of the function.

    Examples
    --------
    >>> test_schwefel()
    """

    theproblem = Schwefel()

    # Test case 1: Specific input values
    assert theproblem.f([220.501, -400.025, 30.805, -105.50]) == round(1815.9104334968686, 3)

    # Test case 2: Different specific input values
    assert theproblem.f([-400.995, -25.230, -410.706, 420.305]) == round(2008.8379872817275, 3)

    # Test case 3: Uniform input values
    assert round(theproblem.f([420.9687 for i in range(10)]), 2) == round(0.0, 3)
