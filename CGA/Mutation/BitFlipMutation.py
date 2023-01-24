import numpy as np
from Individual import *
from Problems.Combinatorial.OneMax import *


class BitFlipMutation:
    def __init__(self, mutation_cand):
        self.mutation_cand = mutation_cand

    def mutate(self):

        index = np.random.randint(0, len(self.mutation_cand.chromosome))
        if self.mutation_cand.chromosome[index] == 0:
            self.mutation_cand.chromosome[index] = 1
        else:
            self.mutation_cand.chromosome[index] = 0

        mutated = Individual()
        mutated.chromosome = self.mutation_cand.chromosome
        mutated.position = self.mutation_cand.position
        mutated.neighbors_positions = self.mutation_cand.neighbors_positions
        mutated.fitness_value = OneMax(mutated.chromosome).evalOneMax()

        return mutated
