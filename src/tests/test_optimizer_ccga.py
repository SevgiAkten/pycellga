import pytest
from individual import Individual
from population import Population
from selection.tournament_selection import TournamentSelection
from recombination.one_point_crossover import OnePointCrossover
from mutation.bit_flip_mutation import BitFlipMutation
from problems.single_objective.continuous.ackley import Ackley
from problems.abstract_problem import AbstractProblem
from typing import Callable, List, Tuple
from optimizer_ccga import *


def test_optimizer_ccga():
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

    optimizer_result, parameters, best_objectives, avg_objectives, elapsed_time = ccga(
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


    # Check if the best solution found is at least better or equal to known_best
    assert optimizer_result["best_solution"] >= known_best

    # Check if elapsed_time is a positive number
    assert elapsed_time > 0


def test_compete():
    """
    Test the compete function.

    This test checks if the compete function correctly identifies the winner and loser based on fitness values.
    """
    ind1 = Individual(gen_type="Binary", ch_size=10)
    ind1.fitness_value = 5
    ind2 = Individual(gen_type="Binary", ch_size=10)
    ind2.fitness_value = 3

    winner, loser = compete(ind1, ind2)

    assert winner == ind1
    assert loser == ind2

    ind1.fitness_value = 2
    winner, loser = compete(ind1, ind2)

    assert winner == ind2
    assert loser == ind1


def test_update_vector():
    """
    Test the update_vector function.

    This test checks if the update_vector function correctly updates the vector based on the winner and loser chromosomes.
    """
    vector = [0.5, 0.5, 0.5, 0.5]
    winner = Individual(gen_type="Binary", ch_size=4)
    winner.chromosome = [1, 0, 1, 0]
    loser = Individual(gen_type="Binary", ch_size=4)
    loser.chromosome = [0, 1, 0, 1]
    pop_size = 4

    update_vector(vector, winner, loser, pop_size)

    assert vector == [0.75, 0.25, 0.75, 0.25]


def test_generate_candidate():
    """
    Test the generate_candidate function.

    This test checks if the generate_candidate function correctly generates a chromosome based on the given vector probabilities.
    """
    vector = [0.5, 0.5, 0.5, 0.5]
    candidate = generate_candidate(vector)

    assert len(candidate) == 4
    assert all(gene in [0, 1] for gene in candidate)


# Run the tests
if __name__ == "__main__":
    pytest.main()
