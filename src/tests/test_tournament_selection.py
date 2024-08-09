from problems.single_objective.discrete.binary.one_max import OneMax
from selection.tournament_selection import TournamentSelection
from population import Population, OptimizationMethod
from individual import GeneType

def test_tournament_selection():
    """
    Test the TournamentSelection class implementation.

    This test verifies the functionality of the TournamentSelection for selecting parent individuals 
    from a population. It ensures that the selected parents have valid attributes and different chromosomes 
    and positions.

    The test performs the following checks:
    1. Each selected parent has the correct chromosome size and a non-None fitness value.
    2. Each selected parent has valid types for neighbors_positions and position attributes.
    3. The selected parents have different chromosomes and positions.

    Parameters
    ----------
    None

    Raises
    ------
    AssertionError
        If any of the conditions for the parent selection are not met.
    """
    CH_SIZE = 16
    N_ROWS = 4
    N_COLS = 4
    GEN_TYPE = GeneType.BINARY
    problem = OneMax()
    K_TOURNAMENT = 2
    c = 0

    # Initialize the population
    pop_list = Population(OptimizationMethod.CGA,CH_SIZE, N_ROWS, N_COLS, GEN_TYPE, problem).initial_population()

    # Perform tournament selection to get parent individuals
    parents = TournamentSelection(pop_list, c, K_TOURNAMENT).get_parents()

    # Verify the attributes of each selected parent
    for parent in parents:
        assert parent.ch_size == CH_SIZE, "Parent chromosome size does not match expected size."
        assert parent.fitness_value is not None, "Parent fitness value is None."
        assert isinstance(parent.neighbors_positions, list), "Parent neighbors_positions is not of type list."
        assert isinstance(parent.position, tuple), "Parent position is not of type tuple."

    # Check that the selected parents have different chromosomes and positions
    assert parents[0].chromosome != parents[1].chromosome, "Selected parents have the same chromosome."
    assert parents[0].position != parents[1].position, "Selected parents have the same position."

if __name__ == "__main__":
    test_tournament_selection()
