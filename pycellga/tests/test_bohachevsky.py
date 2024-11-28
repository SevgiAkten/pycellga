import pytest
from problems.single_objective.continuous.bohachevsky import Bohachevsky

@pytest.fixture
def setup_bohachevsky():
    """
    Fixture for creating an instance of the Bohachevsky problem with a specified dimension.

    Returns
    -------
    Bohachevsky
        An instance of the Bohachevsky problem.
    """
    dimension = 4  
    return Bohachevsky(dimension=dimension)

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
    # Test cases with expected results
    assert pytest.approx(setup_bohachevsky.f([2.305, -4.025, 3.805, -1.505]), rel=1e-3) == 103.584, \
        "Bohachevsky function value at [2.305, -4.025, 3.805, -1.505] does not match expected result."

    assert pytest.approx(setup_bohachevsky.f([-4.995, -2.230, -3.706, 2.305]), rel=1e-3) == 95.582, \
        "Bohachevsky function value at [-4.995, -2.230, -3.706, 2.305] does not match expected result."

    assert pytest.approx(setup_bohachevsky.f([0, 0, 0, 0]), rel=1e-3) == 0.0, \
        "Bohachevsky function value at [0, 0, 0, 0] does not match expected result."

if __name__ == "__main__":
    pytest.main()
