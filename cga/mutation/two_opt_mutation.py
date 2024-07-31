import numpy as np
from individual import *
from problems.abstract_problem import AbstractProblem

"""
    The Two-Opt Mutation operator is a technique used in genetic algorithms to improve solutions 
    by iteratively refining the order of elements within a sequence. During the mutation process, 
    two segments of the sequence are selected, and their order is reversed to create a new arrangement. 
    This method helps eliminate crossings and improves the overall structure of the solution by removing 
    suboptimal paths. Two-Opt Mutation is particularly useful for optimization problems involving routes or 
    paths, such as the traveling salesman problem, as it enhances solution quality by systematically 
    improving the sequence and reducing inefficiencies.
"""


class TwoOptMutation:
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
            mutated_ch_new[ran_1:ran_2] = reversed(mutated_ch_new[ran_1:ran_2])
        else:
            mutated_ch_new[ran_2:ran_1] = reversed(mutated_ch_new[ran_2:ran_1])

        mutated = Individual()

        mutated.chromosome = mutated_ch_new
        mutated.ch_size = len(mutated_ch_new)
        mutated.position = self.mutation_cand.position
        mutated.neighbors_positions = self.mutation_cand.neighbors_positions
        mutated.fitness_value = self.problem.f(mutated.chromosome)

        return mutated
