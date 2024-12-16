from mpmath import power as pw
from typing import List
from problems.abstract_problem import AbstractProblem
from common import GeneType


class Zettle(AbstractProblem):
    """
    Zettle function implementation for optimization problems.

    The Zettle function is widely used for testing optimization algorithms.
    It is typically evaluated on the hypercube x_i ∈ [-5, 5].

    Attributes
    ----------
    n_var : int
        Number of variables (dimensions) in the problem.
    gen_type : GeneType
        Type of genes used in the problem (REAL).
    xl : float
        Lower bounds for the variables, fixed to -5.
    xu : float
        Upper bounds for the variables, fixed to 5.

    Methods
    -------
    f(x: list) -> float
        Compute the Zettle function value for a given solution.
    evaluate(x: list, out: dict, *args, **kwargs) -> None
        Pymoo-compatible evaluation method for batch processing.
    """

    def __init__(self, n_var: int = 2):
        """
        Initialize the Zettle problem.

        Parameters
        ----------
        n_var : int, optional
            Number of variables (dimensions) for the problem, by default 2.
        """
        gen_type = GeneType.REAL
        xl = -5.0
        xu = 5.0

        super().__init__(gen_type=gen_type, n_var=n_var, xl=xl, xu=xu)

    def f(self, x: List[float]) -> float:
        """
        Compute the Zettle function value for a given solution.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The Zettle function value, rounded to six decimal places.
        """
        if len(x) != self.n_var:
            raise ValueError(f"Input must have exactly {self.n_var} variables.")
        
        fitness = 0.0
        for i in range(len(x) - 1):
            fitness += pw((pw(x[i], 2) + pw(x[i + 1], 2)) - 2 * x[i], 2) + 0.25 * x[i]

        return round(fitness, 6)

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
