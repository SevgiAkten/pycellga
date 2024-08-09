import numpy as np
from individual import *
from problems.abstract_problem import AbstractProblem
from mutation.mutation_operator import MutationOperator

class InsertionMutation(MutationOperator):
    """
    InsertionMutation performs an insertion mutation on an individual's chromosome in a Genetic Algorithm.

    Parameters
    ----------
    mutation_cand : Individual, optional
        The candidate individual to be mutated (default is None).
    problem : AbstractProblem, optional
        The problem instance that provides the fitness function (default is None).
    """

    def __init__(self, mutation_cand: Individual = None, problem: AbstractProblem = None):
        """
        Initialize the InsertionMutation object.

        Parameters
        ----------
        mutation_cand : Individual, optional
            The candidate individual to be mutated (default is None).
        problem : AbstractProblem, optional
            The problem instance that provides the fitness function (default is None).
        """
        self.mutation_cand = mutation_cand
        self.problem = problem

    def mutate(self) -> Individual:
        """
        Perform an insertion mutation on the candidate individual.

        A gene in the candidate's chromosome is randomly selected and moved to a new position in the chromosome.

        Returns
        -------
        Individual
            A new individual with the mutated chromosome.
        """
        # Convert the chromosome to a list to allow mutation
        mutated_ch = list(self.mutation_cand.chromosome)

        # Randomly select two distinct indices in the chromosome
        ran_1 = np.random.randint(0, len(mutated_ch))
        ran_2 = np.random.randint(0, len(mutated_ch))
        while ran_1 == ran_2:
            ran_2 = np.random.randint(0, len(mutated_ch))

        # Remove the gene at the first index and insert it at the second index
        x = mutated_ch[ran_1]
        mutated_ch_new = list(mutated_ch)
        mutated_ch_new.remove(x)
        mutated_ch_new.insert(ran_2, x)

        # Create a new Individual with the mutated chromosome
        mutated = Individual()
        mutated.chromosome = mutated_ch_new
        mutated.ch_size = len(mutated_ch_new)
        mutated.position = self.mutation_cand.position
        mutated.neighbors_positions = self.mutation_cand.neighbors_positions
        mutated.fitness_value = self.problem.f(mutated.chromosome)

        return mutated
