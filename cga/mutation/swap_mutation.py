# Mutation for permutation representation. Swaps the place of two genes.
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from individual import *

class SwapMutation:
    def __init__(self, mutation_cand:list):
        self.mutation_cand = mutation_cand

    def mutate(self) -> Individual:

        return None
