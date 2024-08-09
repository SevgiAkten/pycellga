import pytest
from individual import Individual
from population import Population
from grid import Grid
from neighborhoods.linear_9 import Linear9
from byte_operators import *
from problems.abstract_problem import AbstractProblem
from typing import List

class MockProblem(AbstractProblem):
    """
    Mock problem class for testing the Population class.
    """
    def f(self, x: list) -> float:
        return sum(x)

def test_population_initialization():
    """
    Test the initialization of the Population class.
    
    This test checks if the Population class initializes correctly with given parameters.
    """
    ch_size = 10
    n_rows = 5
    n_cols = 5
    gen_type = "Binary"
    problem = MockProblem()
    vector = [0.5] * ch_size

    population = Population(ch_size=ch_size, n_rows=n_rows, n_cols=n_cols, gen_type=gen_type, problem=problem, vector=vector)
    
    assert population.ch_size == ch_size
    assert population.n_rows == n_rows
    assert population.n_cols == n_cols
    assert population.gen_type == gen_type
    assert population.problem == problem
    assert population.vector == vector

def test_initial_population():
    """
    Test the initial_population method of the Population class.
    
    This test checks if the initial_population method generates a list of initialized
    individuals with the correct properties.
    """
    ch_size = 10
    n_rows = 5
    n_cols = 5
    gen_type = "Binary"
    problem = MockProblem()
    vector = [0.5] * ch_size

    population = Population(ch_size=ch_size, n_rows=n_rows, n_cols=n_cols, gen_type=gen_type, problem=problem, vector=vector)
    initial_pop = population.initial_population()
    
    assert len(initial_pop) == n_rows * n_cols

    for ind in initial_pop:
        assert isinstance(ind, Individual)
        assert len(ind.chromosome) == ch_size
        assert isinstance(ind.position, tuple)
        assert isinstance(ind.neighbors_positions, list)
        assert ind.neighbors is None
        assert ind.gen_type == gen_type
        assert ind.ch_size == ch_size

# Run the tests
if __name__ == "__main__":
    pytest.main()
