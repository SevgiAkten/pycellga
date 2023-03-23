from individual import *
from problems.abstract_problem import AbstractProblem
from typing import List

# Partially-mapped crossover (PMX)


class PMXCrossover:
    def __init__(self, parents: list, problem: AbstractProblem):
        self.parents = parents
        self.problem = problem

    def get_recombinations(self) -> List[Individual]:

        offsprings = []
        p1 = self.parents[0]
        p2 = self.parents[1]

        co_point_1 = 15
        co_point_2 = 35

        p1_seg_main = list(p1.chromosome[co_point_1:co_point_2])
        p1_seg_left = list(p1.chromosome[0:co_point_1])
        p1_seg_right = list(p1.chromosome[co_point_2:])

        p2_seg_main = list(p2.chromosome[co_point_1:co_point_2])
        p2_seg_left = list(p2.chromosome[0:co_point_1])
        p2_seg_right = list(p2.chromosome[co_point_2:])

        # First child
        child_1 = Individual()
        child_1_aux = p1_seg_left + p2_seg_main + p1_seg_right

        for i in range(len(p1_seg_left)):
            if p1_seg_left[i] in p2_seg_main + p1_seg_right:
                mapping_index = p2_seg_main.index(p1_seg_left[i])
                mapping_item = p1_seg_main[mapping_index]
                if (mapping_item in child_1_aux):
                    mapping_index = p2_seg_main.index(mapping_item)
                    mapping_item = p1_seg_main[mapping_index]
                p1_seg_left[i] = mapping_item

        for i in range(len(p1_seg_right)):
            if p1_seg_right[i] in p2_seg_main + p1_seg_left:
                mapping_index = p2_seg_main.index(p1_seg_right[i])
                mapping_item = p1_seg_main[mapping_index]
                if (mapping_item in child_1_aux):
                    mapping_index = p2_seg_main.index(mapping_item)
                    mapping_item = p1_seg_main[mapping_index]
                p1_seg_right[i] = mapping_item

        child_1_ch = p1_seg_left + p2_seg_main + p1_seg_right

        child_1.chromosome = child_1_ch
        child_1.ch_size = len(child_1_ch)

        child_1.position = p1.position
        child_1.neighbors_positions = p1.neighbors_positions
        child_1.fitness_value = self.problem.f(child_1.chromosome)
        offsprings.append(child_1)

        # Second child
        child_2 = Individual()
        child_2_aux = p2_seg_left + p1_seg_main + p2_seg_right

        for i in range(len(p2_seg_left)):
            if p2_seg_left[i] in p1_seg_main + p2_seg_right:
                mapping_index = p1_seg_main.index(p2_seg_left[i])
                mapping_item = p2_seg_main[mapping_index]
                if (mapping_item in child_2_aux):
                    mapping_index = p1_seg_main.index(mapping_item)
                    mapping_item = p2_seg_main[mapping_index]
                p2_seg_left[i] = mapping_item

        for i in range(len(p2_seg_right)):
            if p2_seg_right[i] in p1_seg_main + p2_seg_left:
                mapping_index = p1_seg_main.index(p2_seg_right[i])
                mapping_item = p2_seg_main[mapping_index]
                if (mapping_item in child_2_aux):
                    mapping_index = p1_seg_main.index(mapping_item)
                    mapping_item = p2_seg_main[mapping_index]
                p2_seg_right[i] = mapping_item

        child_2_ch = p2_seg_left + p1_seg_main + p2_seg_right

        child_2.chromosome = child_2_ch
        child_2.ch_size = len(child_2_ch)

        child_2.position = p2.position
        child_2.neighbors_positions = p2.neighbors_positions
        child_2.fitness_value = self.problem.f(child_2.chromosome)

        offsprings.append(child_2)

        return offsprings
