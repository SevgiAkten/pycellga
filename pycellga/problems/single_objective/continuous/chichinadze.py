import numpy as np
from typing import List
from problems.abstract_problem import AbstractProblem
from common import GeneType


class Chichinadze(AbstractProblem):
    """
    Chichinadze function implementation for optimization problems.

    The Chichinadze function is widely used for testing optimization algorithms.
    It is usually evaluated on the hypercube x, y ∈ [-30, 30].

    Attributes
    ----------
    n_var : int
        Number of variables (fixed to 2 for x and y).
    gen_type : GeneType
        Type of genes used in the problem (fixed to REAL).
    xl : float
        Lower bound for the variables (fixed to -30).
    xu : float
        Upper bound for the variables (fixed to 30).

    Methods
    -------
    f(x: List[float]) -> float
        Compute the Chichinadze function value for a single solution.

    Notes
    -----
    -30 ≤ x, y ≤ 30
    Global minimum at f(5.90133, 0.5) = −43.3159
    """

    def __init__(self):
        """
        Initialize the Chichinadze problem.
        """
        gen_type = GeneType.REAL
        n_var = 2  # Fixed to 2 for x and y
        xl = -30.0
        xu = 30.0

        super().__init__(gen_type=gen_type, n_var=n_var, xl=xl, xu=xu)

    def f(self, x: List[float]) -> float:
        """
        Compute the Chichinadze function value for a single solution.

        Parameters
        ----------
        x : list or numpy.ndarray
            Array of input variables.

        Returns
        -------
        float
            The computed fitness value for the given solution.
        """
        x_val, y_val = x[0], x[1]
        term1 = x_val**2 - 12 * x_val + 11
        term2 = 10 * np.cos(np.pi * x_val / 2)
        term3 = 8 * np.sin(5 * np.pi * x_val)
        term4 = (1.0 / np.sqrt(5)) * np.exp(-((y_val - 0.5)**2) / 2)
        fitness = term1 + term2 + term3 - term4

        return round(fitness, 4)
