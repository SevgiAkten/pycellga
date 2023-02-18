import numpy.random as randomgenerator
from individual import *
from problems.abstract_problem import AbstractProblem


class UniformCrossover:
    def __init__(self, parents: list, problem: AbstractProblem):
        self.parents = parents
        self.problem = problem


    def combine(self, p1: Individual, p2: Individual):
        chsize = len(p1.chromosome)
        child = [0 for i in range(chsize)]
        for i in range(chsize):
            if randomgenerator.rand() < 0.5:
                child[i] = p1.chromosome[i]
            else:
                child[i] = p2.chromosome[i]

        return child 
    

    def get_recombinations(self):

        p1 = self.parents[0]
        p2 = self.parents[1]

        return [
            self.combine(p1, p2), 
            self.combine(p1, p2)
        ]
