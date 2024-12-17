
from mpmath import power as pw

from pycellga.problems.abstract_problem import AbstractProblem
from pycellga.common import GeneType

class Matyas(AbstractProblem):
    """
    Matyas function implementation for optimization problems.

    The Matyas function is commonly used to evaluate the performance of optimization algorithms.
    It is a simple, continuous, convex function that has a global minimum at the origin.

    Attributes
    ----------
    gen_type : GeneType
        The type of genes used in the problem (fixed to REAL).
    n_var : int
        Number of variables (dimensions) in the problem (fixed to 2).
    xl : float
        Lower bound for the variables (fixed to -10).
    xu : float
        Upper bound for the variables (fixed to 10).

    Methods
    -------
    f(x: list) -> float
        Computes the Matyas function value for a given solution.
    """

    def __init__(self):
        """
        Initialize the Matyas problem.

        This problem is defined for exactly 2 variables with bounds [-10, 10].

        Parameters
        ----------
        None
        """
        gen_type = GeneType.REAL
        n_var = 2
        xl = -10.0
        xu = 10.0

        super().__init__(gen_type=gen_type, n_var=n_var, xl=xl, xu=xu)

    def f(self, x):
        """
        Compute the Matyas function value for a given solution.

        Parameters
        ----------
        x : list of float
            A list of float variables representing a point in the solution space.

        Returns
        -------
        float
            The computed fitness value for the given solution.
        """
        if len(x) != 2:
            raise ValueError("Matyas function is defined for exactly 2 variables.")

        x1, x2 = x
        fitness = 0.26 * (pw(x1, 2) + pw(x2, 2)) - 0.48 * x1 * x2
        return round(fitness, 2)
