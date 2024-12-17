
import math
from mpmath import power as pw
from typing import List

from pycellga.problems.abstract_problem import AbstractProblem
from pycellga.common import GeneType


class Levy(AbstractProblem):
    """
    Levy function implementation for optimization problems.

    The Levy function is widely used for testing optimization algorithms.
    It evaluates inputs over the hypercube x_i ∈ [-10, 10].

    Attributes
    ----------
    n_var : int
        Number of variables (dimensions) in the problem.
    gen_type : GeneType
        Type of genes used in the problem (REAL).
    xl : float
        Lower bounds for the variables, fixed to -10.
    xu : float
        Upper bounds for the variables, fixed to 10.

    Methods
    -------
    f(x: List[float]) -> float
        Compute the Levy function value for a given solution.
    evaluate(x: List[float], out: dict, *args, **kwargs) -> None
        Pymoo-compatible evaluation method for batch processing.
    """

    def __init__(self, n_var: int = 2):
        """
        Initialize the Levy problem.

        Parameters
        ----------
        n_var : int, optional
            Number of variables (dimensions) for the problem, by default 2.
        """
        gen_type = GeneType.REAL
        xl = -10.0
        xu = 10.0

        super().__init__(gen_type=gen_type, n_var=n_var, xl=xl, xu=xu)

    def f(self, x: List[float]) -> float:
        """
        Compute the Levy function value for a given solution.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The Levy function value.
        """
        if len(x) != self.n_var:
            raise ValueError(f"Input must have exactly {self.n_var} variables.")

        fitness = 0.0
        for i in range(self.n_var - 1):
            term1 = pw(math.sin(3 * x[i] * math.pi), 2)
            term2 = (pw((x[i] - 1), 2)) * (1 + pw(math.sin(3 * x[i + 1] * math.pi), 2))
            term3 = (pw((x[i + 1] - 1), 2)) * (1 + pw(math.sin(2 * x[i + 1] * math.pi), 2))
            fitness += term1 + term2 + term3

        return round(fitness, 3)

    def evaluate(self, x: List[float], out: dict, *args, **kwargs) -> None:
        """
        Evaluate method for compatibility with pymoo's framework.

        Parameters
        ----------
        x : numpy.ndarray
            Array of input variables.
        out : dict
            Dictionary to store the output fitness values.
        """
        out["F"] = self.f(x)
