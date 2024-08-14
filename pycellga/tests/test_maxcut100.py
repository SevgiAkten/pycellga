import pytest

from problems.single_objective.discrete.binary.maxcut100 import Maxcut100


@pytest.fixture
def maxcut_instance():
    """
    Fixture for creating an instance of the Maxcut100 class.

    This fixture returns an instance of the Maxcut100 class to be used in tests.
    """
    return Maxcut100()

def test_maxcut100():
    # Maxcut100 sınıfı örneği oluştur
    problem = Maxcut100()

    # Test durumu: Bütün değerler 0
    chromosome = [0] * 100
    expected_result = 0.0 
    assert problem.f(chromosome) == expected_result, f"Beklenen: {expected_result}, Bulunan: {problem.f(chromosome)}"

    # Test durumu: Bütün değerler 1
    chromosome = [1] * 100
    expected_result = 0.0
    assert problem.f(chromosome) == expected_result, f"Beklenen: {expected_result}, Bulunan: {problem.f(chromosome)}"

    # Test durumu: Karışık değerler
    chromosome = [0, 1] * 50
    expected_result = 1124.0 
    assert problem.f(chromosome) == expected_result, f"Beklenen: {expected_result}, Bulunan: {problem.f(chromosome)}"

if __name__ == "__main__":
    pytest.main()

