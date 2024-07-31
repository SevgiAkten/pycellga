from typing import List
from individual import Individual
import numpy as np
import random

"""
    The Roulette Wheel Selection operator is a method used in genetic algorithms to select 
    individuals from a population based on their fitness levels. Each individual is assigned a 
    probability of being selected proportional to its fitness, which is represented as a segment 
    on a metaphorical roulette wheel. During selection, individuals are chosen by spinning the wheel, 
    with higher fitness individuals having a larger segment and thus a higher chance of being selected. 
    This probabilistic approach allows for both exploitation of high-quality solutions and exploration 
    of less fit individuals, contributing to the overall diversity and adaptability of the population. 
    Roulette Wheel Selection is particularly useful for maintaining a balance between selection pressure 
    and genetic diversity in evolutionary algorithms.
"""
class RouletteWheelSelection:
    def __init__(self, pop_list: List[Individual] = {}, c: int = 0):
        self.pop_list = pop_list
        self.c = c

    def get_parents(self) -> List[Individual]:
        parents = []
        p1 = self.pop_list[self.c - 1]

        parents.append(p1)
        neighbors_positions = p1.neighbors_positions
        neighbors = []

        for i in range(len(self.pop_list)):
            if self.pop_list[i].position in neighbors_positions:
                neighbors.append(self.pop_list[i])

        neighbors_fitness_sum = 0
        neighbors_fitnesess = []
        for neighbor in neighbors:
            neighbors_fitness_sum += neighbor.fitness_value
            neighbors_fitnesess.append(neighbor.fitness_value)

        random_number = random.uniform(0, 1)
        previous_probability = 0
        for neighbor in neighbors:
            previous_probability += (neighbor.fitness_value /
                                     neighbors_fitness_sum)

            if p1 != neighbor:
                if random_number < previous_probability:
                    parents.append(neighbor)
                    break

        return parents
