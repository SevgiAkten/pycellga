import numpy as np
from cga.population import *
from cga.selection.tournament_selection import *
from cga.recombination.one_point_crossover import *
from cga.mutation.bit_flip_mutation import *
from cga.problems.single_objective.discrete.binary.one_max import OneMax
import time
from typing import Callable, List, Tuple


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
    selection: Callable,
    recombination: Callable,
    mutation: Callable
) -> Tuple[dict, dict, List[float], List[float], float]:
    """
    Optimize the given problem using a genetic algorithm.

    Parameters
    ----------
    n_cols : int
        Number of columns in the population grid.
    n_rows : int
        Number of rows in the population grid.
    n_gen : int
        Number of generations to evolve.
    ch_size : int
        Size of the chromosome.
    gen_type : str
        Type of the genome representation (e.g., 'Binary', 'Permutation', 'Real').
    p_crossover : float
        Probability of crossover (between 0 and 1).
    p_mutation : float
        Probability of mutation (between 0 and 1).
    known_best : float
        Known best solution for gap calculation.
    k_tournament : int
        Size of the tournament for selection.
    problem : AbstractProblem
        The problem instance used for fitness evaluation.
    selection : Callable
        Function or class used for selecting parents.
    recombination : Callable
        Function or class used for recombination (crossover).
    mutation : Callable
        Function or class used for mutation.

    Returns
    -------
    Tuple[dict, dict, List[float], List[float], float]
        optimizer_result : dict
            Best solution details including chromosome, fitness value, and generation found.
        parameters : dict
            Optimization parameters including number of generations, population size, crossover, mutation probabilities, and tournament size.
        best_objectives : List[float]
            List of best fitness values found over generations.
        avg_objectives : List[float]
            List of average fitness values over generations.
        elapsed_time : float
            Time taken to complete the optimization in seconds.
    """

    pop_size = n_cols * n_rows
    best_solutions = []
    best_objectives = []
    best_ever_solution = []
    avg_objectives = []
    start_time = time.time()

    # Generate Initial Population
    pop_list = Population(ch_size, n_rows, n_cols,
                          gen_type, problem).initial_population()

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

    # Evolutionary Algorithm Loop
    generation = 1
    while generation != n_gen + 1:
        for c in range(pop_size):
            offsprings = []
            parents = selection(pop_list, c).get_parents()
            rnd = np.random.rand()

            if rnd < p_crossover:
                offsprings = recombination(
                    parents, problem).get_recombinations()
            else:
                offsprings = parents

            for p in range(len(offsprings)):

                mutation_cand = offsprings[p]

                # for byte_mutation_dynamic and byte_mutation_random_dynamic
                # p_mutation = p_mutation - ((g/n_gen)*p_mutation)

                rnd = np.random.rand()

                if rnd < p_mutation:
                    mutated = mutation(mutation_cand, problem).mutate()
                    offsprings[p] = mutated
                else:
                    pass

                # Replacement: Replace if better
                if offsprings[p].fitness_value < parents[p].fitness_value:
                    index = pop_list.index(parents[p])
                    new_p = offsprings[p]
                    old_p = pop_list[index]
                    pop_list[index] = new_p

                else:
                    pass
        pop_list_ordered = sorted(
            pop_list, key=lambda x: x.fitness_value)

        best_solutions.append(pop_list_ordered[0].chromosome)
        best_objectives.append(pop_list_ordered[0].fitness_value)

        if (pop_list_ordered[0].fitness_value) < best_ever_solution[1]:
            best_ever_solution = [
                pop_list_ordered[0].chromosome,
                pop_list_ordered[0].fitness_value,
                generation,
            ]
        else:
            pass

        mean = sum(map(lambda x: x.fitness_value, pop_list)) / len(pop_list)
        avg_objectives.append(mean)
        
        # Print progress (optional)
        # print(
        #     f"{g} - {pop_list_ordered[0].chromosome} - {pop_list_ordered[0].fitness_value}"
        # )
        generation += 1
    try:
        gap = (best_ever_solution[1]-known_best)*100/known_best
    except ZeroDivisionError:
        gap = "The known best zero division error was occurred."
    except TypeError:
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
