
import numpy as np
from individual import *
from problems.abstract_problem import AbstractProblem
from typing import List

"""
    The Two-Point crossover operator is a genetic algorithm technique used to create offspring 
    by recombining segments from two parent solutions. Two crossover points are randomly chosen 
    along the length of the parent genomes. The segments between these two points are exchanged 
    between the parents to form the offspring. This method ensures that the offspring inherit 
    large contiguous blocks of genes from each parent, preserving the gene order and structure. 
    Two-Point crossover is effective for maintaining genetic diversity and creating offspring 
    with a good balance of traits from both parents, which can enhance the exploration of the 
    solution space and lead to improved optimization results.
"""

class TwoPointCrossover:
    def __init__(self, parents: list, problem: AbstractProblem):
        self.parents = parents
        self.problem = problem

    def get_recombinations(self) -> List[Individual]:

        offsprings = []
        p1 = self.parents[0]
        p2 = self.parents[1]

        parameter = len(p1.chromosome) * 0.20
        min_co = parameter
        max_co = len(p1.chromosome) - (parameter - 1)

        co_point_1 = np.random.randint(min_co, max_co)
        co_point_2 = np.random.randint(min_co, max_co)

        P1_seg_1 = p1.chromosome[0:co_point_1]
        P1_seg_2 = p1.chromosome[co_point_1: len(p1.chromosome)]

        P2_seg_1 = p2.chromosome[0:co_point_2]
        P2_seg_2 = p2.chromosome[co_point_2: len(p2.chromosome)]

        seg_1_aux = list(p2.chromosome)
        seg_2_aux = list(p1.chromosome)

        # First child
        rand_number = np.random.rand()

        if rand_number < 0.5:

            for i in range(len(P1_seg_1)):
                seg_1_aux.remove(P1_seg_1[i])

            new_chromosome_1 = P1_seg_1 + seg_1_aux
        else:
            for i in range(len(P1_seg_2)):
                seg_1_aux.remove(P1_seg_2[i])

            new_chromosome_1 = seg_1_aux + P1_seg_2

        
        child_1 = Individual()
        child_1.chromosome = new_chromosome_1
        child_1.ch_size = len(new_chromosome_1)

        child_1.position = p1.position
        child_1.neighbors_positions = p1.neighbors_positions
        child_1.fitness_value = self.problem.f(child_1.chromosome)
        offsprings.append(child_1)

        # Second child
        rand_number = np.random.rand()

        if rand_number < 0.5:

            for i in range(len(P2_seg_1)):
                seg_2_aux.remove(P2_seg_1[i])

            new_chromosome_2 = P2_seg_1 + seg_2_aux

        else:
            for i in range(len(P2_seg_2)):
                seg_2_aux.remove(P2_seg_2[i])

            new_chromosome_2 = seg_2_aux + P2_seg_2

        
        child_2 = Individual()
        child_2.chromosome = new_chromosome_2
        child_2.ch_size = len(new_chromosome_2)

        child_2.position = p2.position
        child_2.neighbors_positions = p2.neighbors_positions
        child_2.fitness_value = self.problem.f(child_2.chromosome)
        offsprings.append(child_2)

        return offsprings
