
import numpy as np
from individual import *
from problems.abstract_problem import AbstractProblem

"""
    The Swap Mutation operator is a genetic algorithm technique used to alter solutions by 
    exchanging the positions of two elements within a sequence. During the mutation process, 
    two positions in the sequence are randomly selected, and the elements at these positions are swapped. 
    This method introduces small but significant changes to the solution, which can help explore new 
    configurations and maintain genetic diversity. Swap Mutation is particularly effective for problems 
    involving permutations or ordered sequences, as it preserves the overall structure of the solution while 
    allowing for variability and improvement in the search for optimal solutions.
"""


class SwapMutation:
    def __init__(self, mutation_cand: Individual = None, problem: AbstractProblem = None):
        self.mutation_cand = mutation_cand
        self.problem = problem

    def mutate(self) -> Individual:

        mutated_ch = list(self.mutation_cand.chromosome)

        ran_1 = np.random.randint(0, len(mutated_ch))
        ran_2 = np.random.randint(0, len(mutated_ch))

        while ran_1 == ran_2:
            ran_2 = np.random.randint(0, len(mutated_ch))

        swap_candidate_1 = mutated_ch[ran_1]
        swap_candidate_2 = mutated_ch[ran_2]

        mutated_ch_new = list(mutated_ch)

        mutated_ch_new[ran_1] = swap_candidate_2
        mutated_ch_new[ran_2] = swap_candidate_1

        mutated = Individual()

        mutated.chromosome = mutated_ch_new
        mutated.ch_size = len(mutated_ch_new)
        mutated.position = self.mutation_cand.position
        mutated.neighbors_positions = self.mutation_cand.neighbors_positions
        mutated.fitness_value = self.problem.f(mutated.chromosome)

        return mutated
