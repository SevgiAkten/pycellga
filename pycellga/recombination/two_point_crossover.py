import numpy as np
from individual import Individual
from problems.abstract_problem import AbstractProblem
from typing import List
from recombination.recombination_operator import RecombinationOperator

class TwoPointCrossover(RecombinationOperator):
    """
    TwoPointCrossover performs a two-point crossover on a pair of parent individuals
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
        Initialize the TwoPointCrossover object.

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
        Perform the two-point crossover on the parent individuals to produce offspring.

        Returns
        -------
        List[Individual]
            A list containing the offspring individuals.
        """
        offsprings = []
        p1 = self.parents[0]
        p2 = self.parents[1]

        parameter = len(p1.chromosome) * 0.20
        min_co = int(parameter)
        max_co = len(p1.chromosome) - (int(parameter) - 1)

        co_point_1 = np.random.randint(min_co, max_co)
        co_point_2 = np.random.randint(min_co, max_co)

        if co_point_1 > co_point_2:
            co_point_1, co_point_2 = co_point_2, co_point_1

        P1_seg_1 = p1.chromosome[0:co_point_1]
        P1_seg_2 = p1.chromosome[co_point_1:co_point_2]
        P1_seg_3 = p1.chromosome[co_point_2:]

        P2_seg_1 = p2.chromosome[0:co_point_1]
        P2_seg_2 = p2.chromosome[co_point_1:co_point_2]
        P2_seg_3 = p2.chromosome[co_point_2:]

        child_1_chromosome = P1_seg_1 + P2_seg_2 + P1_seg_3
        child_2_chromosome = P2_seg_1 + P1_seg_2 + P2_seg_3

        child_1 = Individual()
        child_1.chromosome = child_1_chromosome
        child_1.ch_size = len(child_1_chromosome)
        child_1.position = p1.position
        child_1.neighbors_positions = p1.neighbors_positions
        child_1.fitness_value = self.problem.f(child_1.chromosome)
        offsprings.append(child_1)

        child_2 = Individual()
        child_2.chromosome = child_2_chromosome
        child_2.ch_size = len(child_2_chromosome)
        child_2.position = p2.position
        child_2.neighbors_positions = p2.neighbors_positions
        child_2.fitness_value = self.problem.f(child_2.chromosome)
        offsprings.append(child_2)

        return offsprings
