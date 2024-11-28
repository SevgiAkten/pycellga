import pytest
from individual import Individual, GeneType
from grid import Grid
from neighborhoods.linear_9 import Linear9
from byte_operators import bits_to_floats
from problems.abstract_problem import AbstractProblem
from typing import List
from population import Population, OptimizationMethod


class MockProblem(AbstractProblem):
    """
    A mock problem for testing purposes.

    Methods
    -------
    f(chromosome : List[float]) -> float
        Returns the sum of the chromosome as the fitness value.
    """
    def __init__(self):
        super().__init__(design_variables=10, bounds=[(0, 1)] * 10, objectives=1)
    
    def f(self, chromosome: List[float]) -> float:
        return sum(chromosome)


@pytest.fixture
def setup_population():
    """
    Fixture for setting up a Population object.

    Returns
    -------
    Population
        A population instance with a mock problem.
    """
    mock_problem = MockProblem()
    return Population(
        method_name=OptimizationMethod.CGA,
        ch_size=10,
        n_rows=3,
        n_cols=3,
        gen_type=GeneType.BINARY,
        problem=mock_problem
    )


def test_initial_population_size(setup_population):
    """
    Test the size of the initial population.

    Parameters
    ----------
    setup_population : Population
        The population fixture.

    Asserts
    -------
    True if the size of the population is correct.
    """
    population = setup_population
    pop_list = population.initial_population()
    expected_size = population.n_rows * population.n_cols
    assert len(pop_list) == expected_size, f"Expected population size: {expected_size}, found: {len(pop_list)}"


def test_fitness_evaluation(setup_population):
    """
    Test the fitness evaluation of the individuals.

    Parameters
    ----------
    setup_population : Population
        The population fixture.

    Asserts
    -------
    True if the fitness evaluation is correctly performed.
    """
    population = setup_population
    pop_list = population.initial_population()

    for ind in pop_list:
        expected_fitness = population.problem.f(ind.chromosome)
        assert ind.fitness_value == expected_fitness, f"Expected fitness: {expected_fitness}, found: {ind.fitness_value}"


def test_neighborhood_assignment(setup_population):
    """
    Test the neighborhood assignment for the individuals.

    Parameters
    ----------
    setup_population : Population
        The population fixture.

    Asserts
    -------
    True if neighborhood positions are correctly assigned.
    """
    population = setup_population
    pop_list = population.initial_population()

    for ind in pop_list:
        expected_neighbors_positions = Linear9(
            position=ind.position, n_rows=population.n_rows, n_cols=population.n_cols
        ).calculate_neighbors_positions()
        assert ind.neighbors_positions == expected_neighbors_positions, (
            f"Expected neighbors: {expected_neighbors_positions}, found: {ind.neighbors_positions}"
        )

if __name__ == "__main__":
    pytest.main()
