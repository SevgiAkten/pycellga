from problems.abstract_problem import AbstractProblem
from common import GeneType
from mpmath import power as pw
from typing import List

class Powell(AbstractProblem):
    """
    Powell function implementation for optimization problems.

    The Powell function is widely used for testing optimization algorithms.
    It is typically evaluated on the hypercube x_i ∈ [-4, 5], for all i = 1, 2, ..., n.
    
    Attributes
    ----------
    n_var : int
        Number of variables (dimensions) in the problem.
    gen_type : GeneType
        Type of genes used in the problem (REAL for this implementation).
    xl : float
        Lower bound for the variables (fixed to -4).
    xu : float
        Upper bound for the variables (fixed to 5).

    Methods
    -------
    f(x: List[float]) -> float
        Compute the Powell function value for a given solution.
    """

    def __init__(self, n_var: int = 4):
        """
        Initialize the Powell problem.

        Parameters
        ----------
        n_var : int, optional
            Number of variables (dimensions) in the problem, by default 4.
        """
        gen_type = GeneType.REAL
        xl = -4.0
        xu = 5.0

        super().__init__(gen_type=gen_type, n_var=n_var, xl=xl, xu=xu)

    def f(self, x: List[float]) -> float:
        """
        Compute the Powell function value for a given solution.

        Parameters
        ----------
        x : list of float
            A list of float variables representing a point in the solution space.

        Returns
        -------
        float
            The computed fitness value for the given solution.
        """
        if len(x) % 4 != 0:
            raise ValueError("Powell function requires the number of variables to be a multiple of 4.")

        fitness = 0.0
        d = len(x) // 4
        
        for i in range(d):
            a = pw(x[4 * i] + 10 * x[4 * i + 1], 2)
            b = pw(x[4 * i + 2] - x[4 * i + 3], 2)
            c = pw(x[4 * i + 1] - 2 * x[4 * i + 2], 4)
            e = pw(x[4 * i] - x[4 * i + 3], 4)
            fitness += a + 5 * b + c + 10 * e

        return round(fitness, 1)
