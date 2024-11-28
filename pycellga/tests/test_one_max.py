import pytest
from problems.single_objective.discrete.binary.one_max import OneMax  

@pytest.fixture
def one_max_instance():
    """
    Fixture for creating an instance of the OneMax class.

    This fixture returns an instance of the OneMax class to be used in tests.
    """
    return OneMax()

def test_one_max(one_max_instance):
    """
    Test the OneMax function implementation.

    This test verifies the calculation of the OneMax function value for specific binary input values.

    The OneMax function evaluates the number of 1s in a binary list. This test ensures that the function 
    computes the correct number of 1s for various test inputs.
    """
    # Test case 1: All variables set to 1
    # Expected output is 5 because there are 5 ones in the input list.
    assert one_max_instance.f([1, 1, 1, 1, 1]) == -5

    # Test case 2: All variables set to 1 in a list of size 6
    # Expected output is 6 because there are 6 ones in the input list.
    assert one_max_instance.f([1, 1, 1, 1, 1, 1]) == -6

    # Test case 3: All variables set to 0
    # Expected output is 0 because there are no ones in the input list.
    assert one_max_instance.f([0 for _ in range(10)]) == 0

    # Test case 4: Mixed 1s and 0s
    # Expected output is 3 because there are 3 ones in the input list.
    assert one_max_instance.f([1, 0, 1, 0, 1]) == -3

if __name__ == "__main__":
    pytest.main()
