import pytest
from problems.single_objective.discrete.binary.maxcut100 import Maxcut100

@pytest.fixture
def maxcut_instance():
    """
    Fixture for creating an instance of the Maxcut100 class.
    """
    return Maxcut100()

def test_maxcut100(maxcut_instance):

    chromosome = [0] * 100
    expected_result = 0.0
    assert maxcut_instance.f(chromosome) == expected_result, f"Beklenen: {expected_result}, Bulunan: {maxcut_instance.f(chromosome)}"

    chromosome = [1] * 100
    expected_result = 0.0
    assert maxcut_instance.f(chromosome) == expected_result, f"Beklenen: {expected_result}, Bulunan: {maxcut_instance.f(chromosome)}"

    chromosome = [0, 1] * 50
    expected_result = 567.5 
    computed_result = maxcut_instance.f(chromosome)
    assert computed_result == expected_result, f"Beklenen: {expected_result}, Bulunan: {computed_result}"

if __name__ == "__main__":
    pytest.main()
