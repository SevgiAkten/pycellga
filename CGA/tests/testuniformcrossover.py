from grid import Grid
import sys
sys.path.append('..')

from individual import Individual
from recombination.uniformcrossover import UniformCrossover

def test_uniformcrossover():

    CHSIZE = 10

    indv1 = Individual(gen_type = "Binary", ch_size = CHSIZE)
    indv2 = Individual(gen_type = "Binary", ch_size = CHSIZE)
    
    indv1.randomize()
    indv2.randomize()

    parents = [indv1, indv2]
    
    ucx = UniformCrossover(parents, None)
    child1, child2 = ucx.get_recombinations()
    
    assert len(child1) == len(child2)
    assert len(child1) == CHSIZE

    for i in range(CHSIZE): 
        assert child1[i] == 1 or child1[i] == 0
    
    for i in range(CHSIZE):
        assert child2[i] == 1 or child2[i] == 0

