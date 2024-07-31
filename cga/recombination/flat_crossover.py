
import random
from individual import *
from problems.abstract_problem import AbstractProblem
from typing import List

"""
    The Flat crossover operator is used in genetic algorithms to generate offspring by 
    selecting random values within the range defined by the parent solutions. For each 
    gene, the offspring gene is chosen randomly from a uniform distribution between the 
    minimum and maximum values of the corresponding parent genes. This method is 
    particularly effective for continuous optimization problems, as it allows offspring 
    to explore the entire range between the parent solutions, promoting genetic 
    diversity and enabling the discovery of new and potentially better solutions.
"""


class FlatCrossover:
    def __init__(self, parents: list, problem: AbstractProblem):
        self.parents = parents
        self.problem = problem

    def combine(self, p1: Individual, p2: Individual, locationsource: Individual) -> Individual:
        chsize = len(p1.chromosome)
        child = [0 for i in range(chsize)]
        for i in range(chsize):
            p1_allele = p1.chromosome[i]
            p2_allele = p2.chromosome[i]

            if (p1_allele > p2_allele):
                c_max = p1_allele
                c_min = p2_allele
            else:
                c_max = p2_allele
                c_min = p1_allele
            new_allele = random.uniform(c_min, c_max)
            child[i] = round(new_allele, 5)

        indv = Individual(p1.gen_type, p1.ch_size)
        indv.position = locationsource.position
        indv.neighbors_positions = locationsource.neighbors_positions
        indv.chromosome = list(child)
        indv.fitness_value = self.problem.f(child)
        return indv

    def get_recombinations(self) -> List[Individual]:

        p1 = self.parents[0]
        p2 = self.parents[1]

        return [
            self.combine(p1, p2, p1),
            self.combine(p1, p2, p2)
        ]
