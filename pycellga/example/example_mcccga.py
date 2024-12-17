
import numpy as np

from pycellga.optimizer import mcccga
from pycellga.selection.tournament_selection import TournamentSelection
from pycellga.problems.abstract_problem import AbstractProblem
from pycellga.common import GeneType

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
