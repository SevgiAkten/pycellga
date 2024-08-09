import numpy as np
from individual import *
from problems.abstract_problem import AbstractProblem
from typing import List
from recombination.recombination_operator import RecombinationOperator


class OnePointCrossover(RecombinationOperator):
    """
    OnePointCrossover performs a one-point crossover on a pair of parent individuals
    to produce offspring individuals.

    Parameters
    ----------
    parents : list
        A list containing two parent individuals.
    problem : AbstractProblem
        The problem instance that provides the fitness function.
    """

    def __init__(self, parents: list, problem: AbstractProblem):
        """
        Initialize the OnePointCrossover object.

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
        Perform the one-point crossover on the parent individuals to produce offspring.

        Returns
        -------
        List[Individual]
            A list containing the offspring individuals.
        """
        offsprings = []
        p1 = self.parents[0]
        p2 = self.parents[1]

        # Determine crossover point
        co_point = np.random.randint(len(p1.chromosome))

        # Segment the chromosomes at the crossover point
        p1_seg1 = list(p1.chromosome[0:co_point])
        p1_seg2 = list(p1.chromosome[co_point:])
        p2_seg1 = list(p2.chromosome[0:co_point])
        p2_seg2 = list(p2.chromosome[co_point:])

        # Create the first child
        child_1 = Individual()
        new_chromosome_1 = p1_seg1 + p2_seg2
        child_1.chromosome = new_chromosome_1
        child_1.ch_size = len(new_chromosome_1)
        child_1.position = p1.position
        child_1.neighbors_positions = p1.neighbors_positions
        child_1.fitness_value = self.problem.f(child_1.chromosome)
        offsprings.append(child_1)

        # Create the second child
        child_2 = Individual()
        new_chromosome_2 = p1_seg2 + p2_seg1
        child_2.chromosome = new_chromosome_2
        child_2.ch_size = len(new_chromosome_2)
        child_2.position = p2.position
        child_2.neighbors_positions = p2.neighbors_positions
        child_2.fitness_value = self.problem.f(child_2.chromosome)
        offsprings.append(child_2)

        return offsprings
