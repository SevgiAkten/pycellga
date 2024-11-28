import numpy as np
from individual import *
from problems.abstract_problem import AbstractProblem
import struct
from mutation.mutation_operator import MutationOperator

class ByteMutationRandom(MutationOperator):
    """
    ByteMutationRandom operator defined in (Satman, 2013). ByteMutationRandom performs 
    a random byte mutation on an individual's chromosome in a Genetic Algorithm.

    Parameters
    ----------
    mutation_cand : Individual, optional
        The candidate individual to be mutated (default is None).
    problem : AbstractProblem, optional
        The problem instance that provides the fitness function (default is None).
    """

    def __init__(self, mutation_cand: Individual = None, problem: AbstractProblem = None):
        """
        Initialize the ByteMutationRandom object.

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
        Perform a random byte mutation on the candidate individual.

        A single byte in one of the candidate's chromosome's floating-point numbers is randomly selected
        and mutated to a random value.

        Returns
        -------
        Individual
            A new individual with the mutated chromosome.
        """
        # Convert the chromosome to a list to allow mutation
        m_ch = list(self.mutation_cand.chromosome)

        # Randomly select an index in the chromosome
        index = np.random.randint(0, len(m_ch))

        # Pack the selected float into bytes
        m_byte_ch = list(struct.pack("d", m_ch[index]))

        # Randomly select an index in the byte representation
        rnd_index = np.random.randint(0, len(m_byte_ch))

        # Generate a random byte
        mutant = np.random.randint(0, 256)

        # Replace the selected byte with the random byte
        m_byte_ch[rnd_index] = mutant

        # Convert the mutated byte sequence back to a float
        mutatnt_part_byte = bytearray(m_byte_ch)
        mutant_part_float = list(struct.unpack("d", mutatnt_part_byte))
        m_ch[index] = round(mutant_part_float[0], 5)

        # Create a new Individual with the mutated chromosome
        mutated = Individual()
        mutated.chromosome = m_ch
        mutated.ch_size = len(m_ch)
        mutated.position = self.mutation_cand.position
        mutated.neighbors_positions = self.mutation_cand.neighbors_positions
        mutated.fitness_value = self.problem.f(mutated.chromosome)

        return mutated
