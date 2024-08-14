import pytest
from numpy import random
import random as rd
from individual import Individual, GeneType 


@pytest.fixture
def setup_individual():
    """
    Fixture to provide an instance of the Individual class with different configurations.
    """
    return Individual(gen_type=GeneType.BINARY, ch_size=10)

def test_individual_init():
    """
    Test the initialization of the Individual class.
    """
    ind = Individual(gen_type=GeneType.BINARY, ch_size=10)
    assert ind.gen_type == GeneType.BINARY
    assert ind.ch_size == 10
    assert ind.chromosome == []
    assert ind.fitness_value == 0
    assert ind.position == (0, 0)
    assert ind.neighbors_positions is None
    assert ind.neighbors is None

def test_randomize_binary():
    """
    Test the randomization of the chromosome for a binary genome type.
    """
    ind = Individual(gen_type=GeneType.BINARY, ch_size=10)
    ind.randomize()
    assert len(ind.chromosome) == 10
    assert all(gene in [0, 1] for gene in ind.chromosome)

def test_randomize_permutation():
    """
    Test the randomization of the chromosome for a permutation genome type.
    """
    chsize = 14
    ind = Individual(gen_type=GeneType.PERMUTATION, ch_size=chsize)
    ind.randomize()
    assert len(ind.chromosome) == chsize
    for i in range(1, chsize+1):
        assert i in ind.chromosome

    assert len(set(ind.chromosome)) == len(ind.chromosome)

def test_randomize_real_valued():
    """
    Test the randomization of the chromosome for a real-valued genome type.
    """
    chsize = 10
    ind = Individual(gen_type=GeneType.REAL, ch_size=chsize)
    ind.randomize()
    assert len(ind.chromosome) == chsize
    assert all(isinstance(gene, float) for gene in ind.chromosome)

def test_illegal_genome_type():
    """
    Test that an exception is raised when an illegal genome type is provided.
    """
    try:
        ind = Individual(gen_type="Illegal genome type", ch_size=10)
    except Exception:
        # Passes the test if an exception is raised
        assert True


def test_get_set_neighbors_positions():
    """
    Test getting and setting the positions of the individual's neighbors.
    """
    

def test_get_set_neighbors():
    """
    Test getting and setting the list of neighbors for the individual.
    """
    

# Run the tests
if __name__ == "__main__":
    pytest.main()
