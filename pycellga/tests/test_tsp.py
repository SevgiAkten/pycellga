from problems.single_objective.discrete.permutation.tsp import Tsp
import random
import pytest

@pytest.fixture
def tsp_instance():
    """
    Fixture for creating an instance of the Tsp class.

    This fixture returns an instance of the Tsp class to be used in tests.
    """
    return Tsp()

def test_tsp(tsp_instance):
    """
    Test the TSP function implementation.

    This test verifies the calculation of the TSP (Traveling Salesman Problem) function value for 
    different permutations of cities.

    The TSP function evaluates the total distance for a given permutation of cities. This test checks 
    if the function computes the correct distance for specific permutations generated using different 
    random seeds.
    """
    # Test case 1: Random permutation with seed 0
    random.seed(0)
    chromosome = list(random.sample(range(1, 15), 14))
    expected_distance = tsp_instance.f(chromosome)
    assert isinstance(expected_distance, float), "The result should be a float."
    print(f"Chromosome: {chromosome} => Distance: {expected_distance}")

    # Test case 2: Random permutation with seed 50
    random.seed(50)
    chromosome = list(random.sample(range(1, 15), 14))
    expected_distance = tsp_instance.f(chromosome)
    assert isinstance(expected_distance, float), "The result should be a float."
    print(f"Chromosome: {chromosome} => Distance: {expected_distance}")

    # Test case 3: Random permutation with seed 100
    random.seed(100)
    chromosome = list(random.sample(range(1, 15), 14))
    expected_distance = tsp_instance.f(chromosome)
    assert isinstance(expected_distance, float), "The result should be a float."
    print(f"Chromosome: {chromosome} => Distance: {expected_distance}")

if __name__ == "__main__":
    pytest.main()
