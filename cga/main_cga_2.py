from optimizer import *
import matplotlib.pyplot as plt
from problems.single_objective.discrete.permutation.tsp import Tsp

from selection.tournament_selection import TournamentSelection
from selection.roulette_wheel_selection import RouletteWheelSelection

from recombination.one_point_crossover import OnePointCrossover
from recombination.two_point_crossover import TwoPointCrossover
from recombination.uniform_crossover import UniformCrossover
from recombination.pmx_crossover import PMXCrossover

from mutation.insertion_mutation import InsertionMutation
from mutation.shuffle_mutation import ShuffleMutation
from mutation.swap_mutation import SwapMutation
from mutation.two_opt_mutation import TwoOptMutation

result_tuple = optimize(
    n_cols=10,
    n_rows=10,
    n_gen=2,
    ch_size=52,
    gen_type="Permutation",
    p_crossover=0.8,
    p_mutation=0.4,
    known_best=7544.365901904087,
    k_tournament=2,
    problem=Tsp(),
    selection=TournamentSelection,
    recombination=PMXCrossover,
    mutation=InsertionMutation

)
# result_tuple[0] = optimizer_result, type is dict
# result_tuple[1] = parameters, type is dict
# result_tuple[2] = best_objectives, type is list
# result_tuple[3] = avg_objectives, type is list

# exucute optimize function print optimizer_result dict keys and values
print("-------------#### Solution Output ####-------------")
[print(i, result_tuple[0][i]) for i in result_tuple[0]]

print("-------------##### Parameters #####-------------")
[print(i, result_tuple[1][i]) for i in result_tuple[1]]

# plot result
plt.plot(result_tuple[2])  # best_objectives
plt.plot(result_tuple[3])  # avg_objectives
plt.title("Objectives", fontsize=20, fontweight="bold"),
plt.xlabel("Generations", fontsize=16, fontweight="bold"),
plt.ylabel("Cost", fontsize=16, fontweight="bold"),
plt.show()
