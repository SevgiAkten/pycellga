
# ------------------------------ selection --------------------------------- #
from selection.roulette_wheel_selection import RouletteWheelSelection
from selection.tournament_selection import TournamentSelection
from selection.selection_operator import SelectionOperator
# -------------------------------------------------------------------------- #

# ------------------------------ recombination ----------------------------- #
from recombination.one_point_crossover import OnePointCrossover
from recombination.pmx_crossover import PMXCrossover
from recombination.two_point_crossover import TwoPointCrossover
from recombination.uniform_crossover import UniformCrossover
from recombination.byte_uniform_crossover import ByteUniformCrossover
from recombination.byte_one_point_crossover import ByteOnePointCrossover
from recombination.flat_crossover import FlatCrossover
from recombination.arithmetic_crossover import ArithmeticCrossover
from recombination.blxalpha_crossover import BlxalphaCrossover
from recombination.linear_crossover import LinearCrossover
from recombination.unfair_avarage_crossover import UnfairAvarageCrossover
from recombination.recombination_operator import RecombinationOperator
# -------------------------------------------------------------------------- #

# -------------------------------- mutation -------------------------------- #
from mutation.bit_flip_mutation import BitFlipMutation
from mutation.byte_mutation import ByteMutation
from mutation.byte_mutation_random import ByteMutationRandom
from mutation.insertion_mutation import InsertionMutation
from mutation.shuffle_mutation import ShuffleMutation
from mutation.swap_mutation import SwapMutation
from mutation.two_opt_mutation import TwoOptMutation
from mutation.float_uniform_mutation import FloatUniformMutation
from mutation.mutation_operator import MutationOperator
# -------------------------------------------------------------------------- #


# ------------------- problems.single_objective.continuous -------------------------------- #
from problems.single_objective.continuous.ackley import *
from problems.single_objective.continuous.bentcigar import Bentcigar
from problems.single_objective.continuous.bohachevsky import Bohachevsky
from problems.single_objective.continuous.chichinadze import Chichinadze
from problems.single_objective.continuous.dropwave import Dropwave
from problems.single_objective.continuous.fms import Fms
from problems.single_objective.continuous.griewank import Griewank
from problems.single_objective.continuous.holzman import Holzman
from problems.single_objective.continuous.levy import Levy
from problems.single_objective.continuous.matyas import Matyas
from problems.single_objective.continuous.pow import Pow
from problems.single_objective.continuous.powell import Powell
from problems.single_objective.continuous.rastrigin import Rastrigin
from problems.single_objective.continuous.rosenbrock import Rosenbrock
from problems.single_objective.continuous.rothellipsoid import Rothellipsoid
from problems.single_objective.continuous.schaffer import Schaffer
from problems.single_objective.continuous.schaffer2 import Schaffer2
from problems.single_objective.continuous.schwefel import Schwefel
from problems.single_objective.continuous.sphere import Sphere
from problems.single_objective.continuous.styblinskitang import StyblinskiTang
from problems.single_objective.continuous.sumofdifferentpowers import Sumofdifferentpowers
from problems.single_objective.continuous.threehumps import Threehumps
from problems.single_objective.continuous.zakharov import Zakharov
from problems.single_objective.continuous.zettle import Zettle
# ----------------------------------------------------------------------------------------------- #


# ------------------- problems.single_objective.discrete.binary -------------------------------- #
from problems.single_objective.discrete.binary.count_sat import CountSat
from problems.single_objective.discrete.binary.ecc import Ecc
from problems.single_objective.discrete.binary.maxcut20_01 import Maxcut20_01
from problems.single_objective.discrete.binary.maxcut20_09 import Maxcut20_09
from problems.single_objective.discrete.binary.maxcut100 import Maxcut100
from problems.single_objective.discrete.binary.mmdp import Mmdp
from problems.single_objective.discrete.binary.one_max import OneMax
from problems.single_objective.discrete.binary.peak import Peak
# ----------------------------------------------------------------------------------------------- #


# ------------------- problems.single_objective.discrete.permutation.tsp ------------------------ #
from problems.single_objective.discrete.permutation.tsp import Tsp
# ----------------------------------------------------------------------------------------------- #




import random
import numpy as np
import byte_operators
from population import *
from individual import *
from mutation.bit_flip_mutation import *
from selection.tournament_selection import *
from recombination.one_point_crossover import *
from problems.single_objective.discrete.binary.one_max import *

from typing import Callable, List, Tuple
from collections.abc import Callable


from dataclasses import dataclass
from typing import List, Callable

@dataclass
class Result:
    chromosome: List[float]
    fitness_value: float
    generation_found: int

def cga(
    n_cols: int,
    n_rows: int,
    n_gen: int,
    ch_size: int,
    gen_type: str,
    p_crossover: float,
    p_mutation: float,
    problem: AbstractProblem,
    selection: SelectionOperator,
    recombination: RecombinationOperator,
    mutation: MutationOperator,
    mins: List[float] = [],
    maxs: List[float] = [],
    seed_par: int = None
) -> Result:
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
    problem : AbstractProblem
        The problem instance used for fitness evaluation.
    selection : SelectionOperator
        Function or class used for selecting parents.
    recombination : RecombinationOperator
        Function or class used for recombination (crossover).
    mutation : MutationOperator
        Function or class used for mutation.
    mins : list[float]
        List of minimum values for each gene in the chromosome (for real value optimization).
    maxs : list[float]
        List of maximum values for each gene in the chromosome (for real value optimization).
    seed_par : int
        Ensures the random number generation is repeatable.

    Returns
    -------
    Result
        A Result object containing the best solution found, with its chromosome, fitness value, and generation.
    """

    if seed_par is not None:
        np.random.seed(seed_par)
        random.seed(seed_par)

    pop_size = n_cols * n_rows
    best_solutions = []
    best_objectives = []
    avg_objectives = []
    method_name = OptimizationMethod.CGA

    # Generate Initial Population
    pop_list = Population(method_name, ch_size, n_rows, n_cols,
                          gen_type, problem, mins=mins, maxs=maxs).initial_population()

    pop_list_ordered = sorted(pop_list, key=lambda x: x.fitness_value)

    best_solutions.append(pop_list_ordered[0].chromosome)
    best_objectives.append(pop_list_ordered[0].fitness_value)
    best_ever_solution = Result(
        chromosome=pop_list_ordered[0].chromosome,
        fitness_value=pop_list_ordered[0].fitness_value,
        generation_found=0
    )

    mean = sum(ind.fitness_value for ind in pop_list) / len(pop_list)
    avg_objectives.append(mean)

    # Evolutionary Algorithm Loop
    generation = 1
    while generation != n_gen + 1:
        for c in range(pop_size):
            offsprings = []
            parents = selection(pop_list, c).get_parents()
            rnd = np.random.rand()

            if rnd < p_crossover:
                offsprings = recombination(parents, problem).get_recombinations()
            else:
                offsprings = parents

            for p in range(len(offsprings)):
                mutation_cand = offsprings[p]
                rnd = np.random.rand()

                if rnd < p_mutation:
                    mutated = mutation(mutation_cand, problem).mutate()
                    offsprings[p] = mutated

                # Replacement: Replace if better
                if offsprings[p].fitness_value < parents[p].fitness_value:
                    index = pop_list.index(parents[p])
                    pop_list[index] = offsprings[p]

        pop_list_ordered = sorted(pop_list, key=lambda x: x.fitness_value)
        best_solutions.append(pop_list_ordered[0].chromosome)
        best_objectives.append(pop_list_ordered[0].fitness_value)

        if pop_list_ordered[0].fitness_value < best_ever_solution.fitness_value:
            best_ever_solution = Result(
                chromosome=pop_list_ordered[0].chromosome,
                fitness_value=pop_list_ordered[0].fitness_value,
                generation_found=generation
            )

        mean = sum(ind.fitness_value for ind in pop_list) / len(pop_list)
        avg_objectives.append(mean)
        generation += 1
    
    return best_ever_solution

def sync_cga(
    n_cols: int,
    n_rows: int,
    n_gen: int,
    ch_size: int,
    gen_type: str,
    p_crossover: float,
    p_mutation: float,
    problem: Callable[[List[float]], float],
    selection: SelectionOperator,
    recombination: RecombinationOperator,
    mutation: MutationOperator,
    mins: List[float] = [],
    maxs: List[float] = [],
    seed_par: int = None
) -> Result:
    """
    Optimize the given problem using a synchronous cellular genetic algorithm (Sync-CGA).

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
        Probability of crossover between parents.
    p_mutation : float
        Probability of mutation in offspring.
    problem : Callable[[List[float]], float]
        Function to evaluate the fitness of a solution. Takes a list of floats and returns a float.
    selection : SelectionOperator
        Function or class used for selecting parents.
    recombination : RecombinationOperator
        Function or class used for recombination (crossover).
    mutation : MutationOperator
        Function or class used for mutation.
    mins : List[float]
        List of minimum values for each gene in the chromosome (for real value optimization).
    maxs : List[float]
        List of maximum values for each gene in the chromosome (for real value optimization).
    seed_par : int
        Ensures the random number generation is repeatable.
        
    Returns
    -------
    Result
        A Result object containing the best solution found, with its chromosome, fitness value, and generation.
    """

    if seed_par is not None:
        np.random.seed(seed_par)
        random.seed(seed_par)

    pop_size = n_cols * n_rows
    best_solutions = []
    best_objectives = []
    avg_objectives = []
    method_name = OptimizationMethod.SYNCGA

    # Generate Initial Population
    pop_list = Population(method_name, ch_size, n_rows, n_cols,
                          gen_type, problem, mins=mins, maxs=maxs).initial_population()

    # Sort population by fitness value
    pop_list_ordered = sorted(pop_list, key=lambda x: x.fitness_value)

    # Track the best solution in the initial population
    best_solutions.append(pop_list_ordered[0].chromosome)
    best_objectives.append(pop_list_ordered[0].fitness_value)
    best_ever_solution = Result(
        chromosome=pop_list_ordered[0].chromosome,
        fitness_value=pop_list_ordered[0].fitness_value,
        generation_found=0
    )

    # Calculate the mean fitness for the initial population
    mean = sum(map(lambda x: x.fitness_value, pop_list)) / len(pop_list)
    avg_objectives.append(mean)

    # Evolutionary Algorithm Loop
    generation = 1
    aux_poplist = []

    while generation != n_gen + 1:
        aux_poplist = pop_list.copy()  # Create a copy of the population for synchronous update

        for c in range(pop_size):
            offsprings = []
            # Select parents
            parents = selection(pop_list, c).get_parents()
            rnd = np.random.rand()

            # Apply crossover with probability p_crossover
            if rnd < p_crossover:
                offsprings = recombination(parents, problem).get_recombinations()
            else:
                offsprings = parents

            for p in range(len(offsprings)):
                mutation_cand = offsprings[p]
                rnd = np.random.rand()

                # Apply mutation with probability p_mutation
                if rnd < p_mutation:
                    mutated = mutation(mutation_cand, problem).mutate()
                    offsprings[p] = mutated

                # Replacement: Replace if offspring is better
                if offsprings[p].fitness_value < parents[p].fitness_value:
                    index = pop_list.index(parents[p])
                    aux_poplist[index] = offsprings[p]

        # Update population synchronously
        pop_list = aux_poplist
        pop_list_ordered = sorted(pop_list, key=lambda x: x.fitness_value)

        # Track best solutions
        best_solutions.append(pop_list_ordered[0].chromosome)
        best_objectives.append(pop_list_ordered[0].fitness_value)

        # Update best ever solution if the current solution is better
        if pop_list_ordered[0].fitness_value < best_ever_solution.fitness_value:
            best_ever_solution = Result(
                chromosome=pop_list_ordered[0].chromosome,
                fitness_value=pop_list_ordered[0].fitness_value,
                generation_found=generation
            )

        # Calculate the mean fitness for the current generation
        mean = sum(map(lambda x: x.fitness_value, pop_list)) / len(pop_list)
        avg_objectives.append(mean)

        generation += 1

    return best_ever_solution

def alpha_cga(
    n_cols: int,
    n_rows: int,
    n_gen: int,
    ch_size: int,
    gen_type: str,
    p_crossover: float,
    p_mutation: float,
    problem: AbstractProblem,
    selection: SelectionOperator,
    recombination: RecombinationOperator,
    mutation: MutationOperator,
    mins: List[float] = [],
    maxs: List[float] = [],
    seed_par: int = None
) -> Result:
    """
    Optimize a problem using an evolutionary algorithm with an alpha-male exchange mechanism.

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
    gen_type : GeneType
        Type of genome representation (GeneType.BINARY, GeneType.PERMUTATION, or GeneType.REAL).
    p_crossover : float
        Probability of crossover, should be between 0 and 1.
    p_mutation : float
        Probability of mutation, should be between 0 and 1.
    problem : AbstractProblem
        The problem instance used to evaluate fitness.
    selection : SelectionOperator
        Function used for selection in the evolutionary algorithm.
    recombination : RecombinationOperator
        Function used for recombination (crossover) in the evolutionary algorithm.
    mutation : MutationOperator
        Function used for mutation in the evolutionary algorithm.
    mins : List[float]
        List of minimum values for each gene in the chromosome (for real value optimization).
    maxs : List[float]
        List of maximum values for each gene in the chromosome (for real value optimization).
    seed_par : int
        Ensures the random number generation is repeatable.

    Returns
    -------
    Result
        A Result object containing the best solution found, with its chromosome, fitness value, and generation.
    """

    if seed_par is not None:
        np.random.seed(seed_par)
        random.seed(seed_par)

    pop_size = n_cols * n_rows
    best_solutions = []
    best_objectives = []
    avg_objectives = []
    method_name = OptimizationMethod.ALPHA_CGA

    # Generate Initial Population
    pop_list = Population(method_name, ch_size, n_rows, n_cols,
                          gen_type, problem, mins=mins, maxs=maxs).initial_population()
    
    # Sort population by fitness value
    pop_list_ordered = sorted(pop_list, key=lambda x: x.fitness_value)

    # Initialize tracking of best solutions
    best_solutions.append(pop_list_ordered[0].chromosome)
    best_objectives.append(pop_list_ordered[0].fitness_value)
    best_ever_solution = Result(
        chromosome=pop_list_ordered[0].chromosome,
        fitness_value=pop_list_ordered[0].fitness_value,
        generation_found=0
    )

    # Calculate mean fitness for the initial population
    mean = sum(map(lambda x: x.fitness_value, pop_list)) / len(pop_list)
    avg_objectives.append(mean)

    # Optimization loop
    generation = 1

    while generation != n_gen + 1:
        for c in range(0, pop_size, n_cols):
            # Alpha-male exchange mechanism
            if generation % 10 == 0:
                rnd1 = rd.randrange(1, pop_size + 1, n_cols)
                rnd2 = rd.randrange(1, pop_size + 1, n_cols)
                while rnd1 == rnd2:
                    rnd2 = np.random.randint(1, n_cols + 1)

                alpha_male1 = pop_list[rnd1]
                alpha_male2 = pop_list[rnd2]

                pop_list[rnd2] = alpha_male1
                pop_list[rnd1] = alpha_male2

            for n in range(n_cols):
                offsprings = []
                parents = []

                p1 = pop_list[c]
                p2 = pop_list[c + n]
                parents.append(p1)
                parents.append(p2)

                rnd = np.random.rand()

                # Apply crossover with probability p_crossover
                if rnd < p_crossover:
                    offsprings = recombination(parents, problem).get_recombinations()
                else:
                    offsprings = parents

                for p in range(len(offsprings)):

                    mutation_cand = offsprings[p]
                    rnd = np.random.rand()

                    # Apply mutation with probability p_mutation
                    if rnd < p_mutation:
                        mutated = mutation(mutation_cand, problem).mutate()
                        offsprings[p] = mutated

                    # Replacement: Replace if offspring is better
                    if offsprings[p].fitness_value < parents[1].fitness_value:
                        try:
                            index = pop_list.index(parents[1])
                        except ValueError:
                            continue
                        new_p = offsprings[p]
                        pop_list[index] = new_p

        # Sort population and update best solutions
        pop_list_ordered = sorted(pop_list, key=lambda x: x.fitness_value)

        best_solutions.append(pop_list_ordered[0].chromosome)
        best_objectives.append(pop_list_ordered[0].fitness_value)

        # Update best ever solution if current solution is better
        if pop_list_ordered[0].fitness_value < best_ever_solution.fitness_value:
            best_ever_solution = Result(
                chromosome=pop_list_ordered[0].chromosome,
                fitness_value=pop_list_ordered[0].fitness_value,
                generation_found=generation
            )

        # Update average objectives
        mean = sum(map(lambda x: x.fitness_value, pop_list)) / len(pop_list)
        avg_objectives.append(mean)

        generation += 1

    return best_ever_solution

def ccga(
    n_cols: int,
    n_rows: int,
    n_gen: int,
    ch_size: int,
    gen_type: str,
    problem: AbstractProblem,
    selection: SelectionOperator,
    mins: List[float] = [],
    maxs: List[float] = []
) -> Result:
    """
    Perform optimization using a Cooperative Coevolutionary Genetic Algorithm (CCGA).

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
    gen_type : GeneType
        Type of genome representation (GeneType.BINARY, Genetype.PERMUTATION, GeneType.REAL).
    problem : AbstractProblem
        The problem instance used to evaluate fitness.
    selection : SelectionOperator
        Function used for selection in the evolutionary algorithm.
    mins : List[float]
        List of minimum values for each gene in the chromosome (for real value optimization).
    maxs : List[float]
        List of maximum values for each gene in the chromosome (for real value optimization).

    Returns
    -------
    Result
        A Result object containing the best solution found during the optimization process,
        including its chromosome, fitness value, and generation.
    """

    pop_size = n_cols * n_rows
    best_solutions = []
    best_objectives = []
    avg_objectives = []
    vector = [0.5 for _ in range(ch_size)]
    method_name = OptimizationMethod.CCGA

    # Generate Initial Population
    pop_list = Population(method_name, ch_size, n_rows, n_cols,
                          gen_type, problem, vector, mins=mins, maxs=maxs).initial_population()

    # Sort population by fitness value
    pop_list_ordered = sorted(pop_list, key=lambda x: x.fitness_value)

    # Initialize tracking of best solutions
    best_solutions.append(pop_list_ordered[0].chromosome)
    best_objectives.append(pop_list_ordered[0].fitness_value)
    best_ever_solution = Result(
        chromosome=pop_list_ordered[0].chromosome,
        fitness_value=pop_list_ordered[0].fitness_value,
        generation_found=0
    )

    # Calculate mean fitness for the initial population
    mean = sum(map(lambda x: x.fitness_value, pop_list)) / len(pop_list)
    avg_objectives.append(mean)
    best = pop_list_ordered[0]

    # Evolutionary Algorithm Loop
    generation = 1
    while generation != n_gen + 1:
        for c in range(pop_size):
            # Select parents and determine the winner and loser
            parents = selection(pop_list, c).get_parents()
            p1, p2 = parents[0], parents[1]
            winner, loser = compete(p1, p2)

            if winner.fitness_value > best.fitness_value:
                best = winner

            # Update the vector based on the winner and loser
            update_vector(vector, winner, loser, pop_size)

            # Re-generate the population based on the updated vector
            pop_list = Population(method_name, ch_size, n_rows, n_cols,
                                  gen_type, problem, vector, mins=mins, maxs=maxs).initial_population()

        # Update best ever solution if the current best solution is better
        if best.fitness_value > best_ever_solution.fitness_value:
            best_ever_solution = Result(
                chromosome=best.chromosome,
                fitness_value=best.fitness_value,
                generation_found=generation
            )

        # Update average objectives
        mean = sum(map(lambda x: x.fitness_value, pop_list)) / len(pop_list)
        avg_objectives.append(mean)

        generation += 1

    return best_ever_solution

def mcccga(
    n_cols: int,
    n_rows: int,
    n_gen: int,
    ch_size: int,
    gen_type: str,
    problem: AbstractProblem,
    selection: SelectionOperator,
    mins: List[float],
    maxs: List[float]
) -> Result:
    """
    Optimize the given problem using a multi-population machine-coded compact genetic algorithm (MCCGA).

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
    problem : AbstractProblem
        Problem instance for fitness evaluation.
    selection : SelectionOperator
        Function or class used for selecting parents.
    mins : List[float]
        List of minimum values for the probability vector generation.
    maxs : List[float]
        List of maximum values for the probability vector generation.

    Returns
    -------
    Result
        A Result instance containing the best solution found during optimization,
        including its chromosome, fitness value, and generation found.
    """

    pop_size = n_cols * n_rows
    best_objectives = []
    avg_objectives = []
    method_name = OptimizationMethod.MCCCGA

    # Generate initial probability vector
    vector = generate_probability_vector(mins, maxs, pop_size)

    # Generate Initial Population
    pop_list = Population(method_name, ch_size, n_rows, n_cols,
                          gen_type, problem, vector).initial_population()

    # Sort population by fitness value
    pop_list_ordered = sorted(pop_list, key=lambda x: x.fitness_value)

    # Track the best solution in the initial population
    best_objectives.append(pop_list_ordered[0].fitness_value)
    best_byte_ch = byte_operators.bits_to_floats(pop_list_ordered[0].chromosome)
    best_ever_solution = Result(
        chromosome=best_byte_ch,
        fitness_value=pop_list_ordered[0].fitness_value,
        generation_found=1
    )

    # Calculate the mean fitness for the initial population
    mean = sum(map(lambda x: x.fitness_value, pop_list)) / len(pop_list)
    avg_objectives.append(mean)
    best = pop_list_ordered[0]

    # Evolutionary Algorithm Loop
    generation = 1
    while generation != n_gen + 1:
        for c in range(pop_size):

            # Select parents from the population
            parents = selection(pop_list, c).get_parents()
            p1, p2 = parents[0], parents[1]

            # Compete parents and identify the winner and loser
            winner, loser = compete(p1, p2)
            if winner.fitness_value < best.fitness_value:
                best = winner

            # Update the probability vector based on the competition result
            update_vector(vector, winner, loser, pop_size)

        # Re-generate the population based on the updated vector
        pop_list = Population(method_name, ch_size, n_rows, n_cols,
                              gen_type, problem, vector).initial_population()

        # Track the best fitness value and update the best solution if necessary
        best_objectives.append(best.fitness_value)
        best_byte_ch = byte_operators.bits_to_floats(pop_list_ordered[0].chromosome)

        if best.fitness_value < best_ever_solution.fitness_value:
            best_ever_solution = Result(
                chromosome=best_byte_ch,
                fitness_value=best.fitness_value,
                generation_found=generation
            )

        # Calculate the mean fitness for the current generation
        mean = sum(map(lambda x: x.fitness_value, pop_list)) / len(pop_list)
        avg_objectives.append(mean)
        best_byte_ch = byte_operators.bits_to_floats(best.chromosome)

        generation += 1

    # Evaluate the final solution sampled from the probability vector
    best_byte_ch = byte_operators.bits_to_floats(sample(vector))
    best_byte_result = problem.f(best_byte_ch)

    # Update the best-ever solution if the sampled solution is better
    if best_byte_result <= best_ever_solution.fitness_value:
        best_ever_solution = Result(
            chromosome=best_byte_ch,
            fitness_value=best_byte_result,
            generation_found=generation
        )

    return best_ever_solution

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



