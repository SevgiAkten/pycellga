
import random
from individual import *
from problems.abstract_problem import AbstractProblem
from typing import List


class LinearCrossover:
    def __init__(self, parents: list, problem: AbstractProblem):
        self.parents = parents
        self.problem = problem

    def combine(self, p1: Individual, p2: Individual, locationsource: Individual) -> Individual:
        chsize = len(p1.chromosome)
        child1_ch = [0 for i in range(chsize)]
        child2_ch = [0 for i in range(chsize)]
        child3_ch = [0 for i in range(chsize)]
        fitness1 = 0.0
        fitness2 = 0.0
        fitness3 = 0.0

        for i in range(chsize):
            p1_allele = p1.chromosome[i]
            p2_allele = p2.chromosome[i]

            child1_ch[i] = round(0.5*p1_allele + 0.5*p2_allele, 3)
            child2_ch[i] = round(3*p1_allele/2 - 0.5*p2_allele, 3)
            child3_ch[i] = round(-0.5*p1_allele + 3*p2_allele/2, 3)

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
