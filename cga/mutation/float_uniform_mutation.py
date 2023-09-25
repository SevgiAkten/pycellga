import random
from individual import *
from problems.abstract_problem import AbstractProblem

# for real-valued problems


class FloatUniformMutation:
    def __init__(self, mutation_cand: Individual = None, problem: AbstractProblem = None):
        self.mutation_cand = mutation_cand
        self.problem = problem

    def mutate(self) -> Individual:

        m_ch = list(self.mutation_cand.chromosome)

        for i in range(len(m_ch)):
            rnd = random.uniform(0, 1)
            if (rnd < 0.5):
                m_ch[i] = round(m_ch[i] - rnd, 3)
            else:
                m_ch[i] = round(m_ch[i] + rnd, 3)

        mutated_ch_new = list(m_ch)
        mutated = Individual()

        mutated.chromosome = mutated_ch_new
        mutated.ch_size = len(mutated_ch_new)
        mutated.position = self.mutation_cand.position
        mutated.neighbors_positions = self.mutation_cand.neighbors_positions
        mutated.fitness_value = self.problem.f(mutated.chromosome)

        return mutated
