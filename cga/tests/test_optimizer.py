from optimizer import *
from problems.combinatorial.one_max import OneMax
from mutation.bit_flip_mutation import *
from recombination.one_point_crossover import *
from selection.tournament_selection import *
from population import *
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


def test_optimizer():

    res = optimize()
    assert type(res) == tuple
    assert type(res[0]) == dict
    assert type(res[1]) == list
    assert type(res[2]) == list
