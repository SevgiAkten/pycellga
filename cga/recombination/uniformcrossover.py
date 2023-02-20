import numpy.random as randomgenerator
from individual import *
from problems.abstract_problem import AbstractProblem
from typing import List

class UniformCrossover:
    def __init__(self, parents: list, problem: AbstractProblem):
        self.parents = parents
        self.problem = problem


    def combine(self, p1: Individual, p2: Individual, locationsource: Individual) -> Individual:
        chsize = len(p1.chromosome)
        child = [0 for i in range(chsize)]
        for i in range(chsize):
            if randomgenerator.rand() < 0.5:
                child[i] = p1.chromosome[i]
            else:
                child[i] = p2.chromosome[i]

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
