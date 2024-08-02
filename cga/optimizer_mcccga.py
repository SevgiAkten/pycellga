from collections.abc import Callable
import random
import byte_operators
from cga.population import Population
from cga.individual import Individual
from cga.selection.tournament_selection import *
from cga.recombination.one_point_crossover import *
from cga.mutation.bit_flip_mutation import *
import time
from typing import List, Tuple


def optimize(
    n_cols: int,
    n_rows: int,
    n_gen: int,
    ch_size: int,
    gen_type: str,
    known_best: float,
    k_tournament: int,
    problem: Callable[[List[float]], float],
    selection: Callable,
    mins: List[float],
    maxs: List[float]
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
    known_best : float
        Known best solution for gap calculation.
    k_tournament : int
        Size of the tournament for selection.
    problem : Callable[[List[float]], float]
        Function to evaluate the fitness of a solution. Takes a list of floats and returns a float.
    selection : Callable
        Function or class used for selecting parents.
    mins : List[float]
        List of minimum values for the probability vector generation.
    maxs : List[float]
        List of maximum values for the probability vector generation.

    Returns
    -------
    Tuple[dict, dict, List[float], List[float], float]
        optimizer_result : dict
            Best solution details including chromosome, fitness value, and generation found.
        parameters : dict
            Optimization parameters including number of generations, population size, and tournament size.
        best_objectives : List[float]
            List of best fitness values found over generations.
        avg_objectives : List[float]
            List of average fitness values over generations.
        elapsed_time : float
            Time taken to complete the optimization in seconds.
    """

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

    # Evolutionary Algorithm Loop
    generation = 1
    while generation != n_gen + 1:
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
                generation,
            ]

        mean = sum(map(lambda x: x.fitness_value, pop_list)) / len(pop_list)
        avg_objectives.append(mean)
        best_byte_ch = byte_operators.bits_to_floats(best.chromosome)

        # Print progress (optional)
        # print(
        #     f"{g} - {best_byte_ch} - {best.fitness_value}"
        # )
        generation += 1

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


def compete(p1: Individual, p2: Individual) -> Tuple[Individual, Individual]:
    """
    Compete between two individuals to determine the better one.

    Parameters
    ----------
    p1 : Individual
        First individual.
    p2 : Individual
        Second individual.

    Returns
    -------
    Tuple[Individual, Individual]
        The better individual and the loser.
    """
    if p1.fitness_value < p2.fitness_value:
        return p1, p2
    else:
        return p2, p1


def update_vector(vector: List[float], winner: Individual, loser: Individual, pop_size: int):
    """
    Update the probability vector based on the winner and loser individuals.

    Parameters
    ----------
    vector : List[float]
        Probability vector to be updated.
    winner : Individual
        The winning individual.
    loser : Individual
        The losing individual.
    pop_size : int
        Size of the population.
    """
    for i in range(len(vector)):
        if winner.chromosome[i] != loser.chromosome[i]:
            if winner.chromosome[i] == 1:
                vector[i] += round((1.0 / float(pop_size)), 3)
            else:
                vector[i] -= round((1.0 / float(pop_size)), 3)


def random_vector_between(mins: List[float], maxs: List[float]) -> List[float]:
    """
    Generate a random vector of floats between the given minimum and maximum values.

    Parameters
    ----------
    mins : List[float]
        List of minimum values.
    maxs : List[float]
        List of maximum values.

    Returns
    -------
    List[float]
        Randomly generated vector.
    """
    n = len(mins)
    result = [0.0] * n

    for i in range(n):
        result[i] = mins[i] + random.random() * (maxs[i] - mins[i])

    return result


def generate_probability_vector(mins: List[float], maxs: List[float], ntries: int) -> List[float]:
    """
    Generate a probability vector based on the given minimum and maximum values.

    Parameters
    ----------
    mins : List[float]
        List of minimum values.
    maxs : List[float]
        List of maximum values.
    ntries : int
        Number of trials for generating the probability vector.

    Returns
    -------
    List[float]
        Probability vector.
    """
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


def sample(probvector: List[float]) -> List[int]:
    """
    Sample a vector based on the provided probability vector.

    Parameters
    ----------
    probvector : List[float]
        Probability vector for sampling.

    Returns
    -------
    List[int]
        Sampled binary vector.
    """
    n = len(probvector)
    newvector = [0] * n

    for i in range(n):
        if random.random() < probvector[i]:
            newvector[i] = 1

    return newvector
