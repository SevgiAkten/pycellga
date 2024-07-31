
import numpy as np
from individual import *
from problems.abstract_problem import AbstractProblem

"""
    The Bit Flip Mutation operator is a genetic algorithm technique used to introduce random 
    changes in binary-encoded solutions by flipping individual bits. During mutation, each bit 
    in a binary string is independently flipped (i.e., changed from 0 to 1 or from 1 to 0) with 
    a given probability. This method introduces genetic diversity by randomly altering the genetic 
    material of the solutions, which helps in exploring new areas of the solution space and 
    preventing premature convergence to local optima. Bit Flip Mutation is particularly effective 
    in problems where solutions are represented as binary strings, as it provides a straightforward 
    mechanism for introducing variability and maintaining diversity within the population.
"""


class BitFlipMutation:
    def __init__(self, mutation_cand: Individual = None, problem: AbstractProblem = None):
        self.mutation_cand = mutation_cand
        self.problem = problem

    def mutate(self) -> Individual:

        m_ch = list(self.mutation_cand.chromosome)
        index = np.random.randint(0, len(m_ch))
        if m_ch[index] == 0:
            m_ch[index] = 1
        else:
            m_ch[index] = 0

        mutated = Individual()

        mutated.chromosome = m_ch
        mutated.ch_size = len(m_ch)
        mutated.position = self.mutation_cand.position
        mutated.neighbors_positions = self.mutation_cand.neighbors_positions
        mutated.fitness_value = self.problem.f(mutated.chromosome)

        return mutated
