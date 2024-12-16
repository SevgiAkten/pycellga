from numpy import pi, e, cos, sqrt, exp, power
from problems.abstract_problem import AbstractProblem
from typing import List
from common import GeneType


class Ackley(AbstractProblem):
    """
    Ackley function implementation for optimization problems.

    The Ackley function is widely used for testing optimization algorithms.
    It is characterized by a nearly flat outer region and a large hole at the center.
    The function is usually evaluated on the hypercube x_i ∈ [-32.768, 32.768], for all i = 1, 2, ..., d.

    Attributes
    ----------
    n_var : int
        Number of variables (dimensions) in the problem.
    gen_type : GeneType
        Type of genes used in the problem (fixed to REAL).
    xl : float
        Lower bound for each variable (fixed to -32.768).
    xu : float
        Upper bound for each variable (fixed to 32.768).

    Methods
    -------
    __init__(n_var: int)
        Initialize the Ackley problem with the specified number of variables.

    f(x: List[float]) -> float
        Compute the Ackley function value for a single solution.

        Parameters
        ----------
        x : list or numpy.ndarray
            Array of input variables.

        Returns
        -------
        float
            The computed fitness value for the given solution.
    """

    def __init__(self, n_var):
        """
        Initialize the Ackley problem.

        Parameters
        ----------
        n_var : int
            Number of variables (dimensions) in the problem.
        """
        gen_type = GeneType.REAL
        xl = -32.768
        xu = 32.768

        super().__init__(gen_type=gen_type, n_var=n_var, xl=xl, xu=xu)

    def f(self, x: List[float]) -> float:
        """
        Compute the Ackley function value for a single solution.

        Parameters
        ----------
        x : list or numpy.ndarray
            Array of input variables.

        Returns
        -------
        float
            The computed fitness value for the given solution.
        """
        sum1 = sum(power(gene, 2) for gene in x)
        sum2 = sum(cos(2 * pi * gene) for gene in x)

        fitness = -20.0 * exp(-0.2 * sqrt(sum1 / self.n_var)) - exp(sum2 / self.n_var) + 20.0 + e
        return round(fitness, 3)
