from cga.population import *
from cga.individual import *
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

    # Evolutionary Algorithm Loop
    generation = 1
    while generation != n_gen + 1:
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
                generation,
            ]

        mean = sum(map(lambda x: x.fitness_value, pop_list)) / len(pop_list)
        avg_objectives.append(mean)
        
        # Print progress (optional)
        # print(
        #     f"{generation} - {best.chromosome} - {best.fitness_value}"
        # )
        generation += 1
    try:
        gap = (best_ever_solution[1] - known_best) * 100 / known_best
    except ZeroDivisionError:
        gap = "The known best zero division error occurred."
    except Exception as e:
        gap = f"Something else went wrong: {str(e)}"

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


def compete(p1: Individual, p2: Individual) -> Tuple[Individual, Individual]:
    """
    Compare two individuals and return the winner and the loser based on fitness values.

    Parameters
    ----------
    p1 : Individual
        First individual to compare.
    p2 : Individual
        Second individual to compare.

    Returns
    -------
    Tuple[Individual, Individual]
        The winner and the loser individual based on fitness values.
    """
    if p1.fitness_value > p2.fitness_value:
        return p1, p2
    else:
        return p2, p1


def update_vector(vector: List[float], winner: Individual, loser: Individual, pop_size: int):
    """
    Update the vector based on the difference between the winner and loser chromosomes.

    Parameters
    ----------
    vector : List[float]
        Vector to be updated based on the winner and loser chromosomes.
    winner : Individual
        The individual with the better fitness value.
    loser : Individual
        The individual with the worse fitness value.
    pop_size : int
        Size of the population.
    """
    for i in range(len(vector)):
        if winner.chromosome[i] != loser.chromosome[i]:
            if winner.chromosome[i] == 1:
                vector[i] += 1.0 / float(pop_size)
            else:
                vector[i] -= 1.0 / float(pop_size)


def generate_candidate(vector: List[float]) -> List[int]:
    """
    Generate a candidate chromosome based on the given vector.

    Parameters
    ----------
    vector : List[float]
        Vector that represents the probability of each gene being 1.

    Returns
    -------
    List[int]
        Generated chromosome based on the vector probabilities.
    """
    ind = []
    for p in vector:
        ind.append(
            1) if random.rand() < p else ind.append(0)

    return ind
