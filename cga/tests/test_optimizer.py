from cga.optimizer_cga import *
from cga.problems.single_objective.discrete.binary.one_max import OneMax
from cga.selection.tournament_selection import TournamentSelection
from cga.recombination.one_point_crossover import OnePointCrossover
from cga.mutation.bit_flip_mutation import BitFlipMutation


def test_optimizer_cga():

    res = optimize(
        n_cols=10,
        n_rows=10,
        n_gen=2,
        ch_size=5,
        gen_type="Permutation",
        p_crossover=0.8,
        p_mutation=0.4,
        known_best=52,
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
