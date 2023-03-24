
import numpy as np
from individual import *
from problems.abstract_problem import AbstractProblem


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
