
import numpy.random as randomgenerator
from individual import *
from problems.abstract_problem import AbstractProblem
from typing import List
import struct

"""
    Byte Uniform crossover operator defined in (Satman, 2013). 
    The Byte Uniform crossover operator is a method used in genetic algorithms 
    to create new offspring by uniformly combining bytes from two parent solutions. 
    In this operator, each byte position in the offspring is chosen randomly from 
    one of the corresponding bytes in the parent solutions with equal probability. 
    This technique ensures that the genetic material from both parents is evenly 
    represented in the offspring, promoting genetic diversity and allowing for
    a thorough exploration of the solution space. Byte Uniform crossover is particularly 
    useful when working with byte-level data representations, providing a straightforward 
    yet effective means of recombining parent solutions.
"""

class ByteUniformCrossover:
    def __init__(self, parents: list, problem: AbstractProblem):
        self.parents = parents
        self.problem = problem

    def combine(self, p1: Individual, p2: Individual, locationsource: Individual) -> Individual:

        child_ch = []
        for k in range(len(p1.chromosome)):
            p1_byte_ch = list(struct.pack("d", p1.chromosome[k]))
            p2_byte_ch = list(struct.pack("d", p2.chromosome[k]))

            chsize = len(p1_byte_ch)
            child_part = [0 for i in range(len(p1_byte_ch))]
            for i in range(chsize):
                if randomgenerator.rand() < 0.5:
                    child_part[i] = p1_byte_ch[i]
                else:
                    child_part[i] = p2_byte_ch[i]

            child_part_byte = bytearray(child_part)
            child_part_float = list(struct.unpack("d", child_part_byte))

            child_ch.append(round(child_part_float[0], 5))

        indv = Individual(p1.gen_type, p1.ch_size)
        indv.position = locationsource.position
        indv.neighbors_positions = locationsource.neighbors_positions
        indv.chromosome = list(child_ch)
        indv.fitness_value = self.problem.f(child_ch)
        return indv

    def get_recombinations(self) -> List[Individual]:

        p1 = self.parents[0]
        p2 = self.parents[1]

        return [
            self.combine(p1, p2, p1),
            self.combine(p1, p2, p2)
        ]
