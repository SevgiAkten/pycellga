import numpy as np
import matplotlib.pyplot as plt
from population import *
from selection.tournament_selection import *
from recombination.one_point_crossover import *
from mutation.bit_flip_mutation import *
from problems.combinatorial.one_max import OneMax

#                      Parameter Definition for Cellular GA                                 #
# -------------------------------------------------------------------------------------------
N_COLS = 10  # Number of colums in grid
N_ROWS = 10  # Number of rows in grid
POP_SIZE = N_COLS * N_ROWS  # Number of population
N_GEN = 50  # Number of generation
CH_SIZE = 50  # Size of chromosome
GEN_TYPE = "Binary"  # Type of gene as binary, real-value or etc.
P_CROSSOVER = 0.8  # Probability of crossover
P_MUTATION = 0.4  # Probability of mutation
KNOWN_BEST = 50 # It can be change according to the problem
problem = OneMax()
# -------------------------------------------------------------------------------------------

best_solutions = []
best_objectives = []
best_ever_solution = []
avg_objectives = []

# Generate Initial Population
pop_list = Population(CH_SIZE, N_ROWS, N_COLS, GEN_TYPE, problem).initial_population()

pop_list_ordered = sorted(pop_list, key=lambda x: x.fitness_value, reverse=True)

best_solutions.append(pop_list_ordered[0].chromosome)
best_objectives.append(pop_list_ordered[0].fitness_value)
best_ever_solution = [
    pop_list_ordered[0].chromosome,
    pop_list_ordered[0].fitness_value,
    0,
]

mean = sum(map(lambda x: x.fitness_value, pop_list)) / len(pop_list)
avg_objectives.append(mean)

# -----------------------------------------------------------------
g = 1
while g != N_GEN + 1:
    for c in range(POP_SIZE):
        offsprings = []
        parents = TournamentSelection(pop_list, c).get_parents()
        rnd = np.random.rand()

        if rnd < P_CROSSOVER:
            offsprings = OnePointCrossover(parents, problem).get_recombinations()
        else:
            offsprings = parents

        for p in range(len(offsprings)):

            mutation_cand = offsprings[p]
            rnd = np.random.rand()

            if rnd < P_MUTATION:
                mutated = BitFlipMutation(mutation_cand, problem).mutate()
                offsprings[p] = mutated
            else:
                pass

        # # Replacement: Replace if better
            if offsprings[p].fitness_value > parents[p].fitness_value:
                index = pop_list.index(parents[p])
                new_p = offsprings[p]
                old_p = pop_list[index]
                pop_list[index] = new_p
                
            else:
                pass   
    pop_list_ordered = sorted(pop_list, key=lambda x: x.fitness_value, reverse=True)

    best_solutions.append(pop_list_ordered[0].chromosome)
    best_objectives.append(pop_list_ordered[0].fitness_value)

    if (pop_list_ordered[0].fitness_value) > best_ever_solution[1]:
        best_ever_solution = [
            pop_list_ordered[0].chromosome,
            pop_list_ordered[0].fitness_value,
            g,
        ]
    else:
        pass

    mean = sum(map(lambda x: x.fitness_value, pop_list)) / len(pop_list)
    avg_objectives.append(mean)

    print(
        f"{g} - {pop_list_ordered[0].chromosome} - {pop_list_ordered[0].fitness_value}"
    )
    g += 1
# -----------------------------------------------------------------

print()
print("#### Solution Output ####")
print("Best Solution Chromosome  :", best_ever_solution[0])
print()
print("Best Solution             :", best_ever_solution[1])
print("Found at generation       :", best_ever_solution[2])
print("Known Best Solution       :", KNOWN_BEST)
print(f"Gap                      : {(best_ever_solution[1]-KNOWN_BEST)*100/KNOWN_BEST}")
print()
print("##### Parameters #####")
print(f"Number of generation      :{N_GEN}")
print(f"Population size           :{N_COLS*N_ROWS}")
print(f"Probability of crossover  :{P_CROSSOVER*100}")
print(f"Probability of mutation   :{P_MUTATION*100}")
print(f"Tournament selection      :{2}")

plt.plot(best_objectives)
plt.plot(avg_objectives)
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
