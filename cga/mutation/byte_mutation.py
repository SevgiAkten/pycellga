
import numpy as np
from individual import *
from problems.abstract_problem import AbstractProblem
import struct

# for real-valued problems


class ByteMutation:
    def __init__(self, mutation_cand: Individual = None, problem: AbstractProblem = None):
        self.mutation_cand = mutation_cand
        self.problem = problem

    def mutate(self) -> Individual:

        m_ch = list(self.mutation_cand.chromosome)

        index = np.random.randint(0, len(m_ch))
        m_byte_ch = list(struct.pack("d", m_ch[index]))

        rnd_index = np.random.randint(0, len(m_byte_ch))
        mutant = m_byte_ch[rnd_index]

        u = np.random.uniform(0, 1)

        if u < 0.5:
            mutant += 1
        else:
            mutant -= 1
        if mutant > 255:
            mutant = 0
        elif mutant < 0:
            mutant = 255

        m_byte_ch[rnd_index] = mutant

        mutatnt_part_byte = bytearray(m_byte_ch)
        mutant_part_float = list(struct.unpack("d", mutatnt_part_byte))
        m_ch[index] = round(mutant_part_float[0], 3)
        mutated = Individual()

        mutated.chromosome = m_ch
        mutated.ch_size = len(m_ch)
        mutated.position = self.mutation_cand.position
        mutated.neighbors_positions = self.mutation_cand.neighbors_positions
        mutated.fitness_value = self.problem.f(mutated.chromosome)

        return mutated
