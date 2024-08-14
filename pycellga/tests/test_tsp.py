from problems.single_objective.discrete.permutation.tsp import Tsp
import random

def test_tsp():
    """
    Test the Tsp function implementation.

    This test verifies the calculation of the TSP (Traveling Salesman Problem) function value for 
    different permutations of cities.

    The TSP function evaluates the total distance for a given permutation of cities. This test checks 
    if the function computes the correct distance for specific permutations generated using different 
    random seeds.

    Examples
    --------
    >>> test_tsp()
    """
    
    theproblem = Tsp()

    # Test case 1: Random permutation with seed 0
    # The expected result is the distance calculated for the permutation generated with seed 0.
    random.seed(0)
    assert theproblem.f(
        list(random.sample(range(1, 15), 14))) == 6094.6

    # Test case 2: Random permutation with seed 50
    # The expected result is the distance calculated for the permutation generated with seed 50.
    random.seed(50)
    assert theproblem.f(
        list(random.sample(range(1, 15), 14))) == 6879.0

    # Test case 3: Random permutation with seed 100
    # The expected result is the distance calculated for the permutation generated with seed 100.
    random.seed(100)
    assert theproblem.f(
        list(random.sample(range(1, 15), 14))) == 8222.0
