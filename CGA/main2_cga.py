import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from Population import *
from Selection.TournamentSelection import *
from Recombination.TwoPointsCrossover import *
from Mutation.BitFlipMutation import *


#                      Parameter Definition for Cellular GA                                 #
# -------------------------------------------------------------------------------------------
N_COLS = 5  # Number of colums in grid
N_ROWS = 5  # Number of rows in grid
POP_SIZE = N_COLS * N_ROWS  # Number of population
N_GEN = 10  # Number of generation
CH_SIZE = 10  # Size of chromosome
GEN_TYPE = "Binary"  # Type of gene as binary, real-value or etc.
E = 10  # Elite list size, how many of the best I will pass directly to the next generation
p_crossover = 0.7  # Probability of crossover
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
Best_Ever_Solution = (
    Pop_list_ordered[0].chromosome,
    Pop_list_ordered[0].fitness_value,
    0,
)

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


# -----------------------------------------------------------------
g = 0
while g != N_GEN:
    for c in range(POP_SIZE):
        Offsprings = []
        Parents = TournamentSelection(Pop_list).getParents()
        rnd = np.random.rand()

        if rnd < p_crossover:
            Offsprings = TwoPointsCrossover(Parents).getRecombinations()
        else:
            Offsprings = Parents

        for p in range(len(Offsprings)):

            mutation_cand = Offsprings[p]
            rnd = np.random.rand()

            if rnd < p_mutation:
                mutated = BitFlipMutation(mutation_cand).mutate()
                Offsprings[p] = mutated
            else:
                pass
            # Replacement: Replace if better
            x = Offsprings[p]
            a = x.fitness_value
            c = Parents[p]
            b = Parents[p].fitness_value

            if Offsprings[p].fitness_value > Parents[p].fitness_value:
                index = Pop_list.index(Parents[p])
                Pop_list[index] = Offsprings[p]
            else:
                pass

    Pop_list_ordered = sorted(Pop_list, key=lambda x: x.fitness_value, reverse=True)

    Best_Solutions.append(Pop_list_ordered[0].chromosome)
    Best_Objectives.append(Pop_list_ordered[0].fitness_value)

    if Pop_list_ordered[0].fitness_value > Best_Ever_Solution[1]:
        Best_Ever_Solution = (
            Pop_list_ordered[0].chromosome,
            Pop_list_ordered[0].fitness_value,
            i,
        )
    else:
        pass
    mean = sum(map(lambda x: x.fitness_value, Pop_list)) / len(Pop_list)
    Avg_Objectives.append(mean)

print()
print("#### Solution Output ####")
print("Best Solution             :", Best_Ever_Solution[0])
print()
print("Cost                      :", Best_Ever_Solution[1])
print("Found at generation       :", Best_Ever_Solution[2])
print("Known Best Solution       :", Known_Best)
print(f"Gap                      : {(Best_Ever_Solution[1]-Known_Best)*100/Known_Best}")
print()
print("##### Parameters #####")
print(f"Number of generation      :{N_GEN}")
print(f"Population size           :{N_COLS*N_ROWS}")
print(f"Probability of crossover  :{p_crossover*100}")
print(f"Probability of mutation   :{p_mutation*100}")
print(f"Tournament selection      :{4}")
print(f"Elitism selection         :{E}")

plt.plot(Best_Objectives)
plt.plot(Avg_Objectives)
plt.title("Objectives", fontsize=20, fontweight="bold")
plt.xlabel("Generations", fontsize=16, fontweight="bold")
plt.ylabel("Cost", fontsize=16, fontweight="bold")
plt.show()


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
