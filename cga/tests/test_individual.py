import pytest
from numpy import random
import random as rd
from cga.individual import Individual 

@pytest.fixture
def setup_individual():
    """
    Fixture to provide an instance of the Individual class with different configurations.
    """
    return Individual(gen_type="Binary", ch_size=10)

def test_individual_init():
    """
    Test the initialization of the Individual class.
    """
    ind = Individual(gen_type="Binary", ch_size=10)
    assert ind.gen_type == "Binary"
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
    ind = Individual(gen_type="Binary", ch_size=10)
    ind.randomize()
    assert len(ind.chromosome) == 10
    assert all(gene in [0, 1] for gene in ind.chromosome)

def test_randomize_permutation():
    """
    Test the randomization of the chromosome for a permutation genome type.
    """
    ind = Individual(gen_type="Permutation", ch_size=10)
    ind.randomize()
    assert len(ind.chromosome) == 10
    assert set(ind.chromosome).issubset(set(range(1, 15)))
    assert len(set(ind.chromosome)) == len(ind.chromosome)

def test_randomize_real_valued():
    """
    Test the randomization of the chromosome for a real-valued genome type.
    """
    ind = Individual(gen_type="Real-valued", ch_size=10)
    ind.randomize()
    assert len(ind.chromosome) == 10
    assert all(isinstance(gene, float) for gene in ind.chromosome)

def test_generate_candidate():
    """
    Test the generation of a candidate chromosome based on a given probability vector.
    """
    ind = Individual(gen_type="Binary", ch_size=10)
    vector = [0.5] * 10
    candidate = ind.generate_candidate(vector)
    assert len(candidate) == 10
    assert all(gene in [0, 1] for gene in candidate)

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
