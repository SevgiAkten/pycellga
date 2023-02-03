import numpy as np
from Individual import *
from Problems.Combinatorial.OneMax import *


class BitFlipMutation:
    def __init__(self, mutation_cand):
        self.mutation_cand = mutation_cand

    def mutate(self):

        m_ch = list(self.mutation_cand.chromosome)
        index = np.random.randint(0, len(m_ch))
        if m_ch[index] == 0:
            m_ch[index] = 1
        else:
            m_ch[index] = 0

        mutated = Individual()

        mutated.chromosome = m_ch
        mutated.position = self.mutation_cand.position
        mutated.neighbors_positions = self.mutation_cand.neighbors_positions
        mutated.fitness_value = OneMax(mutated.chromosome).evalOneMax()

        return mutated
