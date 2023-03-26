from typing import List
from individual import Individual
import numpy as np
import random


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
