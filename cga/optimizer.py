import numpy as np
import matplotlib.pyplot as plt
from population import *
from selection.tournament_selection import *
from recombination.one_point_crossover import *
from mutation.bit_flip_mutation import *
from problems.combinatorial.one_max import OneMax


def optimize(
    N_COLS: int = 10,
    N_ROWS: int = 10,
    N_GEN: int = 50,
    CH_SIZE: int = 50,
    GEN_TYPE: str = "Binary",
    P_CROSSOVER: float = 0.8,
    P_MUTATION: float = 0.4,
    KNOWN_BEST: float = 50,
    K_TOURNAMENT: int = 2,
    problem: AbstractProblem = OneMax(),
    selection=TournamentSelection,
    recombination=OnePointCrossover,
    mutation=BitFlipMutation
) -> dict:

    POP_SIZE = N_COLS * N_ROWS
    best_solutions = []
    best_objectives = []
    best_ever_solution = []
    avg_objectives = []

    # Generate Initial Population
    pop_list = Population(CH_SIZE, N_ROWS, N_COLS,
                          GEN_TYPE, problem).initial_population()

    pop_list_ordered = sorted(
        pop_list, key=lambda x: x.fitness_value, reverse=True)

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
            parents = selection(pop_list, c, K_TOURNAMENT).get_parents()
            rnd = np.random.rand()

            if rnd < P_CROSSOVER:
                offsprings = recombination(
                    parents, problem).get_recombinations()
            else:
                offsprings = parents

            for p in range(len(offsprings)):

                mutation_cand = offsprings[p]
                rnd = np.random.rand()

                if rnd < P_MUTATION:
                    mutated = mutation(mutation_cand, problem).mutate()
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
        pop_list_ordered = sorted(
            pop_list, key=lambda x: x.fitness_value, reverse=True)

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

    optimizer_result = {
        "-----------------------------------------------------": "",
        "--------------#### Solution Output ####--------------": "",
        "Best Solution Chromosome  :": best_ever_solution[0],
        "Best Solution             :": best_ever_solution[1],
        "Found at generation       :": best_ever_solution[2],
        "Known Best Solution       :": KNOWN_BEST,
        "Gap                       :": (best_ever_solution[1]-KNOWN_BEST)*100/KNOWN_BEST,
        "--------------##### Parameters #####----------------": "",
        "Number of generation      :": N_GEN,
        "Population size           :": N_COLS*N_ROWS,
        "Probability of crossover  :": P_CROSSOVER*100,
        "Probability of mutation   :": P_MUTATION*100,
        "Tournament selection      :": K_TOURNAMENT,
        "-----------------------------------------------------": ""
    }

    return optimizer_result, best_objectives, avg_objectives


res = optimize()
# res[0] = optimizer_result
# res[1] = best_objectives
# res[2] = avg_objectives


# exucute optimize function print optimizer_result dict keys and values
[print(i, res[0][i]) for i in res[0]]

# plot result
plt.plot(res[1])  # best_objectives
plt.plot(res[2])  # avg_objectives
plt.title("Objectives", fontsize=20, fontweight="bold"),
plt.xlabel("Generations", fontsize=16, fontweight="bold"),
plt.ylabel("Cost", fontsize=16, fontweight="bold"),
plt.show()
