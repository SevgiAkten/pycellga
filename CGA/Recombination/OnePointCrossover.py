import numpy as np
from Individual import *
from Problems.abstractproblem import AbstractProblem


class OnePointCrossover:
    def __init__(self, Parents, problem: AbstractProblem):
        self.Parents = Parents
        self.problem = problem

    def getRecombinations(self):

        Offsprings = []
        p1 = self.Parents[0]
        p2 = self.Parents[1]

        co_point = np.random.randint(len(p1.chromosome))

        p1_seg1 = list(p1.chromosome[0:co_point])
        p1_seg2 = list(p1.chromosome[co_point:])

        p2_seg1 = list(p2.chromosome[0:co_point])
        p2_seg2 = list(p2.chromosome[co_point:])

        # First child
        child_1 = Individual()
        new_chromosome = p1_seg1 + p2_seg2
        child_1.chromosome = new_chromosome

        child_1.position = p1.position
        child_1.neighbors_positions = p1.neighbors_positions
        child_1.fitness_value = self.problem.f(child_1.chromosome)
        Offsprings.append(child_1)

        # Second child
        child_2 = Individual()
        child_2.chromosome = p1_seg2 + p2_seg1

        child_2.position = p2.position
        child_2.neighbors_positions = p2.neighbors_positions
        child_2.fitness_value = self.problem.f(child_2.chromosome)

        Offsprings.append(child_2)

        return Offsprings
