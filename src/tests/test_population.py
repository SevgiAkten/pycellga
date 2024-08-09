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
    assert len(pop_list) == population.n_rows * population.n_cols


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
        assert ind.fitness_value == expected_fitness


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
        assert ind.neighbors_positions == expected_neighbors_positions
