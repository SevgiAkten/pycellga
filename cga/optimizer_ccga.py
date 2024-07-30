import numpy as np
import random as rd
from population import *
from individual import *
from selection.tournament_selection import *
from recombination.one_point_crossover import *
from mutation.bit_flip_mutation import *
from problems.single_objective.discrete.binary.one_max import OneMax
import time


def optimize(
    n_cols: int,
    n_rows: int,
    n_gen: int,
    ch_size: int,
    gen_type: str,
    p_crossover: float,
    p_mutation: float,
    known_best: float,
    k_tournament: int,
    problem: AbstractProblem,
    selection,
    recombination,
    mutation
) -> tuple:

    pop_size = n_cols * n_rows
    best_solutions = []
    best_objectives = []
    best_ever_solution = []
    avg_objectives = []
    start_time = time.time()
    vector = [0.5 for p in range(ch_size)]

    # Generate Initial Population
    pop_list = Population(ch_size, n_rows, n_cols,
                          gen_type, problem, vector).initial_population()

    pop_list_ordered = sorted(
        pop_list, key=lambda x: x.fitness_value)

    best_solutions.append(pop_list_ordered[0].chromosome)
    best_objectives.append(pop_list_ordered[0].fitness_value)
    best_ever_solution = [
        pop_list_ordered[0].chromosome,
        pop_list_ordered[0].fitness_value,
        0,
    ]

    mean = sum(map(lambda x: x.fitness_value, pop_list)) / len(pop_list)
    avg_objectives.append(mean)
    best = pop_list_ordered[0]

    # -----------------------------------------------------------------
    g = 1
    while g != n_gen + 1:
        for c in range(pop_size):

            parents = selection(pop_list, c).get_parents()
            p1 = parents[0]
            p2 = parents[1]

            winner, loser = compete(p1, p2)

            if winner.fitness_value > best.fitness_value:
                best = winner

            update_vector(vector, winner, loser, pop_size)
            vector

            best.ch_size = len(best.chromosome)
            pop_list = Population(ch_size, n_rows, n_cols,
                                  gen_type, problem, vector).initial_population()

        if (best.fitness_value) > best_ever_solution[1]:
            best_ever_solution = [
                best.chromosome,
                best.fitness_value,
                g,
            ]

        mean = sum(map(lambda x: x.fitness_value, pop_list)) / len(pop_list)
        avg_objectives.append(mean)

        print(
            f"{g} - {best.chromosome} - {best.fitness_value}"
        )
        g += 1
    try:
        gap = (best_ever_solution[1]-known_best)*100/known_best
    except ZeroDivisionError:
        gap = "The known best zero division error was occurred."
    except:
        gap = "Something else went wrong"
    # -----------------------------------------------------------------

    optimizer_result = {
        "best_solution_chromosome": best_ever_solution[0],
        "best_solution": best_ever_solution[1],
        "found_at_generation": best_ever_solution[2],
        "known_best_solution": known_best,
        "gap": gap
    }
    parameters = {
        "number_of_generation": n_gen,
        "population_size": n_cols*n_rows,
        "probability_of_crossover": p_crossover*100,
        "probability_of_mutation": p_mutation*100,
        "tournament_selection": k_tournament
    }
    end_time = time.time()
    elapsed_time = round((end_time - start_time), 2)  # seconds

    return optimizer_result, parameters, best_objectives, avg_objectives, elapsed_time


def compete(p1: Individual, p2: Individual):
    if p1.fitness_value > p2.fitness_value:
        return p1, p2
    else:
        return p2, p1


def update_vector(vector, winner: Individual, loser: Individual, pop_size):
    for i in range(len(vector)):
        if winner.chromosome[i] != loser.chromosome[i]:
            if winner.chromosome[i] == 1:
                vector[i] += 1.0 / float(pop_size)
            else:
                vector[i] -= 1.0 / float(pop_size)


def generate_candidate(vector: list) -> list:
    ind = []
    for p in vector:
        ind.append(
            1) if random.rand() < p else ind.append(0)

    return ind
