import pytest
from optimizer import cga, GeneType, TournamentSelection, ByteOnePointCrossover, ByteMutationRandom, OnePointCrossover, BitFlipMutation, PMXCrossover, SwapMutation
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

def test_optimizer_cga_real():
    """Test CGA on a real-valued sum of squares problem."""
    result = cga(
        n_cols=5,
        n_rows=5,
        n_gen=100,
        ch_size=5,
        gen_type=GeneType.REAL,
        p_crossover=0.9,
        p_mutation=0.2,
        problem=RealProblem(),
        selection=TournamentSelection,
        recombination=ByteOnePointCrossover,
        mutation=ByteMutationRandom,
        mins=[-32.768] * 5,
        maxs=[32.768] * 5
    )
    assert result.fitness_value == 0.0, "The CGA did not find the global minimum."
    assert result.chromosome == [0.0] * 5, "The chromosome does not match the global minimum."

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
        return -sum(x)

def test_optimizer_cga_binary():
    """Test CGA on a binary OneMax problem."""
    result = cga(
        n_cols=5,
        n_rows=5,
        n_gen=50,
        ch_size=10,
        gen_type=GeneType.BINARY,
        p_crossover=0.9,
        p_mutation=0.2,
        problem=BinaryProblem(),
        selection=TournamentSelection,
        recombination=OnePointCrossover,
        mutation=BitFlipMutation,
        mins=[0] * 10,
        maxs=[1] * 10
    )
    assert result.fitness_value == -10, "The CGA did not maximize the number of 1s."
    assert result.chromosome == [1] * 10, "The chromosome does not match the optimal binary sequence."



class PermutationProblem:
    """
    Example problem class to be minimized using a permutation-based approach.

    This class implements a simple objective function that measures the sum of absolute differences
    between the chromosome and a target permutation.
    """
    
    def __init__(self, target: List[int]):
        """
        Initialize the PermutationProblem with a target permutation.

        Parameters
        ----------
        target : list of int
            The target permutation that the algorithm aims to find.
        """
        self.target = target
    
    def f(self, x: List[int]) -> float:
        """
        Compute the objective function value.

        This method implements the sum of absolute differences function.

        Parameters
        ----------
        x : list
            The input chromosome represented as a list of integers (permutation).

        Returns
        -------
        float
            The computed value of the function given the input x.
        """
        return sum(abs(xi - ti) for xi, ti in zip(x, self.target))


    def test_optimizer_cga_permutation(self):
        """
        Test CGA on a permutation-based problem where the target is the identity permutation.
        """
        target_permutation = [i for i in range(10)]
        problem = PermutationProblem(target=target_permutation)

        result = cga(
            n_cols=5,
            n_rows=5,
            n_gen=50,
            ch_size=10,
            gen_type=GeneType.PERMUTATION,
            p_crossover=0.9,
            p_mutation=0.2,
            problem=problem.f(target_permutation),
            selection=TournamentSelection(),
            recombination=PMXCrossover(),
            mutation=SwapMutation(),
            mins=[0] * 10,
            maxs=[9] * 10
        )

        # Assert that the CGA finds the global minimum
        print(result.chromosome)
        print(result.fitness_value)
        assert result.fitness_value == 0.0, "The CGA did not find the global minimum."
        assert result.chromosome == target_permutation, "The chromosome does not match the target permutation."


def test_optimizer_cga_no_variation():
    """Test CGA with no crossover or mutation."""
    result = cga(
        n_cols=5,
        n_rows=5,
        n_gen=50,
        ch_size=5,
        gen_type=GeneType.REAL,
        p_crossover=0.0,
        p_mutation=0.0,
        problem=RealProblem(),
        selection=TournamentSelection,
        recombination=ByteOnePointCrossover,
        mutation=ByteMutationRandom,
        mins=[-32.768] * 5,
        maxs=[32.768] * 5
    )
    assert result.fitness_value != 0.0, "With no crossover or mutation, the solution should not reach the global minimum."



if __name__ == "__main__":
    pytest.main()
