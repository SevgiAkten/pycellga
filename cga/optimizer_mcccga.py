import numpy as np
from collections.abc import Callable
import random
import byte_operators
from population import *
from individual import *
from selection.tournament_selection import *
from recombination.one_point_crossover import *
from mutation.bit_flip_mutation import *
import time


def optimize(
    n_cols: int,
    n_rows: int,
    n_gen: int,
    ch_size: int,
    gen_type: str,
    known_best: float,
    k_tournament: int,
    problem: Callable[[list[float]], float],
    selection,
    mins: list[float],
    maxs: list[float]
) -> tuple:

    pop_size = n_cols * n_rows
    best_objectives = []
    best_ever_solution = []
    avg_objectives = []
    start_time = time.time()
    # vector = [0.5 for p in range(ch_size)]
    vector = generate_probability_vector(mins, maxs, pop_size)

    # Generate Initial Population
    pop_list = Population(ch_size, n_rows, n_cols,
                          gen_type, problem, vector).initial_population()

    pop_list_ordered = sorted(
        pop_list, key=lambda x: x.fitness_value)

    best_objectives.append(pop_list_ordered[0].fitness_value)
    best_byte_ch = byte_operators.bits_to_floats(
        pop_list_ordered[0].chromosome)
    best_ever_solution = [
        best_byte_ch,
        pop_list_ordered[0].fitness_value,
        1,
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
            if winner.fitness_value < best.fitness_value:
                best = winner

            update_vector(vector, winner, loser, pop_size)

        pop_list = Population(ch_size, n_rows, n_cols,
                              gen_type, problem, vector).initial_population()
        best_objectives.append(best.fitness_value)
        best_byte_ch = byte_operators.bits_to_floats(
            pop_list_ordered[0].chromosome)

        if (best.fitness_value) < best_ever_solution[1]:
            best_ever_solution = [
                best_byte_ch,
                best.fitness_value,
                g,
            ]

        mean = sum(map(lambda x: x.fitness_value, pop_list)) / len(pop_list)
        avg_objectives.append(mean)
        best_byte_ch = byte_operators.bits_to_floats(best.chromosome)

        print(
            f"{g} - {best_byte_ch} - {best.fitness_value}"
        )
        g += 1

    best_byte_ch = byte_operators.bits_to_floats(sample(vector))
    best_byte_result = problem.f(best_byte_ch)

    if best_byte_result <= best_ever_solution[1]:
        best_ever_solution[0] = best_byte_ch
        best_ever_solution[1] = best_byte_result

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
        "tournament_selection": k_tournament
    }

    end_time = time.time()
    elapsed_time = round((end_time - start_time), 2)  # seconds

    return optimizer_result, parameters, best_objectives, avg_objectives, elapsed_time


def compete(p1: Individual, p2: Individual):
    if p1.fitness_value < p2.fitness_value:
        return p1, p2
    else:
        return p2, p1


def update_vector(vector, winner: Individual, loser: Individual, pop_size):
    for i in range(len(vector)):
        if winner.chromosome[i] != loser.chromosome[i]:
            if winner.chromosome[i] == 1:
                vector[i] += round((1.0 / float(pop_size)), 3)
            else:
                vector[i] -= round((1.0 / float(pop_size)), 3)


def random_vector_between(mins: list, maxs: list) -> list:
    n = len(mins)
    result = [0.0] * n

    for i in range(n):
        result[i] = mins[i] + random.random() * (maxs[i] - mins[i])

    return result


def generate_probability_vector(mins: list, maxs: list, ntries: int) -> list:
    nbits = len(mins) * 32
    mutrate = 1.0 / ntries
    probvector = [0.0] * nbits

    for _ in range(ntries):
        floats = random_vector_between(mins, maxs)
        floatbits = byte_operators.floats_to_bits(floats)
        for k in range(nbits):
            if floatbits[k] == 1:
                probvector[k] = probvector[k] + mutrate

    return probvector


def sample(probvector: list[float]) -> list[int]:
    n = len(probvector)
    newvector = [0] * n

    for i in range(n):
        if random.random() < probvector[i]:
            newvector[i] = 1

    return newvector
