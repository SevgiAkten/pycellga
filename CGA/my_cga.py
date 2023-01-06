import numpy as np
from numpy import random


class Candidate_Solution:
    def __init__(self, chromosome, fitness_value):
        self.chromosome = chromosome
        self.fitness_value = fitness_value


class Population:
    def __init__(self, pop_size):
        self.pop_size = pop_size


population = Population()

ch = random.randint(2, size=(5))
population.pop_size = n_rows * n_columns

grid = np.array([n_rows], [n_columns])
