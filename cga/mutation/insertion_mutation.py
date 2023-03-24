import numpy as np
from individual import *
from problems.abstract_problem import AbstractProblem


class InsertionMutation:
    def __init__(self, mutation_cand: Individual = None, problem: AbstractProblem = None):
        self.mutation_cand = mutation_cand
        self.problem = problem

    def mutate(self) -> Individual:

        mutated_ch = list(self.mutation_cand.chromosome)

        ran_1 = np.random.randint(0, len(mutated_ch))
        ran_2 = np.random.randint(0, len(mutated_ch))

        while ran_1 == ran_2:
            ran_2 = np.random.randint(0, len(mutated_ch))

        x = mutated_ch[ran_1]

        mutated_ch_new = list(mutated_ch)

        mutated_ch_new.remove(x)

        mutated_ch_new.insert(ran_2, x)

        mutated = Individual()

        mutated.chromosome = mutated_ch_new
        mutated.ch_size = len(mutated_ch_new)
        mutated.position = self.mutation_cand.position
        mutated.neighbors_positions = self.mutation_cand.neighbors_positions
        mutated.fitness_value = self.problem.f(mutated.chromosome)

        return mutated
