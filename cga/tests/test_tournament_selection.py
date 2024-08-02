
from cga.problems.single_objective.discrete.binary.one_max import OneMax
from cga.selection.tournament_selection import TournamentSelection
from cga.population import Population


def test_tournament_selection():
    CH_SIZE = 16
    N_ROWS = 4
    N_COLS = 4
    GEN_TYPE = "Binary"
    problem = OneMax()
    K_TOURNAMENT = 2
    c = 0

    pop_list = Population(CH_SIZE, N_ROWS, N_COLS, GEN_TYPE,
                          problem).initial_population()

    parents = TournamentSelection(pop_list, c, K_TOURNAMENT).get_parents()

    for parent in parents:
        assert parent.ch_size == CH_SIZE
        assert parent.fitness_value != None
        assert type(parent.neighbors_positions) == list
        assert type(parent.position) == tuple

    assert parents[0].chromosome != parents[1].chromosome
    assert parents[0].position != parents[1].position
