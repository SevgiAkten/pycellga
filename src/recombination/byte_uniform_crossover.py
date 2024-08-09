import numpy.random as randomgenerator
from individual import *
from problems.abstract_problem import AbstractProblem
from typing import List
import struct
from recombination.recombination_operator import RecombinationOperator

class ByteUniformCrossover(RecombinationOperator):
    """
    ByteUniformCrossover operator defined in (Satman, 2013). ByteUniformCrossover performs a 
    uniform crossover at the byte level on a pair of parent individuals to produce offspring individuals.

    Parameters
    ----------
    parents : list
        A list containing two parent individuals.
    problem : AbstractProblem
        The problem instance that provides the fitness function.
    """

    def __init__(self, parents: list, problem: AbstractProblem):
        """
        Initialize the ByteUniformCrossover object.

        Parameters
        ----------
        parents : list
            A list containing two parent individuals.
        problem : AbstractProblem
            The problem instance that provides the fitness function.
        """
        self.parents = parents
        self.problem = problem

    def combine(self, p1: Individual, p2: Individual, locationsource: Individual) -> Individual:
        """
        Combine two parent individuals using uniform crossover at the byte level to produce a single offspring.

        Parameters
        ----------
        p1 : Individual
            The first parent individual.
        p2 : Individual
            The second parent individual.
        locationsource : Individual
            The individual from which to copy positional information for the offspring.

        Returns
        -------
        Individual
            The resulting offspring individual.
        """
        child_ch = []
        for k in range(len(p1.chromosome)):
            # Convert the k-th gene of the parents to bytes
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
        """
        Perform the uniform crossover on the parent individuals to produce offspring.

        Returns
        -------
        List[Individual]
            A list containing the offspring individuals.
        """
        p1 = self.parents[0]
        p2 = self.parents[1]

        return [
            self.combine(p1, p2, p1),
            self.combine(p1, p2, p2)
        ]
