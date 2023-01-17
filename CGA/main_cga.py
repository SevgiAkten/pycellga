import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from Population import *
from Selection.TournamentSelection import *


# Parameter Definition for Cellular GA

N_COLS = 5  # Number of colums in grid
N_ROWS = 5  # Number of rows in grid
CH_SIZE = 10  # Size of chromosome
GEN_TYPE = "Binary"  # Type of gene as binary, real-value or etc.


# Generate Initial Population
population = Population(CH_SIZE, N_ROWS, N_COLS, GEN_TYPE).InitialPopulation()

Pop_list_ordered = sorted(population, key=lambda x: x.chromosome)

# Evolution Process
"""
while ! StopCondition() do
    for individual to pop_size do
    negihbors = CalculateNeighborhood(individual.position)
    parents = Selection(neighbors)
    offspring = Recombination(parents)
    offspring = Mutation(offspring)
    Evaluation(offspring)
    Replacement(individual.position, auxiliary_pop, offspring)
    end for
    population=auxiliary_pop
end while

"""
