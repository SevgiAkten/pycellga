import numpy as np
from numpy import random


class Candidate_Solution:
    def __init__(self, chromosome, fitness_value):
        self.chromosome = chromosome
        self.fitness_value = fitness_value


class Population:
    def __init__(self, pop_size, pop_list):
        self.pop_size = pop_size
        self.pop_list = pop_list
        pop_list = []


class Grid:
    def __init__(self, n_rows, n_cols):
        self.n_rows = n_rows
        self.n_cols = n_cols


population = Population(25, [])


def make2DGrid(n_rows, n_cols):
    grd = np.array(n_cols)
    for i in range(grd.size):
        grd[i] = np.array(n_rows)
    return grd


g = make2DGrid(5, 5)
print(g)

# grid = Grid(5, 5)
# # g = np.array([(0, 1, 2, 3)], [(3, 2, 1, 0)])
# x = random.choice([0, 1], size=(5, 5))
# print(x)

# candidate_solution = Candidate_Solution(chromosome=101, fitness_value=10)

# for i in range(population.pop_size):
#     candidate_solution.chromosome = random.randint(2, size=(5))
#     ch = candidate_solution.chromosome
#     population.pop_list.append(ch)
#     grid
#     print(f"{i+1}-{ch}")
