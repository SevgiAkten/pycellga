import pytest
from cga.population import Population
from cga.selection.tournament_selection import TournamentSelection
from cga.recombination.one_point_crossover import OnePointCrossover
from cga.mutation.bit_flip_mutation import BitFlipMutation
from cga.problems.single_objective.continuous.ackley import Ackley
from cga.problems.abstract_problem import AbstractProblem
from typing import Callable, Tuple, List
import time
from cga.optimizer_alpha_cga import *

def test_optimizer_alpha_cga():
    """
    Test the optimize function.

    This test checks if the optimize function runs without errors and returns the expected
    result structure. It uses the OneMax problem as an example.
    """
    n_cols = 5
    n_rows = 5
    n_gen = 10
    ch_size = 10
    gen_type = "Binary"
    p_crossover = 0.8
    p_mutation = 0.1
    known_best = 0
    k_tournament = 2
    problem = Ackley()
    selection = TournamentSelection
    recombination = OnePointCrossover
    mutation = BitFlipMutation

    optimizer_result, parameters, best_objectives, avg_objectives, elapsed_time = optimize(
        n_cols,
        n_rows,
        n_gen,
        ch_size,
        gen_type,
        p_crossover,
        p_mutation,
        known_best,
        k_tournament,
        problem,
        selection,
        recombination,
        mutation
    )

    # Check if the returned structures are dictionaries and lists
    assert isinstance(optimizer_result, dict)
    assert isinstance(parameters, dict)
    assert isinstance(best_objectives, list)
    assert isinstance(avg_objectives, list)
    assert isinstance(elapsed_time, float)

    # Check if optimizer_result has the expected keys
    assert "best_solution_chromosome" in optimizer_result
    assert "best_solution" in optimizer_result
    assert "found_at_generation" in optimizer_result
    assert "known_best_solution" in optimizer_result
    assert "gap" in optimizer_result

    # Check if parameters has the expected keys
    assert "number_of_generation" in parameters
    assert "population_size" in parameters
    assert "probability_of_crossover" in parameters
    assert "probability_of_mutation" in parameters
    assert "tournament_selection" in parameters

    # Check if best_objectives and avg_objectives have the expected length
    assert len(best_objectives) == n_gen + 1
    assert len(avg_objectives) == n_gen + 1

    # Check if the best solution found is at least better or equal to known_best
    assert optimizer_result["best_solution"] >= known_best

# Run the tests
if __name__ == "__main__":
    pytest.main()
