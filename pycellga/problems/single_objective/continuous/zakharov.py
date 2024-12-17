from mpmath import power as pw
from typing import List

from pycellga.problems.abstract_problem import AbstractProblem
from pycellga.common import GeneType


class Zakharov(AbstractProblem):
    """
    Zakharov function implementation for optimization problems.

    The Zakharov function is widely used for testing optimization algorithms.
    It is evaluated on the hypercube x_i ∈ [-5, 10] for all variables.

    Attributes
    ----------
    n_var : int
        Number of variables (dimensions) in the problem.
    gen_type : GeneType
        Type of genes used in the problem (REAL).
    xl : float
        Lower bounds for the variables, fixed to -5.
    xu : float
        Upper bounds for the variables, fixed to 10.

    Methods
    -------
    f(x: list) -> float
        Compute the Zakharov function value for a given solution.
    evaluate(x: list, out: dict, *args, **kwargs) -> None
        Pymoo-compatible evaluation method for batch processing.
    """

    def __init__(self, n_var: int = 2):
        """
        Initialize the Zakharov problem.

        Parameters
        ----------
        n_var : int, optional
            Number of variables (dimensions) for the problem, by default 2.
        """
        gen_type = GeneType.REAL
        xl = -5.0
        xu = 10.0

        super().__init__(gen_type=gen_type, n_var=n_var, xl=xl, xu=xu)

    def f(self, x: List[float]) -> float:
        """
        Compute the Zakharov function value for a given solution.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The Zakharov function value.
        """
        if len(x) != self.n_var:
            raise ValueError(f"Input must have exactly {self.n_var} variables.")

        fitness1 = sum(pw(xi, 2) for xi in x)
        fitness2 = pw(sum(0.5 * (i + 1) * xi for i, xi in enumerate(x)), 2)
        fitness3 = pw(sum(0.5 * (i + 1) * xi for i, xi in enumerate(x)), 4)
        fitness = fitness1 + fitness2 + fitness3
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
