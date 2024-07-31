
import random
from individual import *
from problems.abstract_problem import AbstractProblem
from typing import List

"""
    The Unfair Average Crossover operator is a genetic algorithm technique designed to create 
    offspring by combining parent solutions with weighted averaging. Unlike standard averaging 
    methods, this operator applies different weights to each parent solution, allowing for an 
    "unfair" distribution of influence in the offspring. The weights are typically determined 
    based on predefined criteria or dynamically adjusted during the algorithm. This method can 
    be useful in scenarios where certain parents are more likely to contribute to better solutions, 
    allowing the offspring to inherit more traits from those more promising parents. Unfair Average 
    Crossover helps balance exploration and exploitation by tailoring the contribution of each parent 
    to the genetic recombination process, potentially leading to more effective solution generation.
"""

class UnfairAvarageCrossover:
    def __init__(self, parents: list, problem: AbstractProblem):
        self.parents = parents
        self.problem = problem

    def get_recombinations(self) -> List[Individual]:

        offsprings = []
        p1 = self.parents[0]
        p2 = self.parents[1]
        chsize = len(p1.chromosome)
        a = p1.chromosome
        b = p2.chromosome

        alpha = random.uniform(0, 1)
        child_1_ch = [0 for i in range(chsize)]
        child_2_ch = [0 for i in range(chsize)]

        alpha = random.uniform(0, 1)
        j = random.randint(1, chsize)

        for i in range(chsize):
            if (i <= j):
                child_1_ch[i] = round((1+alpha)*a[i] - alpha*b[i], 5)
                child_2_ch[i] = round((1-alpha)*a[i] + alpha*b[i], 5)
            else:
                child_1_ch[i] = round(-alpha*a[i] + (1+alpha)*b[i], 5)
                child_2_ch[i] = round(alpha*a[i] + (1-alpha)*b[i], 5)

        # First child
        child_1 = Individual()
        child_1.chromosome = child_1_ch
        child_1.ch_size = len(child_1_ch)
        child_1.position = p1.position
        child_1.neighbors_positions = p1.neighbors_positions
        child_1.fitness_value = self.problem.f(child_1_ch)
        offsprings.append(child_1)

        # Second child
        child_2 = Individual()
        child_2.chromosome = child_2_ch
        child_2.ch_size = len(child_2_ch)
        child_2.position = p2.position
        child_2.neighbors_positions = p2.neighbors_positions
        child_2.fitness_value = self.problem.f(child_2_ch)
        offsprings.append(child_2)

        return offsprings
