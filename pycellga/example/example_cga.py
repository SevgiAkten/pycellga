import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mpmath import power as pw
from typing import List

from optimizer import cga
from recombination import ByteOnePointCrossover
from mutation import ByteMutationRandom
from selection import TournamentSelection
from problems import AbstractProblem
from common import GeneType

class ExampleProblem(AbstractProblem):

    def __init__(self, n_var):

        super().__init__(
            gen_type=GeneType.REAL,
            n_var=n_var,
            xl=-100, 
            xu=100
        )

    def f(self, x: List[float]) -> float:
        return round(sum(pw(xi, 2) for xi in x),3)


def run_cga_example():

    result = cga(
        n_cols=5,
        n_rows=5,
        n_gen=100,
        ch_size=5,
        p_crossover=0.9,
        p_mutation=0.2,
        problem=ExampleProblem(n_var=5),
        selection=TournamentSelection,
        recombination=ByteOnePointCrossover,
        mutation=ByteMutationRandom,
        seed_par=100
    )

    # Print the results
    print("Best solution chromosome:", result.chromosome)
    print("Best fitness value:", result.fitness_value)

if __name__ == "__main__":
    run_cga_example()
