import pytest
from optimizer import mcccga, GeneType, TournamentSelection, ByteOnePointCrossover, ByteMutationRandom, OnePointCrossover, BitFlipMutation, PMXCrossover, SwapMutation
import mpmath as mp
from typing import List

class RealProblem:
    """
    Example problem class to be minimized.

    This class implements a simple sum of squares function with a global minimum value of 0,
    achieved when all elements of the chromosome are equal to 0.
    """
    
    def __init__(self):
        pass
    
    def f(self, x):
        """
        Compute the objective function value.

        This method implements the sum of squares function.

        Parameters
        ----------
        x : list or numpy.ndarray
            The input chromosome represented as a list or array of real values.

        Returns
        -------
        float
            The computed value of the function given the input x.
        """
        return sum(mp.power(xi, 2) for xi in x)

def test_optimizer_mcccga_binary():
    """Test mcccga on a binary OneMax problem."""
    result = mcccga(
        n_cols=5,
        n_rows=5,
        n_gen=500,
        ch_size=5,
        gen_type=GeneType.REAL,
        problem=RealProblem(),
        selection=TournamentSelection,
        mins=[-3.768] * 5,
        maxs=[3.768] * 5
    )
    assert result.fitness_value == 0.0, "The mcccga did not find the global minimum."
    assert result.chromosome == [0.0] * 5, "The chromosome does not match the global minimum."

if __name__ == "__main__":
    pytest.main()
