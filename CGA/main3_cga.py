import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from Population import *
from Selection.TournamentSelection import *
from Recombination.OnePointCrossover import *
from Mutation.BitFlipMutation import *


#                      Parameter Definition for Cellular GA                                 #
# -------------------------------------------------------------------------------------------
N_COLS = 7  # Number of colums in grid
N_ROWS = 7  # Number of rows in grid
POP_SIZE = N_COLS * N_ROWS  # Number of population
N_GEN = 10  # Number of generation
CH_SIZE = 10  # Size of chromosome
GEN_TYPE = "Binary"  # Type of gene as binary, real-value or etc.
E = 10  # Elite list size, how many of the best I will pass directly to the next generation
p_crossover = 0.8  # Probability of crossover
p_mutation = 0.4  # Probability of mutation
Known_Best = 10
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
Best_Ever_Solution = [
    Pop_list_ordered[0].chromosome,
    Pop_list_ordered[0].fitness_value,
    0,
]
mean = sum(map(lambda x: x.fitness_value, Pop_list)) / len(Pop_list)
Avg_Objectives.append(mean)

def getElitism(Pop_list):
    Pop_list_ordered = sorted(Pop_list, key=lambda x: x.fitness_value, reverse=True)
    Elit_list = []

    i = 0
    while len(Elit_list) < E:
        solution = Pop_list_ordered[i]
        Elit_add = solution

        if Elit_add not in Elit_list:
            Elit_list.append(Elit_add)
        i += 1

    return Elit_list

# ----------------------------------------------------------------
for i in range(1, N_GEN+1):
    New_gen_Pop_list=[]

    for c in range(int((POP_SIZE-E)/2)):
        pass
pass