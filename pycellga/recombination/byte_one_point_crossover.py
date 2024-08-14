import numpy as np
from individual import Individual
from problems.abstract_problem import AbstractProblem
from typing import List
import struct
from recombination.recombination_operator import RecombinationOperator

class ByteOnePointCrossover(RecombinationOperator):
    """
    ByteOnePointCrossover operator defined in (Satman, 2013). ByteOnePointCrossover performs a 
    one-point crossover at the byte level on a pair of parent individuals to produce offspring individuals.

    Parameters
    ----------
    parents : list
        A list containing two parent individuals.
    problem : AbstractProblem
        The problem instance that provides the fitness function.
    """

    def __init__(self, parents: list, problem: AbstractProblem):
        """
        Initialize the ByteOnePointCrossover object.

        Parameters
        ----------
        parents : list
            A list containing two parent individuals.
        problem : AbstractProblem
            The problem instance that provides the fitness function.
        """
        self.parents = parents
        self.problem = problem

    def get_recombinations(self) -> List[Individual]:
        """
        Perform the one-point crossover on the parent individuals at the byte level to produce offspring.

        Returns
        -------
        List[Individual]
            A list containing the offspring individuals.
        """
        offsprings = []
        child_ch1 = []
        child_ch2 = []
        p1 = self.parents[0]
        p2 = self.parents[1]

        for k in range(len(p1.chromosome)):
            # Convert the k-th gene of the parents to bytes
            p1_byte_ch = list(struct.pack("d", p1.chromosome[k]))
            p2_byte_ch = list(struct.pack("d", p2.chromosome[k]))

            # Determine crossover point
            co_point = np.random.randint(1, len(p1_byte_ch))

            # Segment the bytes at the crossover point
            p1_seg1 = p1_byte_ch[0:co_point]
            p1_seg2 = p1_byte_ch[co_point:]

            p2_seg1 = p2_byte_ch[0:co_point]
            p2_seg2 = p2_byte_ch[co_point:]

            # First child
            new_chromosome_1_part = p1_seg1 + p2_seg2
            child_part_byte_1 = bytearray(new_chromosome_1_part)
            child_part_float_1 = struct.unpack("d", child_part_byte_1)[0]
            child_ch1.append(round(child_part_float_1, 5))

            # Second child
            new_chromosome_2_part = p1_seg2 + p2_seg1
            child_part_byte_2 = bytearray(new_chromosome_2_part)
            child_part_float_2 = struct.unpack("d", child_part_byte_2)[0]
            child_ch2.append(round(child_part_float_2, 5))

        # Create the first child individual
        child_1 = Individual()
        child_1.position = p1.position
        child_1.neighbors_positions = p1.neighbors_positions
        child_1.fitness_value = self.problem.f(child_ch1)
        child_1.chromosome = child_ch1
        child_1.ch_size = len(child_1.chromosome)
        offsprings.append(child_1)

        # Create the second child individual
        child_2 = Individual()
        child_2.position = p2.position
        child_2.neighbors_positions = p2.neighbors_positions
        child_2.fitness_value = self.problem.f(child_ch2)
        child_2.chromosome = child_ch2
        child_2.ch_size = len(child_2.chromosome)
        offsprings.append(child_2)

        return offsprings
