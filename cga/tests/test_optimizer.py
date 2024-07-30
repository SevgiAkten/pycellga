from optimizer_cga import *
from problems.single_objective.discrete.binary.one_max import OneMax
from selection.tournament_selection import TournamentSelection
from recombination.one_point_crossover import OnePointCrossover
from mutation.bit_flip_mutation import BitFlipMutation


def test_optimizer_cga():

    res = optimize(
        n_cols=10,
        n_rows=10,
        n_gen=2,
        ch_size=52,
        gen_type="Permutation",
        p_crossover=0.8,
        p_mutation=0.4,
        known_best=7544.365901904087,
        k_tournament=2,
        problem=OneMax(),
        selection=TournamentSelection,
        recombination=OnePointCrossover,
        mutation=BitFlipMutation
    )
    assert type(res) == tuple
    assert type(res[0]) == dict
    assert type(res[1]) == dict
    assert type(res[2]) == list
    assert type(res[3]) == list
