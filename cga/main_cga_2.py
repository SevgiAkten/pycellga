
# --------------------------------- methods ------------------------------------------ #
from optimizer_cga import *
# from optimizer_sync_cga import *
# from optimizer_alpha_cga import *

# ------------------------------------------------------------------------------------ #

import matplotlib.pyplot as plt
from db_utility import DBUtility

# --------------------------------- problems -------------------------------- #
# Binary
from problems.single_objective.discrete.binary.count_sat import CountSat
# from problems.single_objective.discrete.binary.fms import Fms
from problems.single_objective.discrete.binary.mmdp import Mmdp
from problems.single_objective.discrete.binary.one_max import OneMax
from problems.single_objective.discrete.binary.peak import Peak
from problems.single_objective.discrete.binary.ecc import Ecc
from problems.single_objective.discrete.binary.maxcut20_01 import Maxcut20_01
from problems.single_objective.discrete.binary.maxcut20_09 import Maxcut20_09
from problems.single_objective.discrete.binary.maxcut100 import Maxcut100
# Permutation
from problems.single_objective.discrete.permutation.tsp import Tsp
# Real-valued
from problems.single_objective.continuous.ackley import Ackley
from problems.single_objective.continuous.bohachevsky import Bohachevsky
from problems.single_objective.continuous.fms import Fms
from problems.single_objective.continuous.rastrigin import Rastrigin
from problems.single_objective.continuous.rosenbrock import Rosenbrock
from problems.single_objective.continuous.schwefel import Schwefel
from problems.single_objective.continuous.sphere import Sphere
# -------------------------------------------------------------------------- #

# ------------------------------ selection --------------------------------- #
from selection.roulette_wheel_selection import RouletteWheelSelection
from selection.tournament_selection import TournamentSelection
# -------------------------------------------------------------------------- #

# ------------------------------ recombination ----------------------------- #
from recombination.one_point_crossover import OnePointCrossover
from recombination.pmx_crossover import PMXCrossover
from recombination.two_point_crossover import TwoPointCrossover
from recombination.uniform_crossover import UniformCrossover
# -------------------------------------------------------------------------- #

# -------------------------------- mutation -------------------------------- #
from mutation.bit_flip_mutation import BitFlipMutation
from mutation.insertion_mutation import InsertionMutation
from mutation.shuffle_mutation import ShuffleMutation
from mutation.swap_mutation import SwapMutation
from mutation.two_opt_mutation import TwoOptMutation
# -------------------------------------------------------------------------- #


def runSimulation():
    result_tuple = optimize(
        n_cols=20,
        n_rows=20,
        n_gen=100,
        ch_size=5,
        gen_type="Real-valued",
        p_crossover=0.9,
        p_mutation=0.6,
        known_best=0,
        k_tournament=2,
        problem=Ackley(),
        selection=TournamentSelection,
        recombination=UniformCrossover,
        mutation=SwapMutation
    )
    # result_tuple[0] = optimizer_result, type is dict
    # result_tuple[1] = parameters, type is dict
    # result_tuple[2] = best_objectives, type is list
    # result_tuple[3] = avg_objectives, type is list

    method = "cga"
    gen_type = "Permutation"
    test_function = "Tsp"
    best_solution = result_tuple[0].get('best_solution')
    found_at_generation = result_tuple[0].get('found_at_generation')
    selection = "TournamentSelection"
    recombination = "PMXCrossover"
    mutation = "SwapMutation"
    neighborhood = "Linear9"
    n_cols = 5
    n_rows = 5
    n_gen = result_tuple[1].get('number_of_generation')
    p_cross = result_tuple[1].get('probability_of_crossover')
    p_mut = result_tuple[1].get('probability_of_mutation')

    # database record
    tmpdb = "./simulations.db"
    db = DBUtility(dbpath=tmpdb)
    db.createtables()
    db.insertoptresult(method, gen_type, test_function, best_solution, found_at_generation,
                       selection, recombination, mutation, neighborhood, n_cols, n_rows, n_gen, p_cross, p_mut)
    db.closedb()

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
    # plt.show()


for x in range(10):
    runSimulation()
