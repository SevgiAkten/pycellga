import pytest
import mpmath as mp

from pycellga.optimizer import mcccga
from pycellga.common import GeneType
from pycellga.selection.tournament_selection import TournamentSelection
from pycellga.problems.abstract_problem import AbstractProblem

class RealProblem(AbstractProblem):
    
    def __init__(self, n_var):

        super().__init__(
            gen_type=GeneType.REAL,
            n_var=n_var,
            xl=-3.768, 
            xu=3.768
        )
    
    def f(self, x):
        
        return sum(mp.power(xi, 2) for xi in x)

def test_optimizer_mccga_binary():

    result = mcccga(
        n_cols=5,
        n_rows=5,
        n_gen=500,
        ch_size=5,
        problem=RealProblem(n_var=5),
        selection=TournamentSelection
    )
    assert result.fitness_value == 0.0, "The mcccga did not find the global minimum."
    assert result.chromosome == [0.0] * 5, "The chromosome does not match the global minimum."

if __name__ == "__main__":
    pytest.main()
