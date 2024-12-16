from numpy import cos, pi
from mpmath import power as pw
from typing import List
from problems.abstract_problem import AbstractProblem
from common import GeneType

class Bohachevsky(AbstractProblem):
    """
    Bohachevsky function implementation for optimization problems.

    The Bohachevsky function is widely used for testing optimization algorithms.
    It is usually evaluated on the hypercube x_i ∈ [-15, 15], for all i = 1, 2, ..., n.

    Attributes
    ----------
    n_var : int
        Number of variables (dimensions) in the problem.
    gen_type : GeneType
        Type of genes used in the problem (fixed to REAL).
    xl : float
        Lower bound for each variable (fixed to -15).
    xu : float
        Upper bound for each variable (fixed to 15).

    Methods
    -------
    f(x: List[float]) -> float
        Compute the Bohachevsky function value for a single solution.

    Notes
    -----
    -15 ≤ xi ≤ 15 for i = 1,…,n
    Global minimum at f(0,...,0) = 0
    """

    def __init__(self, n_var: int):
        """
        Initialize the Bohachevsky problem.

        Parameters
        ----------
        n_var : int
            Number of variables (dimensions) in the problem.
        """
        gen_type = GeneType.REAL
        xl = -15.0
        xu = 15.0

        super().__init__(gen_type=gen_type, n_var=n_var, xl=xl, xu=xu)

    def f(self, x: List[float]) -> float:
        """
        Compute the Bohachevsky function value for a single solution.

        Parameters
        ----------
        x : list or numpy.ndarray
            Array of input variables.

        Returns
        -------
        float
            The computed fitness value for the given solution.
        """
        fitness = sum([
            pw(x[i], 2) + (2 * pw(x[i + 1], 2)) 
            - (0.3 * cos(3 * pi * x[i])) 
            - (0.4 * cos(4 * pi * x[i + 1])) + 0.7
            for i in range(len(x) - 1)
        ])
        return round(fitness, 3)
