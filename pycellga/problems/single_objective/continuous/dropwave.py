from problems.abstract_problem import AbstractProblem
from numpy import power, cos, sqrt
from typing import List
from common import GeneType


class Dropwave(AbstractProblem):
    """
    Dropwave function for optimization problems.

    The Dropwave function is a multimodal function commonly used as a performance test problem for optimization algorithms.
    It is defined within the bounds -5.12 ≤ xi ≤ 5.12 for i = 1, 2, and has a global minimum at f(0, 0) = -1.

    Attributes
    ----------
    n_var : int
        Number of variables (dimensions) in the problem (fixed to 2).
    gen_type : GeneType
        Type of genes used in the problem (fixed to REAL).
    xl : float
        Lower bound for the variables (fixed to -5.12).
    xu : float
        Upper bound for the variables (fixed to 5.12).

    Methods
    -------
    f(x: List[float]) -> float
        Compute the Dropwave function value for a single solution.

    Notes
    -----
    -5.12 ≤ xi ≤ 5.12 for i = 1, 2
    Global minimum at f(0, 0) = -1
    """

    def __init__(self):
        """
        Initialize the Dropwave problem.
        """
        gen_type = GeneType.REAL
        n_var = 2  # Fixed to 2 for x1 and x2
        xl = -5.12
        xu = 5.12

        super().__init__(gen_type=gen_type, n_var=n_var, xl=xl, xu=xu)

    def f(self, x: List[float]) -> float:
        """
        Compute the Dropwave function value for a single solution.

        Parameters
        ----------
        x : list or numpy.ndarray
            Array of input variables.

        Returns
        -------
        float
            The computed fitness value for the given solution.
        """
        if len(x) != self.n_var:
            raise ValueError(f"Input must have exactly {self.n_var} variables.")
        
        x1, x2 = x
        sqrts_sums = power(x1, 2) + power(x2, 2)
        denominator = 0.5 * sqrts_sums + 2
        fitness = -(1 + cos(12 * sqrt(sqrts_sums))) / denominator
        return round(fitness, 3)
