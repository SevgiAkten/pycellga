from problems.abstract_problem import AbstractProblem
from mpmath import power as pw
from typing import List
from common import GeneType


class Holzman(AbstractProblem):
    """
    Holzman function implementation for optimization problems.

    The Holzman function is widely used for testing optimization algorithms.
    It is usually evaluated on the hypercube xi ∈ [-10, 10], for all i = 1, 2, ..., n.

    Attributes
    ----------
    n_var : int
        Number of variables (dimensions) in the problem.
    gen_type : GeneType
        Type of genes used in the problem (fixed to REAL).
    xl : float
        Lower bound for the variables (fixed to -10).
    xu : float
        Upper bound for the variables (fixed to 10).

    Methods
    -------
    f(x: List[float]) -> float
        Compute the Holzman function value for a single solution.

    Notes
    -----
    -10 ≤ xi ≤ 10 for i = 1,…,n
    Global minimum at f(0,...,0) = 0
    """

    def __init__(self, n_var: int = 2):
        """
        Initialize the Holzman problem.

        Parameters
        ----------
        n_var : int, optional
            Number of variables (dimensions) in the problem, by default 2.
        """
        gen_type = GeneType.REAL
        xl = -10.0
        xu = 10.0

        super().__init__(gen_type=gen_type, n_var=n_var, xl=xl, xu=xu)

    def f(self, x: List[float]) -> float:
        """
        Compute the Holzman function value for a single solution.

        Parameters
        ----------
        x : list or numpy.ndarray
            Array of input variables.

        Returns
        -------
        float
            The computed fitness value for the given solution.
        """
        fitness = sum((i + 1) * pw(x[i], 4) for i in range(len(x)))
        return round(fitness, 3)
