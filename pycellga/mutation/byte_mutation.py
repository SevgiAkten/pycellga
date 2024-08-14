import numpy as np
from individual import *
from problems.abstract_problem import AbstractProblem
import struct
from mutation.mutation_operator import MutationOperator

class ByteMutation(MutationOperator):
    """
    ByteMutation operator defined in (Satman, 2013). ByteMutation performs a byte-wise mutation 
    on an individual's chromosome in a Genetic Algorithm.

    Parameters
    ----------
    mutation_cand : Individual, optional
        The candidate individual to be mutated (default is None).
    problem : AbstractProblem, optional
        The problem instance that provides the fitness function (default is None).
    """

    def __init__(self, mutation_cand: Individual = None, problem: AbstractProblem = None):
        """
        Initialize the ByteMutation object.

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
        Perform a byte-wise mutation on the candidate individual.

        A single byte in one of the candidate's chromosome's floating-point numbers is randomly selected
        and either incremented or decremented by 1, wrapping around if necessary.

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

        # Get the byte at the selected index
        mutant = m_byte_ch[rnd_index]

        # Generate a random uniform value to decide increment or decrement
        u = np.random.uniform(0, 1)

        # Increment or decrement the byte, with wrapping
        if u < 0.5:
            mutant += 1
        else:
            mutant -= 1
        if mutant > 255:
            mutant = 0
        elif mutant < 0:
            mutant = 255

        # Replace the selected byte with the mutated byte
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
