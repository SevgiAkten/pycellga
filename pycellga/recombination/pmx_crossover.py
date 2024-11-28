from individual import *
from problems.abstract_problem import AbstractProblem
from typing import List
from recombination.recombination_operator import RecombinationOperator

class PMXCrossover(RecombinationOperator):
    """
    PMXCrossover performs Partially Mapped Crossover (PMX) on a pair of parent individuals
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
        Initialize the PMXCrossover object.

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
        Perform the PMX crossover on the parent individuals to produce offspring.

        Returns
        -------
        List[Individual]
            A list containing the offspring individuals.
        """
        offsprings = []
        p1 = self.parents[0]
        p2 = self.parents[1]

        co_point_1 = 15
        co_point_2 = 35

        p1_seg_main = list(p1.chromosome[co_point_1:co_point_2])
        p1_seg_left = list(p1.chromosome[0:co_point_1])
        p1_seg_right = list(p1.chromosome[co_point_2:])
        p1_seg_left_aux = list()
        p1_seg_right_aux = list()

        p2_seg_main = list(p2.chromosome[co_point_1:co_point_2])
        p2_seg_left = list(p2.chromosome[0:co_point_1])
        p2_seg_right = list(p2.chromosome[co_point_2:])
        p2_seg_left_aux = list()
        p2_seg_right_aux = list()

        # First child
        child_1 = Individual()

        for seg in p1_seg_left:
            if seg in p2_seg_main:
                mapping_index = p2_seg_main.index(seg)
                mapping_item = p1_seg_main[mapping_index]
                while mapping_item in p2_seg_main:
                    mapping_index = p2_seg_main.index(mapping_item)
                    mapping_item = p1_seg_main[mapping_index]
                p1_seg_left_aux.append(mapping_item)
            else:
                p1_seg_left_aux.append(seg)

        for seg in p1_seg_right:
            if seg in p2_seg_main:
                mapping_index = p2_seg_main.index(seg)
                mapping_item = p1_seg_main[mapping_index]
                while mapping_item in p2_seg_main:
                    mapping_index = p2_seg_main.index(mapping_item)
                    mapping_item = p1_seg_main[mapping_index]
                p1_seg_right_aux.append(mapping_item)
            else:
                p1_seg_right_aux.append(seg)

        child_1_ch = p1_seg_left_aux + p2_seg_main + p1_seg_right_aux

        child_1.chromosome = child_1_ch
        child_1.ch_size = len(child_1_ch)
        child_1.position = p1.position
        child_1.neighbors_positions = p1.neighbors_positions
        child_1.fitness_value = self.problem.f(child_1.chromosome)
        offsprings.append(child_1)

        # Second child
        child_2 = Individual()

        for seg in p2_seg_left:
            if seg in p1_seg_main:
                mapping_index = p1_seg_main.index(seg)
                mapping_item = p2_seg_main[mapping_index]
                while mapping_item in p1_seg_main:
                    mapping_index = p1_seg_main.index(mapping_item)
                    mapping_item = p2_seg_main[mapping_index]
                p2_seg_left_aux.append(mapping_item)
            else:
                p2_seg_left_aux.append(seg)

        for seg in p2_seg_right:
            if seg in p1_seg_main:
                mapping_index = p1_seg_main.index(seg)
                mapping_item = p2_seg_main[mapping_index]
                while mapping_item in p1_seg_main:
                    mapping_index = p1_seg_main.index(mapping_item)
                    mapping_item = p2_seg_main[mapping_index]
                p2_seg_right_aux.append(mapping_item)
            else:
                p2_seg_right_aux.append(seg)

        child_2_ch = p2_seg_left_aux + p1_seg_main + p2_seg_right_aux

        child_2.chromosome = child_2_ch
        child_2.ch_size = len(child_2_ch)
        child_2.position = p2.position
        child_2.neighbors_positions = p2.neighbors_positions
        child_2.fitness_value = self.problem.f(child_2.chromosome)
        offsprings.append(child_2)

        return offsprings
