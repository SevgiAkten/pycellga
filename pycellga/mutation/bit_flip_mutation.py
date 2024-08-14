import numpy as np
from individual import *
from problems.abstract_problem import AbstractProblem
from mutation.mutation_operator import MutationOperator

class BitFlipMutation(MutationOperator):
    """
    BitFlipMutation performs a bit flip mutation on an individual in a Genetic Algorithm.

    Parameters
    ----------
    mutation_cand : Individual, optional
        The candidate individual to be mutated (default is None).
    problem : AbstractProblem, optional
        The problem instance that provides the fitness function (default is None).
    """

    def __init__(self, mutation_cand: Individual = None, problem: AbstractProblem = None):
        """
        Initialize the BitFlipMutation object.

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
        Perform a bit flip mutation on the candidate individual.

        A single bit in the candidate's chromosome is randomly selected and flipped
        (i.e., a 0 is changed to a 1, or a 1 is changed to a 0).

        Returns
        -------
        Individual
            A new individual with the mutated chromosome.
        """
        # Convert the chromosome to a list to allow mutation
        m_ch = list(self.mutation_cand.chromosome)
        
        # Randomly select an index in the chromosome
        index = np.random.randint(0, len(m_ch))
        
        # Flip the bit at the selected index
        if m_ch[index] == 0:
            m_ch[index] = 1
        else:
            m_ch[index] = 0

        # Create a new Individual with the mutated chromosome
        mutated = Individual()
        mutated.chromosome = m_ch
        mutated.ch_size = len(m_ch)
        mutated.position = self.mutation_cand.position
        mutated.neighbors_positions = self.mutation_cand.neighbors_positions
        mutated.fitness_value = self.problem.f(mutated.chromosome)

        return mutated
