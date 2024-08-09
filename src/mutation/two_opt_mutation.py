import numpy as np
from individual import *
from problems.abstract_problem import AbstractProblem
from mutation.mutation_operator import MutationOperator

class TwoOptMutation(MutationOperator):
    """
    TwoOptMutation performs a 2-opt mutation on an individual's chromosome in a Genetic Algorithm.

    Parameters
    ----------
    mutation_cand : Individual, optional
        The candidate individual to be mutated (default is None).
    problem : AbstractProblem, optional
        The problem instance that provides the fitness function (default is None).
    """

    def __init__(self, mutation_cand: Individual = None, problem: AbstractProblem = None):
        """
        Initialize the TwoOptMutation object.

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
        Perform a 2-opt mutation on the candidate individual.

        A segment of the candidate's chromosome is randomly selected and reversed.

        Returns
        -------
        Individual
            A new individual with the mutated chromosome.
        """
        # Convert the chromosome to a list to allow mutation
        mutated_ch = list(self.mutation_cand.chromosome)

        # Randomly select two distinct indices in the chromosome with a minimum distance between them
        ran_1 = np.random.randint(0, len(mutated_ch))
        ran_2 = np.random.randint(0, len(mutated_ch))

        while abs(ran_1 - ran_2) < 3:
            ran_2 = np.random.randint(0, len(mutated_ch))

        # Create a new list to hold the mutated chromosome
        mutated_ch_new = list(mutated_ch)

        # Reverse the segment between the two selected indices
        if ran_1 < ran_2:
            mutated_ch_new[ran_1:ran_2] = reversed(mutated_ch_new[ran_1:ran_2])
        else:
            mutated_ch_new[ran_2:ran_1] = reversed(mutated_ch_new[ran_2:ran_1])

        # Create a new Individual with the mutated chromosome
        mutated = Individual()
        mutated.chromosome = mutated_ch_new
        mutated.ch_size = len(mutated_ch_new)
        mutated.position = self.mutation_cand.position
        mutated.neighbors_positions = self.mutation_cand.neighbors_positions
        mutated.fitness_value = self.problem.f(mutated.chromosome)

        return mutated
