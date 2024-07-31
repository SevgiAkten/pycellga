
import numpy as np
from individual import *
from problems.abstract_problem import AbstractProblem
import struct

"""
    Byte Mutation Random operator defined in (Satman, 2013).
    The Byte Mutation Random operator is a genetic algorithm technique designed to introduce 
    variability into byte-encoded solutions by randomly modifying individual bytes. During 
    mutation, each byte in a byte string is selected with a certain probability, and its value 
    is randomly changed to a new value within the possible byte range (0-255). This method ensures that 
    the genetic material of the solutions is altered in a stochastic manner, promoting exploration 
    of the solution space and reducing the risk of premature convergence. Byte Mutation Random is 
    especially useful for problems involving byte-level data representation, as it provides a 
    controlled way to introduce genetic diversity and maintain a balance between exploration and 
    exploitation in the evolutionary process.
"""


class ByteMutationRandom:
    def __init__(self, mutation_cand: Individual = None, problem: AbstractProblem = None):
        self.mutation_cand = mutation_cand
        self.problem = problem

    def mutate(self) -> Individual:

        m_ch = list(self.mutation_cand.chromosome)

        index = np.random.randint(0, len(m_ch))
        m_byte_ch = list(struct.pack("d", m_ch[index]))

        rnd_index = np.random.randint(0, len(m_byte_ch))

        mutant = np.random.randint(0, 256)

        m_byte_ch[rnd_index] = mutant

        mutatnt_part_byte = bytearray(m_byte_ch)
        mutant_part_float = list(struct.unpack("d", mutatnt_part_byte))
        m_ch[index] = round(mutant_part_float[0], 5)
        mutated = Individual()

        mutated.chromosome = m_ch
        mutated.ch_size = len(m_ch)
        mutated.position = self.mutation_cand.position
        mutated.neighbors_positions = self.mutation_cand.neighbors_positions
        mutated.fitness_value = self.problem.f(mutated.chromosome)

        return mutated
