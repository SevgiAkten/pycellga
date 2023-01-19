import numpy as np


class BitFlipMutation:
    def __init__(self, mutation_cand):
        self.mutation_cand = mutation_cand

    def mutate(self):

        index = np.random.randint(0, len(self.mutation_cand.chromosome))
        if self.mutation_cand.chromosome[index] == 0:
            self.mutation_cand.chromosome[index] = 1
        else:
            self.mutation_cand.chromosome[index] = 0

        mutated = self.mutation_cand
        return mutated
