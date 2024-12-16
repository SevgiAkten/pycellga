from problems.abstract_problem import AbstractProblem
from mpmath import power as pw
from typing import List
from common import GeneType


class Pow(AbstractProblem):
    """
    Pow function implementation for optimization problems.

    The Pow function is typically used for testing optimization algorithms.
    It is evaluated on the hypercube x_i ∈ [-5.0, 15.0] with the goal of reaching 
    the global minimum at f(5, 7, 9, 3, 2) = 0.

    Attributes
    ----------
    gen_type : GeneType
        The type of genes used in the problem (REAL).
    n_var : int
        The number of design variables.
    xl : float
        The lower bound for the variables (-5.0).
    xu : float
        The upper bound for the variables (15.0).

    Methods
    -------
    f(x: List[float]) -> float
        Compute the Pow function value for a given solution.
    """

    def __init__(self, n_var: int = 5):
        """
        Initialize the Pow problem.

        Parameters
        ----------
        n_var : int, optional
            The number of variables (dimensions) in the problem, by default 5.
        """
        gen_type = GeneType.REAL
        xl = -5.0
        xu = 15.0

        super().__init__(gen_type=gen_type, n_var=n_var, xl=xl, xu=xu)

    def f(self, x: List[float]) -> float:
        """
        Compute the Pow function value for a given solution.

        Parameters
        ----------
        x : list of float
            A list of float variables representing a point in the solution space.

        Returns
        -------
        float
            The computed fitness value for the given solution.
        """
        if len(x) != self.n_var:
            raise ValueError(f"Input must have exactly {self.n_var} variables.")

        # Define the target values
        target = [5, 7, 9, 3, 2]

        # Compute the fitness as the sum of squared differences
        fitness = sum(pw(xi - ti, 2) for xi, ti in zip(x, target))
        return round(fitness, 2)
