import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from optimizer import ccga
from selection import TournamentSelection
from problems import AbstractProblem
from common import GeneType

class ExampleProblem(AbstractProblem):

    def __init__(self, n_var):

        super().__init__(
            gen_type=GeneType.BINARY,
            n_var=n_var,
            xl=0, 
            xu=1
        )
    
    def f(self, x):
        return sum(x)

def run_ccga_example():

    result = ccga(
        n_cols=5,
        n_rows=5,
        n_gen=200,
        ch_size=10,
        problem=ExampleProblem(n_var=10),
        selection=TournamentSelection
    )

    # Print the results
    print("Best solution chromosome:", result.chromosome)
    print("Best fitness value:", result.fitness_value)

if __name__ == "__main__":
    run_ccga_example()
