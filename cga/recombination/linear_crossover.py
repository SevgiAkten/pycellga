
import random
from individual import *
from problems.abstract_problem import AbstractProblem
from typing import List

"""
    The Linear crossover operator is a method used in genetic algorithms to generate 
    offspring by creating linear combinations of the parent solutions. Typically, this 
    involves selecting two or more coefficients that sum to one and using them to 
    weight the parent solutions, resulting in offspring that are convex combinations of 
    the parents. This approach allows for smooth interpolation between parent solutions, 
    maintaining genetic diversity while facilitating the exploration of the solution 
    space. Linear crossover is particularly useful in continuous optimization problems, 
    as it can produce offspring that lie within the convex hull defined by the parent 
    solutions, potentially leading to better and more robust solutions.
"""

class LinearCrossover:
    def __init__(self, parents: list, problem: AbstractProblem):
        self.parents = parents
        self.problem = problem

    def combine(self, p1: Individual, p2: Individual, locationsource: Individual) -> Individual:
        chsize = len(p1.chromosome)
        child1_ch = [0 for i in range(chsize)]
        child2_ch = [0 for i in range(chsize)]
        child3_ch = [0 for i in range(chsize)]

        for i in range(chsize):
            p1_allele = p1.chromosome[i]
            p2_allele = p2.chromosome[i]

            child1_ch[i] = round(0.5*p1_allele + 0.5*p2_allele, 5)
            child2_ch[i] = round(3*p1_allele/2 - 0.5*p2_allele, 5)
            child3_ch[i] = round(-0.5*p1_allele + 3*p2_allele/2, 5)

        chosed_ch = random.randint(1, 4)
        if (chosed_ch == 1):
            chosed_child_ch = child1_ch
        elif (chosed_ch == 2):
            chosed_child_ch = child2_ch
        elif (chosed_ch == 3):
            chosed_child_ch = child3_ch

        indv = Individual(p1.gen_type, p1.ch_size)
        indv.position = locationsource.position
        indv.neighbors_positions = locationsource.neighbors_positions
        indv.chromosome = list(chosed_child_ch)
        indv.fitness_value = self.problem.f(chosed_child_ch)
        return indv

    def get_recombinations(self) -> List[Individual]:

        p1 = self.parents[0]
        p2 = self.parents[1]

        return [
            self.combine(p1, p2, p1),
            self.combine(p1, p2, p2)
        ]
