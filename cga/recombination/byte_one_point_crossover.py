
import numpy as np
from individual import *
from problems.abstract_problem import AbstractProblem
from typing import List
import struct


class ByteOnePointCrossover:
    def __init__(self, parents: list, problem: AbstractProblem):
        self.parents = parents
        self.problem = problem

    def get_recombinations(self) -> List[Individual]:

        offsprings = []
        child_ch1 = []
        child_ch2 = []
        p1 = self.parents[0]
        p2 = self.parents[1]
        for k in range(len(p1.chromosome)):
            p1_byte_ch = list(struct.pack("d", p1.chromosome[k]))
            p2_byte_ch = list(struct.pack("d", p2.chromosome[k]))

            co_point = np.random.randint(len(p1.chromosome))

            p1_seg1 = list(p1_byte_ch[0:co_point])
            p1_seg2 = list(p1_byte_ch[co_point:])

            p2_seg1 = list(p2_byte_ch[0:co_point])
            p2_seg2 = list(p2_byte_ch[co_point:])

            # First child
            new_chromosome_1_part = p1_seg1 + p2_seg2
            child_part_byte_1 = bytearray(new_chromosome_1_part)
            child_part_float_1 = list(struct.unpack("d", child_part_byte_1))
            child_ch1.append(round(child_part_float_1[0], 3))

            # Second child
            new_chromosome_2_part = p1_seg2 + p2_seg1
            child_part_byte_2 = bytearray(new_chromosome_2_part)
            child_part_float_2 = list(struct.unpack("d", child_part_byte_2))
            child_ch2.append(round(child_part_float_2[0], 3))

        child_1 = Individual()
        child_1.position = p1.position
        child_1.neighbors_positions = p1.neighbors_positions
        child_1.fitness_value = self.problem.f(child_ch1)
        child_1.chromosome = child_ch1
        child_1.ch_size = len(child_1.chromosome)
        offsprings.append(child_1)

        child_2 = Individual()
        child_2.position = p2.position
        child_2.neighbors_positions = p2.neighbors_positions
        child_2.fitness_value = self.problem.f(child_ch2)
        child_2.chromosome = child_ch2
        child_2.ch_size = len(child_2.chromosome)
        offsprings.append(child_2)

        return offsprings
