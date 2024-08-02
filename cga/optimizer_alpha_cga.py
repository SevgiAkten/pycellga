import numpy as np
import random as rd
from cga.population import Population
from cga.selection.tournament_selection import *
from cga.recombination.one_point_crossover import *
from cga.mutation.bit_flip_mutation import *
from cga.problems.single_objective.discrete.binary.one_max import OneMax
import time
from typing import Callable, Tuple, List


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
    Perform optimization using an evolutionary algorithm.

    Parameters
    ----------
    n_cols : int
        Number of columns in the grid for the population.
    n_rows : int
        Number of rows in the grid for the population.
    n_gen : int
        Number of generations to run the optimization.
    ch_size : int
        Size of the chromosome.
    gen_type : str
        Type of genome representation ("Binary", "Permutation", "Real-valued").
    p_crossover : float
        Probability of crossover (between 0 and 1).
    p_mutation : float
        Probability of mutation (between 0 and 1).
    known_best : float
        Known best solution value for gap calculation.
    k_tournament : int
        Tournament size for selection.
    problem : AbstractProblem
        The problem instance used to evaluate fitness.
    selection : Callable
        Function used for selection in the evolutionary algorithm.
    recombination : Callable
        Function used for recombination (crossover) in the evolutionary algorithm.
    mutation : Callable
        Function used for mutation in the evolutionary algorithm.

    Returns
    -------
    Tuple[dict, dict, List[float], List[float], float]
        optimizer_result : dict
            Dictionary containing the best solution found, the best solution value, and the generation at which it was found.
        parameters : dict
            Dictionary containing the parameters used in the optimization.
        best_objectives : List[float]
            List of the best fitness values obtained across generations.
        avg_objectives : List[float]
            List of average fitness values across generations.
        elapsed_time : float
            Total elapsed time of the optimization process in seconds.
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
    
    # Sort population by fitness value
    pop_list_ordered = sorted(
        pop_list, key=lambda x: x.fitness_value)

    # Initialize tracking of best solutions
    best_solutions.append(pop_list_ordered[0].chromosome)
    best_objectives.append(pop_list_ordered[0].fitness_value)
    best_ever_solution = [
        pop_list_ordered[0].chromosome,
        pop_list_ordered[0].fitness_value,
        0,
    ]

    # Calculate mean fitness for the initial population
    mean = sum(map(lambda x: x.fitness_value, pop_list)) / len(pop_list)
    avg_objectives.append(mean)

    # Optimization loop
    generation = 1

    while generation != n_gen + 1:
        for c in range(0, pop_size, n_cols):
            # Alpha-male exchange mechanism
            if generation % 10 == 0:
                rnd1 = rd.randrange(1, pop_size+1, n_cols)
                rnd2 = rd.randrange(1, pop_size+1, n_cols)
                while rnd1 == rnd2:
                    rnd2 = np.random.randint(1, n_cols+1)

                alpha_male1 = pop_list[rnd1]
                alpha_male2 = pop_list[rnd2]

                pop_list[rnd2] = alpha_male1
                pop_list[rnd1] = alpha_male2
            ##################################

            for n in range(n_cols):
                offsprings = []
                parents = []

                p1 = pop_list[c]
                p2 = pop_list[c+n]
                parents.append(p1)
                parents.append(p2)

                rnd = np.random.rand()

                # Apply crossover with probability p_crossover
                if rnd < p_crossover:
                    offsprings = recombination(
                        parents, problem).get_recombinations()
                else:
                    offsprings = parents

                for p in range(len(offsprings)):

                    mutation_cand = offsprings[p]
                    rnd = np.random.rand()

                    # Apply mutation with probability p_mutation
                    if rnd < p_mutation:
                        mutated = mutation(mutation_cand, problem).mutate()
                        offsprings[p] = mutated
                    else:
                        pass

                    # Replacement: Replace if offspring is better
                    if offsprings[p].fitness_value < parents[1].fitness_value:
                        try:
                            index = pop_list.index(parents[1])
                        except ValueError:
                            index
                        new_p = offsprings[p]
                        old_p = pop_list[index]
                        pop_list[index] = new_p
                    else:
                        pass
        # Sort population and update best solutions
        pop_list_ordered = sorted(
            pop_list, key=lambda x: x.fitness_value)

        best_solutions.append(pop_list_ordered[0].chromosome)
        best_objectives.append(pop_list_ordered[0].fitness_value)

        # Update best ever solution if current solution is better
        if (pop_list_ordered[0].fitness_value) < best_ever_solution[1]:
            best_ever_solution = [
                pop_list_ordered[0].chromosome,
                pop_list_ordered[0].fitness_value,
                generation,
            ]
        else:
            pass

        # Update average objectives
        mean = sum(map(lambda x: x.fitness_value, pop_list)) / len(pop_list)
        avg_objectives.append(mean)

        # Print progress (optional)
        # print(
        #     f"{generation} - {pop_list_ordered[0].chromosome} - {pop_list_ordered[0].fitness_value}"
        # )

        generation += 1

    # Calculate the gap from the known best solution
    try:
        gap = (best_ever_solution[1] - known_best) * 100 / known_best
    except ZeroDivisionError:
        gap = "Known best solution is zero, cannot calculate gap."
    except Exception as e:
        gap = f"An error occurred: {str(e)}"

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
