from problems.abstract_problem import AbstractProblem
from common import GeneType
import numpy as np
from mpmath import power as pw
class Sumofdifferentpowers(AbstractProblem):
    """
    Sum of Different Powers function implementation for optimization problems.

    The Sum of Different Powers function is commonly used to test optimization algorithms.
    It is defined over the range [-1, 1] for each variable, with a global minimum of 0 at the origin.

    Attributes
    ----------
    n_var : int
        Number of variables (dimensions) in the problem.
    gen_type : GeneType
        Type of genes used in the problem (fixed to REAL).
    xl : float
        Lower bounds for the variables (fixed to -1).
    xu : float
        Upper bounds for the variables (fixed to 1).

    Methods
    -------
    f(x: list) -> float
        Compute the Sum of Different Powers function value for a given solution.

    Notes
    -----
    -1 ≤ xi ≤ 1 for all i.
    Global minimum at f(0,...,0) = 0.
    """

    def __init__(self, n_var: int = 2):
        """
        Initialize the Sum of Different Powers problem.

        Parameters
        ----------
        n_var : int, optional
            Number of variables (dimensions) in the problem, by default 2.
        """
        gen_type = GeneType.REAL
        xl = -1.0
        xu = 1.0

        super().__init__(gen_type=gen_type, n_var=n_var, xl=xl, xu=xu)

    def f(self, x: list) -> float:
        """
        Compute the Sum of Different Powers function value for a given solution.

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

        fitness = sum(pw(np.abs(xi), i + 1) for i, xi in enumerate(x))
        return round(fitness, 3)

    def evaluate(self, x, out, *args, **kwargs):
        """
        Evaluate function for compatibility with pymoo's optimizer.

        Parameters
        ----------
        x : numpy.ndarray
            Array of input variables.
        out : dict
            Dictionary to store the output fitness values.
        """
        out["F"] = self.f(x)
