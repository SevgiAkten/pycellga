import pytest
import mpmath as mp
from typing import List

from optimizer import alpha_cga
from common import GeneType
from recombination import ByteOnePointCrossover, OnePointCrossover, PMXCrossover
from mutation import ByteMutationRandom, BitFlipMutation, SwapMutation
from selection import TournamentSelection
from problems import AbstractProblem


class RealProblem(AbstractProblem):
    
    def __init__(self, n_var):

        super().__init__(
            gen_type=GeneType.REAL,
            n_var=n_var,
            xl=-100, 
            xu=100
        )
    
    def f(self, x):
        
        return sum(mp.power(xi, 2) for xi in x)

def test_optimizer_alpha_cga_real():
    """Test alpha_cga on a real-valued sum of squares problem."""
    result = alpha_cga(
        n_cols=5,
        n_rows=5,
        n_gen=50,
        ch_size=5,
        p_crossover=0.9,
        p_mutation=0.2,
        problem=RealProblem(n_var=5),
        selection=TournamentSelection,
        recombination=ByteOnePointCrossover,
        mutation=ByteMutationRandom
        
    )
    assert result.fitness_value == 0.0, "The alpha_cga did not find the global minimum."
    assert result.chromosome == [0.0] * 5, "The chromosome does not match the global minimum."

class BinaryProblem(AbstractProblem):

    
    def __init__(self, n_var):

        super().__init__(
            gen_type=GeneType.BINARY,
            n_var=n_var,
            xl=0, 
            xu=1
        )
    
    def f(self, x):
        
        return -sum(x)

def test_optimizer_alpha_cga_binary():

    result = alpha_cga(
        n_cols=5,
        n_rows=5,
        n_gen=50,
        ch_size=10,
        p_crossover=0.9,
        p_mutation=0.2,
        problem=BinaryProblem(n_var=10),
        selection=TournamentSelection,
        recombination=OnePointCrossover,
        mutation=BitFlipMutation,
    )
    assert result.fitness_value == -10, "The alpha_cga did not maximize the number of 1s."
    assert result.chromosome == [1] * 10, "The chromosome does not match the optimal binary sequence."

class PermutationProblem(AbstractProblem):
  
    def __init__(self, n_var, target: List[int]):

        super().__init__(
                gen_type=GeneType.PERMUTATION,
                n_var=n_var,
                xl=1, 
                xu=10
            )
        self.target = target
    
    def f(self, x: List[int]) -> float:
      
        return sum(abs(xi - ti) for xi, ti in zip(x, self.target))


    def test_optimizer_alpha_cga_permutation(self):
        
        target_permutation = [i for i in range(10)]
        problem = PermutationProblem(target=target_permutation)

        result = alpha_cga(
            n_cols=5,
            n_rows=5,
            n_gen=50,
            ch_size=10,
            p_crossover=0.9,
            p_mutation=0.2,
            problem=problem.f(target_permutation),
            selection=TournamentSelection,
            recombination=PMXCrossover,
            mutation=SwapMutation
        )

        # Assert that the alpha_cga finds the global minimum
        print(result.fitness_value)
        print(result.chromosome)
        assert result.fitness_value == 0.0, "The alpha_cga did not find the global minimum."
        assert result.chromosome == target_permutation, "The chromosome does not match the target permutation."


if __name__ == "__main__":
    pytest.main()
