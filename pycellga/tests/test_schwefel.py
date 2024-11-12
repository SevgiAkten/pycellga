import pytest
from problems.single_objective.continuous.schwefel import Schwefel

@pytest.fixture
def setup_schwefel():
    """
    Fixture to provide an instance of the Schwefel problem.
    """
    return Schwefel(design_variables=4)

def test_schwefel(setup_schwefel):
    """
    Test the Schwefel function implementation.

    This test verifies the Schwefel function with a set of predefined inputs to ensure accuracy.

    Parameters
    ----------
    setup_schwefel : fixture
        The fixture providing the Schwefel problem instance.
    
    Assertions
    ----------
    - The function's output is correctly rounded to three decimal places.
    - The function returns the expected values for specific inputs.

    Examples
    --------
    >>> test_schwefel_function()
    """

    theproblem = setup_schwefel

    # Test cases with known values
    assert theproblem.f([220.501, -400.025, 30.805, -105.50]) == pytest.approx(1815.910, rel=1e-3), \
        "Failed test for input [220.501, -400.025, 30.805, -105.50]"

    assert theproblem.f([-400.995, -25.230, -410.706, 420.305]) == pytest.approx(2008.838, rel=1e-3), \
        "Failed test for input [-400.995, -25.230, -410.706, 420.305]"

    # Testing for the global minimum case
    assert theproblem.f([420.9687 for _ in range(4)]) == pytest.approx(0.0, rel=1e-3), \
        "Failed test for input [420.9687, 420.9687, 420.9687, 420.9687]"

if __name__ == "__main__":
    pytest.main()
