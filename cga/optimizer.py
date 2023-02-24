import numpy as np
import matplotlib.pyplot as plt
from population import *
from selection.tournament_selection import *
from recombination.one_point_crossover import *
from mutation.bit_flip_mutation import *
from problems.combinatorial.one_max import OneMax


def optimize(
    n_cols: int = 10,
    n_rows: int = 10,
    n_gen: int = 50,
    ch_size: int = 50,
    gen_type: str = "Binary",
    p_crossover: float = 0.8,
    p_mutation: float = 0.4,
    known_best: float = 50,
    k_tournament: int = 2,
    problem: AbstractProblem = OneMax(),
    selection=TournamentSelection,
    recombination=OnePointCrossover,
    mutation=BitFlipMutation
) -> tuple:

    pop_size = n_cols * n_rows
    best_solutions = []
    best_objectives = []
    best_ever_solution = []
    avg_objectives = []

    # Generate Initial Population
    pop_list = Population(ch_size, n_rows, n_cols,
                          gen_type, problem).initial_population()

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
    while g != n_gen + 1:
        for c in range(pop_size):
            offsprings = []
            parents = selection(pop_list, c, k_tournament).get_parents()
            rnd = np.random.rand()

            if rnd < p_crossover:
                offsprings = recombination(
                    parents, problem).get_recombinations()
            else:
                offsprings = parents

            for p in range(len(offsprings)):

                mutation_cand = offsprings[p]
                rnd = np.random.rand()

                if rnd < p_mutation:
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
        "Best Solution Chromosome  :": best_ever_solution[0],
        "Best Solution             :": best_ever_solution[1],
        "Found at generation       :": best_ever_solution[2],
        "Known Best Solution       :": known_best,
        "Gap                       :": (best_ever_solution[1]-known_best)*100/known_best
    }
    parameters = {
        "Number of generation      :": n_gen,
        "Population size           :": n_cols*n_rows,
        "Probability of crossover  :": p_crossover*100,
        "Probability of mutation   :": p_mutation*100,
        "Tournament selection      :": k_tournament
    }

    return optimizer_result, parameters, best_objectives, avg_objectives
