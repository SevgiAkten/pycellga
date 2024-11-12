import pytest
from optimizer import ccga, GeneType, TournamentSelection, ByteOnePointCrossover, ByteMutationRandom, OnePointCrossover, BitFlipMutation, PMXCrossover, SwapMutation
from typing import List

class BinaryProblem:
    """
    Example problem class to be maximized for binary chromosomes.

    This class implements the OneMax problem where the goal is to maximize the number of 1s in a binary string.
    """
    
    def __init__(self):
        pass
    
    def f(self, x):
        """
        Compute the objective function value.

        This method counts the number of 1s in the binary chromosome.

        Parameters
        ----------
        x : list or numpy.ndarray
            The input chromosome represented as a list or array of binary values (0s and 1s).

        Returns
        -------
        int
            The computed value, which is the count of 1s in the chromosome.
        """
        return sum(x)

def test_optimizer_ccga_binary():
    """Test ccga on a binary OneMax problem."""
    result = ccga(
        n_cols=5,
        n_rows=5,
        n_gen=200,
        ch_size=5,
        gen_type=GeneType.BINARY,
        problem=BinaryProblem(),
        selection=TournamentSelection,
        mins=[0] * 5,
        maxs=[1] * 5 
    )
    assert result.fitness_value == 5, "The ccga did not maximize the number of 1s."
    assert result.chromosome == [1] * 5, "The chromosome does not match the optimal binary sequence."

if __name__ == "__main__":
    pytest.main()
