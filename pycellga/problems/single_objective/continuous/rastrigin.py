from numpy import cos, pi
from typing import List
from problems.abstract_problem import AbstractProblem
from common import GeneType

class Rastrigin(AbstractProblem):
    """
    Rastrigin function implementation for optimization problems.

    The Rastrigin function is widely used for testing optimization algorithms.
    It is typically evaluated on the hypercube x_i ∈ [-5.12, 5.12], for all i = 1, 2, ..., n.

    Attributes
    ----------
    gen_type : GeneType
        The type of genes used in the problem, set to REAL.
    n_var : int
        The number of variables (dimensions) in the problem.
    xl : float
        The lower bound for each variable, set to -5.12.
    xu : float
        The upper bound for each variable, set to 5.12.

    Methods
    -------
    f(x: List[float]) -> float
        Computes the Rastrigin function value for a given solution.
    """

    def __init__(self, n_var: int = 2):
        """
        Initialize the Rastrigin problem with the specified number of variables.

        Parameters
        ----------
        n_var : int, optional
            The number of design variables (dimensions), by default 2.
        """
        gen_type = GeneType.REAL
        xl = -5.12
        xu = 5.12

        super().__init__(gen_type=gen_type, n_var=n_var, xl=xl, xu=xu)

    def f(self, x: List[float]) -> float:
        """
        Calculate the Rastrigin function value for a given list of variables.

        Parameters
        ----------
        x : list
            A list of float variables.

        Returns
        -------
        float
            The computed Rastrigin function value.
        """
        if len(x) != self.n_var:
            raise ValueError(f"Input must have exactly {self.n_var} variables.")

        A = 10.0
        fitness = (A * self.n_var) + sum([(xi ** 2) - (A * cos(2 * pi * xi)) for xi in x])
        return round(fitness, 3)
