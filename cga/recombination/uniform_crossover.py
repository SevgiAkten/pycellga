
import numpy.random as randomgenerator
from individual import *
from problems.abstract_problem import AbstractProblem
from typing import List

"""
    The Uniform crossover operator is a genetic algorithm technique used to produce offspring 
    by randomly combining genes from two parent solutions. Instead of relying on a fixed crossover 
    point or range, Uniform crossover selects each gene position independently, with an equal 
    probability of being inherited from either parent. This random selection process ensures 
    that each gene in the offspring has an equal chance of coming from either parent, promoting 
    genetic diversity and allowing for a more thorough exploration of the solution space. 
    Uniform crossover is particularly effective in problems where a balanced mix of traits from 
    both parents is desired, as it avoids the bias of segment-based crossover methods and provides 
    a high degree of recombination flexibility.
"""

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
