import pytest

from pycellga.optimizer import ccga
from pycellga.selection.tournament_selection import TournamentSelection
from pycellga.common import GeneType
from pycellga.problems.abstract_problem import AbstractProblem

class BinaryProblem(AbstractProblem):

    def __init__(self, n_var):

        super().__init__(
            gen_type=GeneType.BINARY,
            n_var=n_var,
            xl=0, 
            xu=1
        )
    
    def f(self, x):
        
        return sum(x)

def test_optimizer_ccga_binary():

    result = ccga(
        n_cols=5,
        n_rows=5,
        n_gen=200,
        ch_size=5,
        problem=BinaryProblem(n_var=5),
        selection=TournamentSelection
    )

    assert result.fitness_value == 5, "The ccga did not maximize the number of 1s."
    assert result.chromosome == [1] * 5, "The chromosome does not match the optimal binary sequence."

if __name__ == "__main__":
    pytest.main()
