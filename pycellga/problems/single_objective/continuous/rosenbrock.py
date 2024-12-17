from typing import List
from mpmath import power as pw

from pycellga.problems.abstract_problem import AbstractProblem
from pycellga.common import GeneType


class Rosenbrock(AbstractProblem):
    """
    Rosenbrock function implementation for optimization problems.

    The Rosenbrock function is widely used for testing optimization algorithms.
    The function is usually evaluated on the hypercube x_i ∈ [-5, 10], for all i = 1, 2, ..., n.

    Attributes
    ----------
    n_var : int
        Number of variables (dimensions) in the problem.
    gen_type : GeneType
        Type of genes used in the problem (fixed to REAL).
    xl : float
        Lower bounds for the variables (fixed to -5).
    xu : float
        Upper bounds for the variables (fixed to 10).

    Methods
    -------
    f(x: List[float]) -> float
        Compute the Rosenbrock function value for a single solution.
    """

    def __init__(self, n_var: int = 2):
        """
        Initialize the Rosenbrock problem.

        Parameters
        ----------
        n_var : int, optional
            Number of variables (dimensions) in the problem, by default 2.
        """
        gen_type = GeneType.REAL
        xl = -5.0
        xu = 10.0

        super().__init__(gen_type=gen_type, n_var=n_var, xl=xl, xu=xu)

    def f(self, x: List[float]) -> float:
        """
        Compute the Rosenbrock function value for a single solution.

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

        fitness = sum([(100 * pw((x[i + 1] - pw(x[i], 2)), 2)) + pw((1 - x[i]), 2) for i in range(self.n_var - 1)])
        return round(fitness, 3)
