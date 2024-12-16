import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np

from optimizer import mcccga
from selection import TournamentSelection
from problems import AbstractProblem
from common import GeneType

class RealProblem(AbstractProblem):

    
    def __init__(self, n_var):

        super().__init__(
            gen_type=GeneType.REAL,
            n_var=n_var,
            xl=-3.768, 
            xu=3.768
        )
    
    def f(self, x):

        return sum(np.power(xi, 2) for xi in x)

def run_mcccga_example():

    result = mcccga(
        n_cols=5,
        n_rows=5,
        n_gen=500,
        ch_size=5,
        problem=RealProblem(n_var=5),
        selection=TournamentSelection
    )

    # Print the results
    print("Best solution chromosome:", result.chromosome)
    print("Best fitness value:", result.fitness_value)

if __name__ == "__main__":
    run_mcccga_example()
