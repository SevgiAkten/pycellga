#  It keeps the largest part of the best parent
import numpy as np
from Individual import *
from Problems.Combinatorial.OneMax import *


class TwoPointsCrossover:
    def __init__(self, Parents):
        self.Parents = Parents

    def getRecombinations(self):

        Offsprings = []

        p1 = self.Parents[0]
        p2 = self.Parents[1]

        param = len(p1.chromosome) * 0.20
        min_c = param
        max_c = len(p1.chromosome) - (param - 1)

        co_point_1 = np.random.randint(min_c, max_c)
        co_point_2 = np.random.randint(min_c, max_c)

        p1_seg1 = p1.chromosome[0:co_point_1]
        p1_seg2 = p1.chromosome[co_point_1 : len(p1.chromosome)]

        p2_seg1 = p2.chromosome[0:co_point_2]
        p2_seg2 = p2.chromosome[co_point_2 : len(p2.chromosome)]

        temp1_seg = list(p2)
        temp2_seg = list(p1)

        # First child
        child_1 = Individual()
        op_rand = np.random.rand()
        if op_rand < 0.5:

            for i in range(len(p1_seg1)):
                temp1_seg.remove(p1_seg1[i])
            child_1.chromosome = p1_seg1 + temp1_seg
        else:
            for i in range(len(p1_seg2)):
                temp1_seg.remove(p1_seg2[i])
            child_1.chromosome = temp1_seg + p1_seg2

        child_1.position = p1.position
        child_1.neighbors_positions = p1.neighbors_positions
        child_1.fitness_value = OneMax(child_1.chromosome).evalOneMax()

        Offsprings.append(child_1)

        # Second child
        child_2 = Individual()
        op_rand = np.random.rand()
        if op_rand < 0.5:
            for i in range(len(p2_seg1)):
                temp2_seg.remove(p2_seg1[i])
            child_2.chromosome = p2_seg1 + temp2_seg
        else:
            for i in range(len(p2_seg2)):
                temp2_seg.remove(p2_seg2[i])
            child_2.chromosome = temp2_seg + p2_seg2

        child_2.position = p2.position
        child_2.neighbors_positions = p2.neighbors_positions
        child_2.fitness_value = OneMax(child_2.chromosome).evalOneMax()

        Offsprings.append(child_2)

        return Offsprings
