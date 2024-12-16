from problems.abstract_problem import AbstractProblem
import math
from typing import List
from common import GeneType


class Griewank(AbstractProblem):
    """
    Griewank function implementation for optimization problems.

    The Griewank function is widely used for testing optimization algorithms.
    It is usually evaluated on the hypercube xi ∈ [-600, 600], for all i = 1, 2, ..., n.

    Attributes
    ----------
    n_var : int
        Number of variables (dimensions) in the problem.
    gen_type : GeneType
        Type of genes used in the problem (fixed to REAL).
    xl : float
        Lower bound for the variables (fixed to -600).
    xu : float
        Upper bound for the variables (fixed to 600).

    Methods
    -------
    f(x: List[float]) -> float
        Compute the Griewank function value for a single solution.

    Notes
    -----
    -600 ≤ xi ≤ 600 for i = 1,…,n
    Global minimum at f(0,...,0) = 0
    """

    def __init__(self, n_var: int = 10):
        """
        Initialize the Griewank problem.

        Parameters
        ----------
        n_var : int, optional
            Number of variables (dimensions) in the problem, by default 10.
        """
        gen_type = GeneType.REAL
        xl = -600.0
        xu = 600.0

        super().__init__(gen_type=gen_type, n_var=n_var, xl=xl, xu=xu)

    def f(self, x: List[float]) -> float:
        """
        Compute the Griewank function value for a single solution.

        Parameters
        ----------
        x : list or numpy.ndarray
            Array of input variables.

        Returns
        -------
        float
            The computed fitness value for the given solution.
        """
        sum_sq = sum(xi ** 2 for xi in x)
        prod_cos = math.prod(math.cos(xi / math.sqrt(i + 1)) for i, xi in enumerate(x))
        fitness = 1 + sum_sq / 4000 - prod_cos
        return round(fitness, 3)
