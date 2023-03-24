import numpy as np
import random as rd
from individual import *
from problems.abstract_problem import AbstractProblem


class ShuffleMutation:
    def __init__(self, mutation_cand: Individual = None, problem: AbstractProblem = None):
        self.mutation_cand = mutation_cand
        self.problem = problem

    def mutate(self) -> Individual:

        mutated_ch = list(self.mutation_cand.chromosome)

        ran_1 = np.random.randint(0, len(mutated_ch))
        ran_2 = np.random.randint(0, len(mutated_ch))

        while abs(ran_1 - ran_2) < 3:
            ran_2 = np.random.randint(0, len(mutated_ch))

        mutated_ch_new = list(mutated_ch)

        if ran_1 < ran_2:
            part = mutated_ch_new[ran_1:ran_2]
            part_shuffle = rd.sample(part, len(part))
            while part == part_shuffle:
                part_shuffle = rd.sample(part, len(part))
            mutated_ch_new[ran_1:ran_2] = part_shuffle
        else:
            part = mutated_ch_new[ran_2:ran_1]
            part_shuffle = rd.sample(part, len(part))
            while part == part_shuffle:
                part_shuffle = rd.sample(part, len(part))
            mutated_ch_new[ran_2:ran_1] = part_shuffle

        mutated = Individual()

        mutated.chromosome = mutated_ch_new
        mutated.ch_size = len(mutated_ch_new)
        mutated.position = self.mutation_cand.position
        mutated.neighbors_positions = self.mutation_cand.neighbors_positions
        mutated.fitness_value = self.problem.f(mutated.chromosome)

        return mutated
