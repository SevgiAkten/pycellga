import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from Population import *
from Selection.TournamentSelection import *
from Recombination.TwoPointsCrossover import *


#                      Parameter Definition for Cellular GA                                 #
# -------------------------------------------------------------------------------------------
N_COLS = 5  # Number of colums in grid
N_ROWS = 5  # Number of rows in grid
# Pop_SIZE is calculated as N_COLS*N_ROWS
N_GEN = 500  # Number of generation
CH_SIZE = 10  # Size of chromosome
GEN_TYPE = "Binary"  # Type of gene as binary, real-value or etc.
E = 10  # Elite list size, how many of the best I will pass directly to the next generation
p_crossover = 0.7  # Probability of crossover
p_mutation = 0.4  # Probability of mutation
# -------------------------------------------------------------------------------------------

Best_Solutions = []
Best_Objectives = []
Best_Ever_Solution = []
Avg_Objectives = []

# Generate Initial Population
Pop_list = Population(CH_SIZE, N_ROWS, N_COLS, GEN_TYPE).InitialPopulation()

Pop_list_ordered = sorted(Pop_list, key=lambda x: x.fitness_value, reverse=True)

Best_Solutions.append(Pop_list_ordered[0].chromosome)
Best_Objectives.append(Pop_list_ordered[0].fitness_value)
Best_Ever_Solution = (Pop_list_ordered[0], Pop_list_ordered[1], 0)

mean = sum(map(lambda x: x.fitness_value, Pop_list)) / len(Pop_list)
Avg_Objectives.append(mean)

for i in range(1, N_GEN + 1):
    New_gen_Pop_list = []

    for c in range(int((Pop_list.pop_size - E) / 2)):

        Offsprings = []
        Parents = TournamentSelection(Pop_list).getParents()

        rnd = np.random.rand()

        if rnd < p_crossover:
            Offsprings = TwoPointsCrossover(Parents).getRecombinations()


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
