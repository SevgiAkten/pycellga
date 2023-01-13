import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import Individual
import Grid
import Population
import Selection.TournamentSelection


# Parameter Definition for cga
N_COLS = 5
N_ROWS = 5
POP_SIZE = N_ROWS * N_COLS


# Generate Initial Population
# ....

# Evaluate Initial Population
# ....

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
