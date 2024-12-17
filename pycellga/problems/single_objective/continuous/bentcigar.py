
from mpmath import power as pw
from typing import List

from pycellga.problems.abstract_problem import AbstractProblem
from pycellga.common import GeneType


class Bentcigar(AbstractProblem):
    """
    Bentcigar function implementation for optimization problems.

    The Bentcigar function is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x_i ∈ [-100, 100], for all i = 1, 2, ..., n.

    Attributes
    ----------
    n_var : int
        Number of variables (dimensions) in the problem.
    gen_type : GeneType
        Type of genes used in the problem (fixed to REAL).
    xl : float
        Lower bound for each variable (fixed to -100).
    xu : float
        Upper bound for each variable (fixed to 100).

    Methods
    -------
    f(x: List[float]) -> float
        Compute the Bentcigar function value for a single solution.

    Notes
    -----
    -100 ≤ xi ≤ 100 for i = 1,…,n
    Global minimum at f(0,...,0) = 0
    """

    def __init__(self, n_var: int):
        """
        Initialize the Bentcigar problem.

        Parameters
        ----------
        n_var : int
            Number of variables (dimensions) in the problem.
        """
        gen_type = GeneType.REAL  
        xl = -100.0
        xu = 100.0

        super().__init__(gen_type=gen_type, n_var=n_var, xl=xl, xu=xu)

    def f(self, x: List[float]) -> float:
        """
        Compute the Bentcigar function value for a single solution.

        Parameters
        ----------
        x : list or numpy.ndarray
            Array of input variables.

        Returns
        -------
        float
            The computed fitness value for the given solution.
        """
        a = pw(x[0], 2)  
        b = pw(10, 6)    
        sum_val = sum(pw(xi, 2) for xi in x[1:])  

        fitness = a + (b * sum_val)
        return round(fitness, 3)
