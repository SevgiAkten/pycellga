# Mutation for permutation representation. Swaps the place of two genes.

import numpy as np
from individual import *
from problems.abstract_problem import AbstractProblem


class SwapMutation:
    def __init__(self, mutation_cand: Individual = None, problem: AbstractProblem = None):
        self.mutation_cand = mutation_cand
        self.problem = problem

    def mutate(self) -> Individual:

        ran_1 = np.random.randint(0, len(self.mutation_cand.chromosome))
        ran_2 = np.random.randint(0, len(self.mutation_cand.chromosome))

        while ran_1 == ran_2:
            ran_2 = np.random.randint(0, len(self.mutation_cand.chromosome))

        x = self.mutation_cand.chromosome[ran_1]
        y = self.mutation_cand.chromosome[ran_2]

        mutated_ch = list(self.mutation_cand.chromosome)

        mutated_ch[ran_1] = y
        mutated_ch[ran_2] = x

        mutated = Individual()

        mutated.chromosome = mutated_ch
        mutated.position = self.mutation_cand.position
        mutated.neighbors_positions = self.mutation_cand.neighbors_positions
        mutated.fitness_value = self.problem.f(mutated.chromosome)

        return mutated
