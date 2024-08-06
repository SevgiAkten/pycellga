from cga.problems.single_objective.continuous.sphere import Sphere

def test_sphere():
    """
    Test the Sphere function implementation.

    This test checks the calculation of the Sphere function value for given input values.

    The Sphere function is a common benchmark function in optimization, where the global minimum is 
    at f(0, 0, ..., 0) = 0. This test ensures that the function computes the correct results for specific
    input values and verifies that the function behaves as expected.

    It performs assertions to validate:
    - The correctness of the function's output for specific test inputs.
    - The rounding of the function's output to three decimal places.

    Examples
    --------
    >>> test_sphere()
    """

    theproblem = Sphere()

    # Test case 1: Specific input values
    assert theproblem.f([2.305, -4.025, 3.805, -1.505]) == round(38.2567, 3)

    # Test case 2: Different specific input values
    assert theproblem.f([-4.995, -2.230, -3.706, 2.305]) == round(48.970386000000005, 3)

    # Test case 3: Uniform input values (all zeros)
    assert theproblem.f([0 for _ in range(10)]) == round(0, 3)
